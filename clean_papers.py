import re, glob, os, json, sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

ROOT = os.path.dirname(os.path.abspath(__file__))

HEADING_RE = re.compile(r'^(#{1,6})\s+(.*\S)\s*$')

ADMIN_ALWAYS = [
    'references', 'reference list', 'bibliography', 'works cited',
    'article history', 'article info',
    'acknowledg',
    'funding', 'financial support', 'sources of funding',
    'role of the funding source', 'role of the sponsor',
    'competing interest', 'conflict of interest', 'conflicts of interest',
    'conflicting interest', 'declaration of competing interest', 'disclosure',
    'author contribution', "authors' contribution", 'credit authorship',
    'contributors', 'author affiliations', 'author details',
    'data availability', 'data sharing', 'availability of data',
    'supplementary', 'supporting information', 'supplemental material', 'supplemental data',
    'declarations', 'declaration of interest',
    'ethics statement', 'ethical approval', 'ethics approval',
    'informed consent statement', 'institutional review board statement',
    'consent to participate', 'consent for publication', 'consent statement',
    'human and animal rights', 'patient consent',
    'orcid',
    'provenance and peer review', 'peer review', 'open peer review',
    'abbreviations',
    'additional information',
    'reporting summary',
    'hhs public access',
    'public domain notice', 'electronic access and printed copies',
    'recommended citation', 'originating office', 'nondiscrimination notice',
    'trial registration',
    "publisher's note", 'publishers note',
    'footnotes',
    'contents', 'table of contents',
]

# Ambiguous / masthead-ish headings: only drop if the section content is short
# (guards against PDF-extraction artifacts where real content — e.g. an
# unheaded abstract — got merged into one of these blocks)
ADMIN_LENGTH_GUARDED = [
    'citation', 'copyright', 'edited by', 'reviewed by',
    'specialty section', 'correspondence', 'patient and public involvement',
]
GUARD_CHARS = 600

MASTHEAD_TAGS = {
    'review', 'original article', 'research article', 'article', 'article open',
    'open access', 'editorial', 'commentary', 'short communication', 'case report',
    'letter', 'systematic review', 'research paper', 'original research', 'letters',
    'perspective', 'viewpoint', 'brief report', 'rapid communication',
}
MASTHEAD_GUARD_CHARS = 200

LINE_NOISE_PATTERNS = [
    re.compile(r'^Contents lists available at', re.I),
    re.compile(r'jour\s*nal\s*home\s*page', re.I),
    re.compile(r'^\xa9\s*\d{4}'),
    re.compile(r'^©\s*\d{4}'),
    re.compile(r'^\d+\s+of\s+\d+\s*,?\s+\d{1,2}/\d{1,2}/\d{2,4}'),
    re.compile(r'^doi:\s*10\.\S+$', re.I),
    re.compile(r'^ISSN\b', re.I),
    re.compile(r'^\[[^\]]+\]\([^)]+\)$'),
    re.compile(r'^-\s*<sup>[a-zA-Z0-9∗*]+</sup>'),
    re.compile(r'^<sup>[∗*]</sup>\s*Corresponding author', re.I),
    re.compile(r'^[∗*]\s*Corresponding author', re.I),
    re.compile(r'^E-mail address:', re.I),
    re.compile(r'^Photo by \xa9', re.I),
    re.compile(r'^Photo by ©', re.I),
]

ARTICLE_INFO_SPACED = re.compile(r'^a\s*r\s*t\s*i\s*c\s*l\s*e\s*i\s*n\s*f\s*o$', re.I)
ABSTRACT_SPACED = re.compile(r'^a\s*b\s*s\s*t\s*r\s*a\s*c\s*t$', re.I)
# PDF pagination artifacts masquerading as headings (e.g. "## Page 27") — these
# are false section breaks that must NOT interrupt the section they fall inside.
PAGE_MARKER_RE = re.compile(r'^page\s+[0-9ivxlc]+$', re.I)


def normalize_heading(text):
    t = text
    t = re.sub(r'<[^>]+>', '', t)
    t = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', t)  # unwrap markdown links
    t = re.sub(r'[*_`]', '', t)
    t = t.strip()
    # strip leading numbering / bullets: "1.", "3.1.", "9.", "■", "-", "*"
    t = re.sub(r'^[■●\-\*•]+\s*', '', t)
    t = re.sub(r'^\(?[0-9]+(\.[0-9]+)*\)?[.\):]?\s+', '', t)
    t = t.strip().rstrip(':').strip()
    t = re.sub(r'\s+', ' ', t)
    return t.lower()


def split_sections(lines):
    sections = []
    cur = {'heading_raw': None, 'norm': '', 'lines': []}
    for line in lines:
        m = HEADING_RE.match(line)
        if m and PAGE_MARKER_RE.match(normalize_heading(m.group(2))):
            continue  # drop pagination artifact, don't let it break the section
        if m:
            sections.append(cur)
            cur = {'heading_raw': line.rstrip('\n'), 'norm': normalize_heading(m.group(2)), 'lines': []}
        else:
            cur['lines'].append(line)
    sections.append(cur)
    return sections


def classify(section):
    """Return 'drop', 'keep', or 'articleinfo'."""
    norm = section['norm']
    if section['heading_raw'] is None:
        return 'keep'
    compact = norm.replace(' ', '')
    if ARTICLE_INFO_SPACED.match(norm) or compact == 'articleinfo':
        return 'articleinfo'
    content_text = ''.join(section['lines']).strip()
    if norm in MASTHEAD_TAGS:
        return 'drop' if len(content_text) < MASTHEAD_GUARD_CHARS else 'keep'
    for pat in ADMIN_LENGTH_GUARDED:
        if pat in norm:
            return 'drop' if len(content_text) < GUARD_CHARS else 'keep'
    for pat in ADMIN_ALWAYS:
        if pat in norm:
            return 'drop'
    return 'keep'


def filter_lines(lines):
    out = []
    for line in lines:
        stripped = line.rstrip('\n')
        if any(p.search(stripped) for p in LINE_NOISE_PATTERNS):
            continue
        out.append(line)
    return out


def fix_heading_line(heading_raw):
    m = HEADING_RE.match(heading_raw)
    hashes, text = m.group(1), m.group(2)
    norm_check = re.sub(r'[*_`]', '', text).strip()
    if ABSTRACT_SPACED.match(norm_check):
        return '## Abstract'
    return heading_raw


def process_file(path):
    with open(path, encoding='utf-8') as f:
        lines = f.readlines()
    sections = split_sections(lines)

    out_lines = []
    stats = {'kept': [], 'dropped': [], 'articleinfo': []}

    for sec in sections:
        action = classify(sec)
        if sec['heading_raw'] is None:
            out_lines.extend(filter_lines(sec['lines']))
            continue
        label = sec['norm'] if sec['norm'] else '(untitled)'
        if action == 'drop':
            stats['dropped'].append(label)
            continue
        elif action == 'articleinfo':
            stats['articleinfo'].append(label)
            kw_lines = [l for l in sec['lines'] if re.match(r'^\s*Keywords?\s*[:\s]', l, re.I)]
            for kw in kw_lines:
                out_lines.append(kw)
            continue
        else:
            stats['kept'].append(label)
            out_lines.append(fix_heading_line(sec['heading_raw']) + '\n')
            out_lines.extend(filter_lines(sec['lines']))

    # collapse 3+ blank lines to 1
    text = ''.join(out_lines)
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = text.strip() + '\n'
    return text, stats


def main():
    files = sorted(glob.glob(os.path.join(ROOT, '*', '*.md')))
    files = [f for f in files if not f.endswith('_clean.md')]
    report = []
    for f in files:
        text, stats = process_file(f)
        base = os.path.splitext(f)[0]
        out_path = base + '_clean.md'
        with open(out_path, 'w', encoding='utf-8') as out:
            out.write(text)
        orig_size = os.path.getsize(f)
        new_size = len(text.encode('utf-8'))
        report.append({
            'file': os.path.relpath(f, ROOT),
            'orig_bytes': orig_size,
            'clean_bytes': new_size,
            'pct_kept': round(100 * new_size / orig_size, 1) if orig_size else 0,
            'dropped_sections': stats['dropped'],
            'articleinfo_sections': stats['articleinfo'],
        })
    with open(os.path.join(ROOT, 'clean_report.json'), 'w', encoding='utf-8') as rf:
        json.dump(report, rf, indent=1)

    print(f"Processed {len(report)} files.\n")
    for r in report:
        flag = ''
        if r['pct_kept'] > 95:
            flag = '  <-- almost nothing dropped (check)'
        if r['pct_kept'] < 30:
            flag = '  <-- large reduction (check)'
        print(f"{r['file']:45s} {r['orig_bytes']:>8d} -> {r['clean_bytes']:>8d} ({r['pct_kept']:>5.1f}%){flag}")


if __name__ == '__main__':
    main()
