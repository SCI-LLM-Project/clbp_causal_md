# **Smoking, alcohol and cofee consumption and risk of low back pain: a Mendelian randomization study**

**Zhengtao Lv<sup>1</sup> · Jiarui Cui2 · Jiaming Zhang[1](http://orcid.org/0000-0001-8520-566X)**

Received: 7 May 2022 / Revised: 7 May 2022 / Accepted: 12 September 2022 / Published online: 16 September 2022 © The Author(s), under exclusive licence to Springer-Verlag GmbH Germany, part of Springer Nature 2022

## Abstract

**Purpose** Low back pain (LBP) is a common health problem in the global population. This study aims to assess whether smoking initiation, alcohol consumption, and cofee consumption are causally with an increased risk of LBP.

**Methods** A two-sample Mendelian Randomization (MR) study was designed, based on summary-level data from the largest published genome-wide association studies. Single nucleotide polymorphisms with genome-wide signifcance level (*P*<5.0× 10−8) were selected as instrumental variables for each exposure. Standard inverse-variance weighted (IVW) method was used as the primary statistical method. The weighted median, MR-Egger regression, and MR-PRESSO methods, which relax some IV assumptions, were used for sensitivity analysis.

**Results** Genetically predicted smoking initiation was causally associated with higher odds of LBP. The pooled OR of LBP using IVW method was 1.36 (95%CI 1.22 1.52; P=6.0× 10−8) for one SD increase in the prevalence of smoking initiation, which was supported by the weighted median method (OR: 1.41, 95%CI 1.22, 1.64; *P*=5.7× 10−6). Sensitivity analysis confrmed the robustness of pooled OR of LBP. There was no evidence to suggest a causal efect of alcohol and cofee consumption on LBP. The pooled ORs of LBP were 1.36 (95%CI 0.94, 1.97; *P*=0.10) for alcohol consumption and 1.00 (95%CI 0.99, 1.00; *P*=0.17) for cofee consumption, respectively.

**Conclusion** Smoking is casually associated with an increased risk of LBP. Smoking control should be recommended in LBP patients to avoid worsening the disease. The safety of LBP with moderate alcohol and cofee consumption merits more study.

**Keywords** Low back pain · Smoking · Alcohol consumption · Cofee consumption · Causal efect · Mendelian randomization

## **Introduction**

Low back pain (LBP) is a common health problem in the global population and is generally defned as pain, muscle tension or stifness that occurs below the costal margin and

- \* Jiarui Cui jrffairybabi@163.com
- \* Jiaming Zhang jiaming\_zhangtjmc@icloud.com Zhengtao Lv 630105736@qq.com

above the inferior gluteal folds, with or without leg pain (sciatica) and associated neurological symptoms of the lower limbs [[1–](#page-5-0)[3](#page-5-1)]. Most people experience at least one episode of acute LBP during their lives [[4\]](#page-5-2), which is usually selflimiting and lasts only a few days [[2\]](#page-5-3). However, recurring bouts are typical, and LBP frequently develops into chronic condition [\[5](#page-5-4)]. Disability-adjusted life year (DALY) of LBP grew 46.9% in 2019 compared to 1990, making it the fourth leading cause of DALY in the 25–49 age range [[6\]](#page-5-5), which undoubtedly increases the burden on global health care and social support systems, particularly in low-and middleincome countries [\[2](#page-5-3)].

Several lifestyle factors have been proposed as risk factors for the occurrence of LBP, such as smoking [[7](#page-5-6)], alcohol [[8\]](#page-5-7), and cofee consumption [[9\]](#page-5-8). However, the available data on the associations between the three factors and LBP are inconsistent [[10–](#page-5-9)[12](#page-5-10)], and whether the associations are

causal remains unclear due to various potential biases such as residual confounding and reverse causality.

Because genetic variants are randomly assigned during conception, a specifc exposure is generally independent of other exposures or environmental factors and cannot be afected by disease status. Mendelian randomization (MR) design using genetic variants as exposure (e.g., smoking) that can help to overcome residual confounding and avoid reverse causality bias, while also improving causal inference in exposure-disease associations. Here, we conducted a two-sample MR study to assess the association of smoking initiation, alcohol consumption, and cofee consumption with an increased risk of LBP.

## **Methods**

### **Study design**

We adopted a two-sample MR design based on summarylevel data from the largest published genome-wide association studies (GWASs) to identify the causal association of smoking initiation (ever smoked regularly), alcohol consumption, cofee consumption and LBP. MR studies use genetic variants as instrumental variables (IVs), mostly single nucleotide polymorphisms (SNPs), that signifcantly associated with an exposure to estimate its causal efect on an outcome. For the validity of IVs in our study, three assumptions must be satisfed: (i) the SNPs should be associated with lifestyle factors (the exposure); (ii) the SNPs are not related to confounders of the lifestyle-LBP associations; (iii) the SNPs afect LBP only through the lifestyle factors.

## **Data source for LBP**

The summary dataset for the associations between SNPs and LBP was retrieved by searching GWAS ID: fnn-b-M13\_ LOWBACKPAIN on the website [https://gwas.mrcieu.ac.](https://gwas.mrcieu.ac.uk/) [uk/](https://gwas.mrcieu.ac.uk/) (accessed on 1 February 2022). This GWAS is the latest one regarding LBP and was updated in 2021. It includes 13,178 cases with LBP and 164,682 controls, with a number of 16,380,287 SNPs being tested. All the participants are from European ancestry.

### **Data source for exposures**

For SNPs that associated with each exposure phenotype, we collected summary statistics (betas and SEs) from published GWASs restricted to European-ancestry individuals [\[13,](#page-5-11) [14](#page-5-12)]. The SNPs were selected at the genome-wide signifcance level (*P*<5.0× 10−8), with a minor allele frequency (MAF)≥0.01. We retained independent SNPs with a pairwise *r*2<0.001 and a clump window of 10000 kb for MR

For smoking initiation, a total of 378 SNPs were identifed as IVs based on the results of a recent meta-analysis of GWASs including 1,232,091 individuals of European ancestry [[14](#page-5-12)]. For the number of alcoholic drinks per week, 99 SNPs were identifed through a meta-analysis of GWASs of 941,280 individuals of European descents [\[14](#page-5-12)]. All the association tests were adjusted for age, sex and the frst ten genetic principal components. Efect estimates for SNPs robustly associated with cofee consumption were obtained from a GWAS on self-reported bitter and sweet beverage consumption, including cofee (European ancestry, *n*=375,833) [[13\]](#page-5-11). These instruments have been used by pervious MR studies [[19–](#page-5-17)[23\]](#page-6-0). In the harmonizing process, SNPs were removed if they were palindromic with intermediate allele frequencies. SNPs unavailable in LBP dataset were also removed. Finally, a total number of 334 SNPs, 89 SNPs and 14 SNPs were considered as IVs for smoking initiation, alcohol consumption and cofee consumption, respectively. Figure [1](#page-2-0) provides an overview and assumptions of the MR study design, along with the number of SNPs selected for each exposure phenotype.

### **Statistical analysis**

All the analyses were performed with R (version 4.1.3), TwoSampleMR (0.5.5) [[24\]](#page-6-1), Mendelian Randomization (0.5.0) [[25](#page-6-2)], and MR-PRESSO package [[26](#page-6-3)]. To address multiple testing, we applied a Bonferroni-corrected P value of 0.017 (0.05/3 putative exposures) to indicate statistical signifcance. All the P values reported were two-sided. The odds ratios (ORs) and corresponding 95% confdence intervals (95%CIs) of LBP for exposures were scaled to oneunit increase in genetically predicted smoking (expressed as log odds of ever smoked regularly), alcohol consumption (expressed as standard deviations of log-transformed drinks per week), and 50% change in cups of cofee intake per day. The F-statistics for each exposure was calculated using the previously described approximation method [\[27\]](#page-6-4).

We used the standard inverse-variance weighting (IVW) method (under random-effect model) as the primary

<span id="page-2-0"></span>**Fig. 1** Overall and assumptions of the Mendelian randomization (MR) study. Assumption 1 indicates that the SNPs selected as instrumental variables should be robustly associated with lifestyle factors (the exposure). Assumption 2 indicates that the SNPs are not related

to confounders of the lifestyle-LBP associations. Assumption 3 indicates that the SNPs afect LBP only through the lifestyle factors, rather than via alternative pathways. SNP: single nucleotide polymorphism; IVW: inverse-variance weighted

statistical method, which assumed that each SNP was a valid IV. The IVW method combines the Wald ratio with a metaanalytic approach and provides the most precise estimation of associations but it is sensitive to invalid instrumental variables with pleiotropic efects [\[28](#page-6-5)]. Heterogeneity across genetic variants was tested using the Cochrane's Q-statistics [\[28\]](#page-6-5).

The weighted median, MR-Egger regression, and MR-PRESSO methods, which relax some IV assumptions, were used for sensitivity analysis. The weighted median method provides consistent estimates provided that more than half of the weight in the analysis were from valid instruments [[27\]](#page-6-4). The MR-Egger regression method can identify and adjust directional pleiotropy. The MR-Egger slope ofers an estimate of the pleiotropy-corrected causal estimate but generally this model compromises statistical power [\[27\]](#page-6-4). The P value for the MR-Egger intercept was used to indicate pleiotropy [[27\]](#page-6-4). The MR-PRESSO approach aims to detect outliers (global test) and generates an estimate after the removal of these outliers [[26\]](#page-6-3). The P value for MR-PRESSO distortion test was used as an indication of signifcant diference in estimates before and after outlier correction [\[26](#page-6-3)].

## **Results**

The scatter plots of associations between genetically predicted smoking initiation, alcohol consumption, coffee consumption and risk of LBP were shown in Fig. [2.](#page-3-0) Genetically predicted smoking initiation was causally associated with higher odds of LBP, albeit null association for the MR-Egger regression analysis (Table [1](#page-3-1)). The pooled OR of LBP using IVW method was 1.36 (95%CI 1.22 1.52; *P*=6.0× 10−8) for one SD increase in the prevalence of smoking initiation, which was supported by the weighted median method (OR: 1.41, 95%CI 1.22, 1.64; *P* = 5.7 × 10−6). The *P* value for MR-Egger regression analysis indicated no directional pleiotropy (Egger intercept=0.0024, *P*= 0.62). Furthermore, the MR-PRESSO model detected several outliers but the outlier-corrected estimate of efect remained unchanged (distortion test P value = 0.97). There was evidence for signifcant intravariant heterogeneity (IVW mode: *P*=8.7× 10−7), but the leave-one-out sensitivity analysis confrmed the robustness of pooled results, as the estimated efect size remained unchanged after the exclusion of any SNP selected.

In terms of alcohol consumption and cofee consumption, there was no evidence to suggest a causal association on LBP (Table [1](#page-3-1)). The pooled ORs of LBP were 1.36 (95%CI 0.94, 1.97; *P*=0.10) for alcohol consumption and 1.00 (95%CI 0.99, 1.00; *P* = 0.17) for cofee consumption, respectively. These null associations were further confrmed by sensitivity analyses (Table [1](#page-3-1)). There was no evidence to indicate directional pleiotropy in the MR-Egger regression analysis (*P*=0.57 for alcohol consumption and 0.42 for cofee consumption). Several outliers were identifed in the analysis of alcohol consumption, but the distortion test suggested no signifcant changes between estimates before and after the correction of outliers (*P*=0.45).

<span id="page-3-0"></span>**Fig. 2** Scatter plots showing the efects of **A** smoking initiation, **B** alcohol consumption, **C** cofee consumption on the risk of LBP. Each point represents the per allele association with exposure plotted against per allele association with LBP. LBP: low back pain

<span id="page-3-1"></span>**Table 1** Causal efects of smoking initiation, alcohol consumption, and cofee consumption on LBP using MR analyses

| Exposure                     | MR method                 | OR (95%CI)        | Beta (SE)        | P         | P-het     | P-pleio |
|------------------------------|---------------------------|-------------------|------------------|-----------|-----------|---------|
| Smoking initiation: 285 SNPs | MR Egger                  | 1.19 (0.72, 1.99) | 0.18 (0.26)      | 0.49      | 7.6× 10−7 |         |
|                              | MR Egger intercept        |                   | 0.0024 (0.0048)  |           |           | 0.62    |
|                              | Weighted median           | 1.41 (1.22, 1.64) | 0.34 (0.08)      | 5.7× 10−6 |           |         |
|                              | IVW                       | 1.36 (1.22, 1.52) | 0.31 (0.06)      | 6.0× 10−8 | 8.7× 10−7 |         |
|                              | MR-PRESSO distortion test |                   |                  | 0.97      |           |         |
| Alcohol consumption: 68 SNPs | MR Egger                  | 1.77 (0.67, 4.67) | 0.57 (0.49)      | 0.25      | 0.029     |         |
|                              | MR Egger intercept        |                   | −0.0032 (0.0056) |           |           | 0.57    |
|                              | Weighted median           | 1.41 (0.88, 2.28) | 0.35 (0.24)      | 0.16      |           |         |
|                              | IVW                       | 1.36 (0.94, 1.97) | 0.31 (0.19)      | 0.10      | 0.033     |         |
|                              | MR-PRESSO distortion test |                   |                  | 0.45      |           |         |
| Cofee consumption: 13 SNPs   | MR Egger                  | 1.00 (0.99, 1.01) | 0.00019 (0.0040) | 0.96      | 0.73      |         |
|                              | MR Egger intercept        |                   | −0.0083 (0.010)  |           |           | 0.42    |
|                              | Weighted median           | 1.00 (0.99, 1.00) | −0.0028 (0.0028) | 0.31      |           |         |
|                              | IVW                       | 1.00 (0.99, 1.00) | −0.0027 (0.0019) | 0.17      | 0.75      |         |
|                              | MR-PRESSO distortion test |                   |                  | 0.68      |           |         |

Beta was the estimated efect size; OR: odds ratio; 95%CI: 95% confdence interval; SE: standard error; SNP: single nucleotide polymorphism; MR: Mendelian randomization; IVW: inverse-variance weighted; P-het: *P* value for heterogeneity test; P-pleio: *P* value for pleiotropy test using MR-Egger regression analysis; *P*<0.05 was considered statistically signifcant

## **Discussion**

In this two-sample MR study of the three lifestyle factors and LBP risk, we found a positive association between smoking and a higher risk of LBP but did not support any association of alcohol and cofee consumption with the occurrence of LBP. To our knowledge, this is the frst study to investigate the potential causal associations between modifable risk factors and LBP risk based on genetic data from large GWASs.

The results show a causal efect of smoking initiation on the higher risk of LBP, which is consistent with the fndings of most but not all previous research. A systematic review of 40 cross-sectional and cohort studies found an association between smoking initiation and the prevalence

of LBP, particularly chronic LBP and disabling LBP [\[29](#page-6-6)]. Current and past smokers have higher prevalence and incidence of LBP than never smokers, while past smokers have lower LBP prevalence than current smokers [\[29\]](#page-6-6). This is in-line with the fndings of a subsequent large-scale longitudinal study involving 204,066 men, which indicated that smokers were at higher risk for LBP than non-smokers in male samples [[30](#page-6-7)]. A similar association was also discovered in a number of cross-sectional research conducted in a variety of settings, including military, school, community, and hospital [[31](#page-6-8)[–34\]](#page-6-9). Current smoking status and higher nicotine dependence were both found to be independently linked to an elevated risk of chronic LBP [[35](#page-6-10), [36](#page-6-11)]. However, smoking was neither a risk nor a prognostic factor for LBP, according to the data from a prospective longitudinal cohort study of 17,962 subjects in Sweden. This could be due to that the study included past and occasional smokers, as well as non-smokers, as a reference group for daily smokers, or because smoking was underreporting, making the association between smoking and LBP difcult to detect [\[37](#page-6-12)]. Based on the latest updated genetic data from GWASs, the present study confrmed that smoking is a causative risk factor for LBP. There are various plausible explanations for the increased risk of LBP associated with smoking. First, smoking reduces bone mineral content and raises the risk of osteoporosis and vertebral body micro-injury, accelerating degenerative changes in the spine [\[38](#page-6-13)]. Second, smoking causes more frequent coughs, which leads to increased intradiscal and intra-abdominal pressure that raises the risk of disc herniation [\[34](#page-6-9)]. Finally, smoking reduces blood fow to the intervertebral discs, resulting in metabolic imbalance of the discs and, eventually, disc degeneration [[39\]](#page-6-14).

Conficting evidence exists regarding the association between alcohol consumption and LBP risk. A previous systematic review reported no research that showed a positive association between alcohol consumption and LBP, as well as no positive gradients in dose–response studies [\[40](#page-6-15)]. Nonetheless, a follow-up meta-analysis of 26 studies found a small association between alcohol consumption and the prevalence of LBP, which appears to exist exclusively in those with alcohol consumption dependence and complex or chronic LBP [\[41](#page-6-16)]. A longitudinal study of young people aged 12 to 22 years reported a negative association between adolescent alcohol consumption and adult LBP, implying that alcohol consumption may protect against future episodes of LBP [\[8](#page-5-7)]. Although the current MR study fnds no causal link between alcohol consumption and LBP risk, the possibility of overlooking a weak association cannot be ruled out.

There is also disagreement among the results from diferent studies when it comes to the efect of cofee consumption on LBP risk. Individuals who consumed six or more cups of cofee per day had a 16-fold greater risk of non-specifc LBP recurrence in a study of 609 medical personnel in northeastern Poland [[42\]](#page-6-17). Another study of 134 postmenopausal women found a signifcant association between cofee consumption and LBP [\[43\]](#page-6-18). However, a cross-sectional study of undergraduate medical students from India shed lights on a conficting result that cofee consumption, whether regular or occasional, was not linked with LBP [\[9](#page-5-8)]. Another piece of evidence from 1335 young adults in India supports this [[44](#page-6-19)]. All the above studies were supposed to be cross-sectional. To better elucidate this issue, we performed the current MR study, which demonstrated no association between cofee consumption and LBP risk.

Our study found no directional pleiotropy in the analysis of smoking initiation using MR-Egger regression. Several outliers were observed in the MR-PRESSO analysis, but the outlier-corrected efect estimates remained unchanged, indicating that the results are likely valid. Furthermore, smoking-related variants may be connected to multiple systems involved in nicotinic, dopaminergic, and glutamatergic neurotransmission. This study could not rule out the potential that LBP risk may be linked to other factors or behaviours that result from diferences in neurotransmission.

There are several strengths of this study. First, we employed the MR method to investigate causal associations of smoking initiation, alcohol consumption, and cofee consumption on the higher risk of LBP from publicly available large GWAS datasets. Since the genetic variant alleles are assigned randomly, residual confounding and reverse causality that may be present in observational studies are minimized. Second, we used three MR analysis methods to support the robustness and efectiveness of our causal estimates, including MR-Egger, weighted median, and IVW. Finally, we limited the study population to individuals of European decent to mitigate possible bias owing to population stratifcation.

There are few limits that need to be considered as well. The main disadvantage is that we were unable to analyse the potential for a nonlinear association between alcohol and cofee consumption and LBP. As a result, the null association between alcohol and LBP risk cannot be interpreted as no causal associations, making it impossible to detect a weak association with these exposures. Second, we were unable to specify the efects of lifestyle factors on diferent subtypes of LBP due to the lack of information. Furthermore, we only included Europeans in our study, limiting the generalizability of our fndings to other populations.

## **Conclusion**

In summary, our MR study provides evidence that smoking is casually associated with an increased risk of LBP. Smoking control should be recommended in LBP patients to avoid

worsening the disease. The safety of LBP with moderate alcohol and cofee consumption merits more study.

**Supplementary Information** The online version contains supplementary material available at<https://doi.org/10.1007/s00586-022-07389-3>.

**Acknowledgements** Not applicable.

**Funding** This work received no specifc grants from any funding agency in the public, commercial, or not-for-proft sectors.
