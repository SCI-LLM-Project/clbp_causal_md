FISEVIER

# Sleep Medicine

# Causal assessment of sleep on coronary heart disease

Li-zhen Liao <sup>a, b, 1</sup>, Wei-dong Li <sup>a, b, 1</sup>, Ying Liu <sup>a, b</sup>, Jia-ping Li <sup>c</sup>, Xiao-dong Zhuang <sup>c</sup>, Xin-xue Liao <sup>c, \*</sup>

- <span id="page-0-0"></span><sup>a</sup> Guangdong Pharmaceutical University, Guangzhou Higher Education Mega Center, Guangzhou, GuangDong, PR China
- <span id="page-0-1"></span><sup>b</sup> Guangdong Engineering Research Center for Light and Health, Guangzhou Higher Education Mega Center, Guangzhou, GuangDong, PR China
- <span id="page-0-3"></span><sup>c</sup> The First Affiliated Hospital of Sun Yat-Sen University, 58 Zhongshan 2nd Road, Yue Xiu, GuangZhou, 510080, GuangDong, PR China

Keywords: Mendelian randomization Sleep Coronary heart disease
#### ARSTRACT

Objective: Sleep is an essential physiological process that protects our physical and mental health. However, the causality of the association between sleep and coronary heart disease (CHD) is unknown. Mendelian randomization (MR), using genetic variants as instrumental variables to test for causality, can infer credible causal associations. We applied a two-sample MR framework to determine the causal association between sleep (sleeplessness, sleep duration, and daytime dozing) and CHD by integrating summary-level genome-wide association study (GWAS) data.

Methods: Data included in this study were the GWAS summary statistics datasets from the C4D Consortium for CHD; Neale Lab UKB-a:13 Consortium for sleeplessness; Neale Lab UKB-a:9 Consortium for sleep duration and Neale Lab UKB-a:15 Consortium for daytime dozing. The conventional MR approach (inverse variance weighted, IVW) method and Egger method were used. Heterogeneity was calculated using each of the different MR methods where possible. Horizontal pleiotropy was evaluated by *p*-value of the MR—Egger intercept.

Results: The IVW method estimate indicated that the odds ratio (OR) (95% confidence interval, CI) for CHD was 3.924 (1.345-11.447) per standard deviation increase in sleeplessness (p=0.012). Results were consistent in MR–Egger method (OR, 4.654; 95% CI, 1.191-18.186; p=0.009). The genetically predicted sleeplessness was positively casually associated with CHD. The causal association between sleep duration (or daytime dozing) and CHD was not established.

*Conclusion:* Our analysis provided evidence supporting a causal relationship between sleeplessness (not sleep duration or daytime dozing) and CHD.

### 1. Introduction

Coronary heart disease (CHD) has become a major health concern over the past several decades, representing a major public health burden worldwide [1]. Sleep is an essential physiological process that protects our physical and mental health. Epidemiological studies suggest that too long (or too short) duration and poor sleep quality are related to an increased subclinical atherosclerosis [2] and cardiovascular risk [3]. However, the causality of the association between sleep and CHD is unknown; thus, there is a need to clarify the true association between them.

Mendelian randomization (MR), using genetic variants as instrumental variables to test for causality, can infer credible causal

associations. Causal inference from an MR study relies on the instrumental variable assumptions, which require that the genetic variant is robustly associated with the exposure; independent of confounders of the exposure—outcome relationship; and influences the outcome through the exposure only and not through any alternative causal pathway (Fig. 1) [4]. We applied a two-sample MR framework to determine the causal association between sleep (sleeplessness, sleep duration, and daytime dozing) and CHD by integrating summary-level genome-wide association study (GWAS) data.

#### 2. Methods

## 2.1. Summary of GWAS data

We included summary data from any array-based analysis, including targeted and untargeted arrays, with or without

<span id="page-0-4"></span><sup>\*</sup> Corresponding author. Cardiology Department, The First Affiliated Hospital of Sun Yat-sen University, 58 Zhongshan 2nd Road, Guangzhou, 510080, PR China. E-mail addresses: zhuangxd3@mail.sysu.edu.cn (X.-d. Zhuang), liaoxinx@mail.

<span id="page-0-2"></span>sysu.edu.cn (X.-x. Liao).

These authors contributed equally to this study.

<span id="page-1-0"></span>**Fig. 1.** Instrumental variables assumptions for Mendelian randomization. The three assumptions were: (1) the genetic variant must be robustly associated with the exposure; (2) the genetic variant should not be associated with confounders of the exposure—outcome association; and (3) the genetic variant must influence the outcome through the exposure only and not through any direct or alternative pathways. The dashed lines represent pathways that violate the assumptions. CHD, coronary heart disease.

additional imputation for single nucleotide polymorphism (SNP). We also collected published GWAS associations that comprise only the significant hits of a GWAS after applying stringent p-value thresholds (eg.  $p < 5 \times 10^{-8}$ , a conventional threshold for declaring statistical significance in GWAS), using the clumping algorithm (r<sup>2</sup> threshold = 0.05 and window size = 1 Mb). Data included in this study were the GWAS summary statistics datasets from the C4D (https://www.ncbi.nlm.nih.gov/pubmed/21378988) for CHD; Neale Lab UKB-a:13 Consortium for sleeplessness; Neale Lab UKB-a:9 Consortium for sleep duration and Neale Lab UKB-a:15 Consortium for daytime dozing (https://www.ukbiobank.ac.uk). UK Biobank participants self-reported sleeplessness symptoms in response to the question 'Do you have trouble falling asleep at night, or do you wake up in the middle of the night?'. As for sleep duration, it was provided as self-reported 'sleep duration', in which individuals were asked to provide the average number of hours slept in a 24-h period. Daytime dozing was investigated using the Epworth scale. This scale consisted of eight questions that could be scored from 0 to 3 and assessed sleepiness during different daytime situations. The final score varies from 0 to 24. A final score >10 indicated daytime dozing. Details of studies and datasets used for analyses were presented in Table 1.

## 2.2. Data extraction and harmonization

The summary-level GWAS data for the diseases were computed from two independent community-based studies with individual-level SNP genotypes. We extracted the following data for each genetic instrument for traits from GWAS of the following outcomes: the effect allele (EA), effect allele frequency (EAF), Beta value, standard error (SE), SNP and p-value. We also requested the following metrics of SNP genotype quality from disease and risk factor studies: strong evidence of between-study heterogeneity in the SNP-trait association ( $p \leq 0.001$ ), Hardy—Weinberg

disequilibrium ( $p \le 0.001$ ) or imputation quality metric (info or  $r^2$ )  $\le 0.90$ . We harmonized the summary data for diseases and risk factors so that the EA reflected the allele associated with exposure. When SNPs were palindromic, ie A/T or G/C, we used the information on allele frequency to resolve strand ambiguity. We excluded SNP-trait associations from the GWAS catalog if they were missing a p-value, Beta or a SE for the Beta.

### 2.3. Two-sample MR and causal effect assessment

We performed MR in a strategy known as two-sample MR using results from GWAS [5]. Here, the SNP-exposure effects and the SNP-outcome effects were obtained from separate studies. With the summary data alone, it was possible to estimate the causal influence of the exposure on the outcome.

We explored the associations in the following scenarios [6]. (1) Causal associations between sleeplessness and CHD: causal associations between sleep duration and CHD: causal associations between daytime dozing and CHD. The conventional MR approach inverse variance weighted (IVW) method and Egger method were used. The causal relationship was rigorous in this study, as it was identified only when the observed association passed both IVW method and Egger method. Characteristics of the SNPs associated with sleep (sleeplessness, sleep duration, and daytime dozing) and their associations with CHD were shown in Table 2. (2) Heterogeneity: heterogeneity is the variability in the causal estimates obtained for each SNP (ie, how consistent is the causal estimate across all SNPs; low heterogeneity suggests increased reliability of MR estimates). It was calculated using each of the different MR methods where possible. (3) Horizontal pleiotropy: this refers to when a genetic variant associated with traits on discrete pathways that are also causal in disease [7]. Unbalanced horizontal pleiotropy can be formally assessed by MR-Egger method, which provides a valid MR estimate that takes into account the presence of unbalanced horizontal pleiotropy [8]. This was evaluated by p-value of the MR-Egger intercept.

#### 2.4. IRB exemption

This research did not involve human or animal experiments.

### 2.5. Statistical analysis

To make the data suitable for MR, we converted odds ratios (ORs) to log ORs and inferred SEs from reported 95% confidence intervals (CIs) or (if the latter were unavailable) from the reported *p*-value using the Z-distribution. For binary traits, the beta corresponded to the log OR per copy of the EA. For quantitative traits, the beta corresponded to the standard deviation (SD) change in the trait per copy of the EA.

<span id="page-1-1"></span>**Table 1**Details of studies and datasets used for analyses.

| Exposure/outcomes      |        | Number of controls |         | Web source                                                                              | First<br>author | Consortium | Year | Units    | Population studied             |
|------------------------|--------|--------------------|---------|-----------------------------------------------------------------------------------------|-----------------|------------|------|----------|--------------------------------|
| Sleeplessness          | N/A    | N/A                | 336,965 | http://www.nealelab.is/blog/2017/9/11/details-and-considerations-of-the-uk-biobank-gwas | Neale           | Neale Lab  | 2017 | N/A      | European, males<br>and females |
| Sleep duration         | N/A    | N/A                | 335,410 | http://www.nealelab.is/blog/2017/9/11/details-and-considerations-of-the-uk-biobank-gwas | Neale           | Neale Lab  | 2017 | N/A      | European, males and females    |
| Daytime dozing         | N/A    | N/A                | 336,082 | http://www.nealelab.is/blog/2017/9/11/details-and-considerations-of-the-uk-biobank-gwas | Neale           | Neale Lab  | 2017 | N/A      | European, males and females    |
| Coronary heart disease | 15,420 | 15,062             | 30,482  | https://www.ncbi.nlm.nih.gov/pubmed/21378988                                            | Peden           | C4D        | 2011 | log odds | Mixed, males and females       |

CHD, coronary heart disease; N/A, not available.

<span id="page-2-0"></span>
 Table 2

 Characteristics of the single-nucleotide polymorphisms associated with sleep and their associations with coronary heart disease.

| SNP                    | EA       | EAF            | Associations with sleeplessness  |                |                      | Associations with CHD |                |                |  |
|------------------------|----------|----------------|----------------------------------|----------------|----------------------|-----------------------|----------------|----------------|--|
|                        |          |                | Beta                             | SE             | р                    | Beta                  | SE             | р              |  |
| rs10156602             | G        | 0.364          | -0.010                           | 0.002          | 2.32E-08             | 0.024                 | 0.019          | 0.200          |  |
| rs11152363             | Α        | 0.185          | 0.014                            | 0.002          | 2.54E-10             | 0.021                 | 0.023          | 0.355          |  |
| rs11635495             | С        | 0.514          | 0.010                            | 0.002          | 2.34E-08             | 0.016                 | 0.017          | 0.360          |  |
| rs17879819             | T        | 0.076          | -0.019                           | 0.003          | 9.83E-09             | -0.101                | 0.025          | 3.71E-0        |  |
| rs2132083              | С        | 0.660          | -0.010                           | 0.002          | 4.04E-08             | -0.021                | 0.020          | 0.289          |  |
| rs224071               | A        | 0.550          | 0.010                            | 0.002          | 2.67E-08             | 0.014                 | 0.017          | 0.424          |  |
| rs2956278              | G        | 0.214          | 0.012                            | 0.002          | 2.03E-08             | 0.006                 | 0.021          | 0.771          |  |
| rs324017               | Č        | 0.705          | -0.012                           | 0.002          | 8.83E-10             | 0.015                 | 0.019          | 0.428          |  |
| rs3817576              | G        | 0.525          | -0.010                           | 0.002          | 2.81E-09             | -0.003                | 0.017          | 0.852          |  |
| rs4688760              | T        | 0.692          | 0.012                            | 0.002          | 1.06E-09             | 0.012                 | 0.021          | 0.553          |  |
| rs4943439              | T        | 0.387          | 0.010                            | 0.002          | 4.75E-09             | 0.017                 | 0.017          | 0.322          |  |
| rs71373536             | A        | 0.253          | 0.013                            | 0.002          | 1.92E-11             | 0.017                 | 0.019          | 0.490          |  |
| rs9815484              | G        | 0.233          | 0.013                            | 0.002          | 5.64E-09             | 0.029                 | 0.013          | 0.450          |  |
| SNP                    |          |                | Associations with sleep duration |                |                      | Associations with CHD |                |                |  |
| 5111                   | EA       | EAF            | Beta SE p                        |                | Beta SE p            |                       |                |                |  |
| rs10496079             | C        | 0.629          | 0.015                            | 0.002          | 1.44E-14             | -0.018                | 0.017          | 0.294          |  |
| rs10510128             | A        | 0.206          | 0.013                            | 0.002          | 9.17E-10             | -0.018<br>-0.002      | 0.017          | 0.294          |  |
| rs10973207             | T        | 0.159          | 0.014                            | 0.002          | 2.87E-08             | 0.012                 | 0.023          | 0.531          |  |
|                        | C        | 0.139          |                                  | 0.003          | 2.79E-08             | 0.012                 | 0.023          | 0.013          |  |
| rs113021516            |          |                | 0.011                            |                |                      |                       |                |                |  |
| rs11621908             | T        | 0.082          | -0.019                           | 0.003          | 3.23E-08             | -0.028                | 0.033          | 0.401          |  |
| rs11650677             | A        | 0.338          | 0.012                            | 0.002          | 5.85E-09             | 0.004                 | 0.018          | 0.813          |  |
| rs11982852             | T        | 0.245          | -0.013                           | 0.002          | 1.43E-09             | 0.027                 | 0.019          | 0.154          |  |
| rs12501164             | C        | 0.497          | 0.011                            | 0.002          | 2.05E-08             | -0.034                | 0.017          | 0.046          |  |
| rs12567114             | Α        | 0.275          | 0.013                            | 0.002          | 2.71E-09             | -0.020                | 0.018          | 0.263          |  |
| rs13107325             | T        | 0.075          | -0.022                           | 0.004          | 9.34E-10             | -0.084                | 0.046          | 0.065          |  |
| rs1570203              | Α        | 0.525          | -0.012                           | 0.002          | 1.90E-10             | 0.028                 | 0.017          | 0.096          |  |
| rs17822558             | Α        | 0.323          | -0.011                           | 0.002          | 2.51E-08             | 0.004                 | 0.017          | 0.829          |  |
| rs180769               | С        | 0.576          | -0.011                           | 0.002          | 7.49E-09             | 0.017                 | 0.018          | 0.340          |  |
| rs28375265             | T        | 0.348          | -0.011                           | 0.002          | 4.15E-08             | 0.011                 | 0.018          | 0.526          |  |
| rs37021                | G        | 0.443          | -0.011                           | 0.002          | 2.86E-08             | 0.022                 | 0.021          | 0.277          |  |
| rs374153               | T        | 0.841          | -0.015                           | 0.003          | 9.35E-09             | 0.036                 | 0.026          | 0.168          |  |
| rs448231               | Α        | 0.444          | 0.011                            | 0.002          | 1.62E-09             | 0.006                 | 0.017          | 0.729          |  |
| rs4588900              | Α        | 0.517          | -0.010                           | 0.002          | 2.84E-08             | 0.003                 | 0.017          | 0.870          |  |
| rs4642942              | G        | 0.586          | -0.012                           | 0.002          | 2.67E-10             | -0.013                | 0.018          | 0.487          |  |
| rs4730640              | C        | 0.616          | -0.013                           | 0.002          | 1.69E-11             | 0.015                 | 0.018          | 0.401          |  |
| rs4897409              | A        | 0.305          | -0.011                           | 0.002          | 4.50E-08             | 0.002                 | 0.018          | 0.896          |  |
| rs61916239             | G        | 0.350          | 0.011                            | 0.002          | 4.26E-08             | 0.011                 | 0.018          | 0.541          |  |
| rs6889592              | A        | 0.335          | 0.011                            | 0.002          | 3.23E-08             | -0.024                | 0.019          | 0.211          |  |
| rs7016314              | C        | 0.657          | 0.011                            | 0.002          | 1.22E-08             | -0.029                | 0.023          | 0.211          |  |
| rs7764984              | G        | 0.327          | -0.013                           | 0.002          | 8.84E-11             | 0.012                 | 0.023          | 0.522          |  |
| rs8029928              | T        | 0.239          | -0.013<br>-0.014                 | 0.002          |                      | 0.012                 | 0.020          | 0.322          |  |
|                        |          |                |                                  |                | 2.58E-10             |                       |                |                |  |
| rs915416               | G        | 0.710          | -0.012                           | 0.002          | 2.53E-08             | 0.016                 | 0.018          | 0.378          |  |
| rs925872               | G        | 0.455          | -0.011                           | 0.002          | 1.46E-09             | -0.022                | 0.018          | 0.210          |  |
| rs9810474<br>rs9895274 | T<br>T   | 0.233<br>0.488 | -0.013<br>-0.010                 | 0.002<br>0.002 | 8.74E-09<br>3.87E-08 | 0.017<br>0.028        | 0.018<br>0.019 | 0.358<br>0.130 |  |
| SNP                    | <u> </u> |                | Associations with daytime dozing |                |                      | Associations with CHD |                |                |  |
|                        | EA       | EAF            | Beta SE p                        |                |                      | Beta                  | SE p           |                |  |
| rs10900858             | G        | 0.527          | -0.007                           | 0.001          | 3.18E-08             | 0.005                 | 0.017          | 0.789          |  |
| rs13023284             | C        | 0.604          | -0.007<br>-0.008                 | 0.001          | 4.15E-11             | -0.037                | 0.017          | 0.789          |  |
|                        |          |                |                                  |                |                      |                       |                |                |  |
| rs13284688             | C        | 0.206          | 0.010                            | 0.001          | 4.75E-12             | -0.033                | 0.023          | 0.152          |  |
| rs1846644              | C        | 0.411          | 0.011                            | 0.001          | 1.96E-18             | -0.009                | 0.017          | 0.599          |  |
| rs285793               | A        | 0.538          | -0.007                           | 0.001          | 6.33E-09             | -0.001                | 0.017          | 0.974          |  |
| rs35284403             | C        | 0.350          | 0.007                            | 0.001          | 8.83E-09             | 0.021                 | 0.017          | 0.236          |  |
| rs4242242              | A        | 0.419          | -0.007                           | 0.001          | 2.01E-09             | -0.019                | 0.017          | 0.252          |  |
| rs553314               | C        | 0.634          | -0.007                           | 0.001          | 3.70E-09             | 0.021                 | 0.018          | 0.233          |  |
| rs614987               | C        | 0.615          | 0.007                            | 0.001          | 2.71E-08             | 0.012                 | 0.017          | 0.476          |  |
| rs780093               | С        | 0.619          | -0.008                           | 0.001          | 8.62E-11             | 0.012                 | 0.021          | 0.572          |  |

CHD, coronary heart disease; EA, effect allele; EAF, effect allele frequency; SE, standard error; SNP, single-nucleotide polymorphism.

Bonferroni corrections were used to make allowance for multiple testing, although this was likely to be overly conservative given the non-independence of many of the exposures tested (as there were three aspects of sleep, including sleeplessness, sleep duration and daytime dozing, 0.05/3 = 0.017. p- Values were two sided, and evidence of causal association was declared at p < 0.017). All analyses were performed in R 3.2.4 (http://www.r-project.org), and Stata release 13.1 (StataCorp LP).

## 3. Results

The IVW method estimate indicated that the OR (95% CI) for CHD was 3.924 (1.345–11.447) per standard deviation increase in sleep-lessness (p=0.012). Results were consistent in MR–Egger method (OR, 4.654; 95% CI, 1.191–18.186; p=0.009) (Fig. 2, Table 3). Test for heterogeneity indicated that there was no heterogeneity amongst these 13 SNPs in the causal effect between sleeplessness and CHD.

<span id="page-3-0"></span>Fig. 2. Mendelian randomization study of the effect of sleeplessness, sleep duration, and daytime dozing on coronary heart disease (CHD). Mendelian randomization (MR) estimate for sleeplessness, sleep duration, and daytime dozing on CHD (log odds per standard deviation (SD)). Each black point represents the log odds ratio (OR) for CHD per change in sleeplessness, sleep duration and daytime dozing, produced using each of the SNPs as separate instruments, and red points showing the combined causal estimate using all single nucleotide polymorphisms (SNPs) together in a single instrument. Horizontal lines denote 95% confidence intervals (CIs). (For interpretation of the references to color in this figure

There was a little evidence of directional horizontal pleiotropy in the MR–Egger regression (-0.077 (SE =0.029), p=0.023) (Fig. 2, Table 3). Our two-sample MR analysis provided evidence supporting that the genetically predicted sleeplessness was positively casually associated with CHD.

legend, the reader is referred to the Web version of this article.)

As for sleep duration, our two-sample MR analysis did not support the causal relationship between it and CHD. Similar results were found between daytime dozing and CHD (Fig. 2, Table 3). Thus, there was a causal relationship between sleeplessness (not sleep duration or daytime dozing) and CHD.

#### 4. Discussion

From our major findings, we have identified that the genetically predicted sleeplessness is positively causally associated with CHD. The causal association between sleep duration (or daytime dozing) and CHD is not established.

Currently, there is no gold standard MR analysis method. Available methods have advantages and limitations that balance precision and adjustment for bias. In the present study, two MR approaches (MR–Egger, and IVW methods) were applied to evaluate the robustness of the causal association between sleep and

CHD. In this way, we had more powder to identify the true associations between sleep and CHD.

Sleep (which accounts for almost one-third of human's life) is one of the most important factors contributing to health. Sleeplessness (also named as insomnia) is the most prevalent sleep disorder all over the world [9] and is highly comorbid with a number of cardiovascular diseases [10]. In the last decade, there is increasing evidence associating sleeplessness with hypertension [11], CHD [12], heart failure [13], as well as subclinical cardiovascular disease [14] and cardiovascular disease mortality [15]. Due to the wide variation in how sleeplessness is defined and measured, there are conflicting data and caution must be exercised when comparing studies and interpreting results. Nonetheless, the existing data suggest that sleeplessness is an important risk factor for CHD [16,17]. In our study, both the IVW method and the MR-Egger method supported that the genetically predicted sleeplessness was positively casually associated with CHD, which was consistent with the previous studies.

There are several plausible mechanisms whereby sleeplessness may positively affect the risk of CHD including dysregulation of the hypothalamic—pituitary axis [18,19], abnormal modulations of the autonomic nervous system and increased sympathetic nervous system activity [20], increased systemic inflammation [21], and

<span id="page-3-1"></span>**Table 3**Causal associations between genetically determined sleep and coronary heart disease (CHD).

| Sleep                     | Method                                              | Causal estimate |                         |                |       |  |  |
|---------------------------|-----------------------------------------------------|-----------------|-------------------------|----------------|-------|--|--|
|                           |                                                     | SNP             | OR                      | 95% (CI)       | p     |  |  |
| Sleeplessness             | MR Egger                                            | 13              | 4.654                   | (1.191–18.186) | 0.009 |  |  |
|                           | Inverse variance weighted                           | 13              | 3.924                   | (1.345-11.447) | 0.012 |  |  |
| Test for heterogeneity: 1 | p = 0.468 (MR-Egger) and $p = 0.133$ (IVW)          |                 |                         |                |       |  |  |
| Test for horizontal pleio | tropy: MR-Egger intercept = $-0.077$ , SE = $0.02$  | 29, p = 0.023   |                         |                |       |  |  |
| Sleep duration            | MR-Egger                                            | 28              | 28 9.758 (0.160-592.894 |                | 0.286 |  |  |
|                           | Inverse variance weighted                           | 28              | 0.451                   | (0.252-0.806)  | 0.007 |  |  |
| Test for heterogeneity: 1 | p = 0.555 (MR-Egger) and $p = 0.487$ (IVW)          |                 |                         |                |       |  |  |
| Test for horizontal pleio | tropy: MR-Egger intercept = $-0.038$ , SE = $0.02$  | 25, p = 0.150   |                         |                |       |  |  |
| Daytime dozing            | MR-Egger                                            | 10              | 10 0.004 (0.000-41.457) |                | 0.278 |  |  |
|                           | Inverse variance weighted                           | 10              | 1.188                   | (0.250-5.634)  | 0.827 |  |  |
| Test for heterogeneity: 1 | p = 0.317  (MR-Egger)  and  p = 0.274  (IVW)        |                 |                         |                |       |  |  |
| Test for horizontal pleio | tropy: MR-Egger intercept = $0.045$ , SE = $0.03$ ? | 7, $p = 0.259$  |                         |                |       |  |  |

abnormal lipid metabolites [\[22\]](#page-4-19). Moreover, sleeplessness is associated with impaired glucose metabolism which may also serve as a mediator on the pathway to CHD.

Although a causal relationship between short sleep duration and cardiovascular risk is not confirmed, most of the data indicate a strong link between short sleep times and diabetes mellitus, obesity, and cardiovascular disorders. Dominguez et al. [\[2\]](#page-4-1) reported that lower sleeping times (<6 h) was independently associated with an increased risk of subclinical multi-territory atherosclerosis. The association between long sleep duration and CHD risk was debated. On the one hand, healthy middle-aged men with long sleep duration (>8 h) were at increased risk of atherosclerosis. On the other hand, it was also reported that no such association had been found with long sleep durations [\[2\]](#page-4-1). In our findings, our twosample MR analysis did not support the causal relationship between sleep duration and CHD. We assumed that it might due to the different definitions and measuring methods used in different research. Furthermore, in this study, the causal relationship was identified only when the observed association passed both the IVW method and the Egger method. Thus, the causal relationship was rigorous and conservative.

This study had some limitations. First, a major limitation was the use of self-reported complaints and lack of objective or standardized measurements. The data included in this study about sleep (sleeplessness, sleep duration, and daytime dozing) were based on self-reported answers, and some of the questions could be differently interpreted by different people. Objective or standardized methods to assess sleep complaints are recommended for future studies. Second, if the exposure was a composite trait that comprises multiple sub-phenotypes, we can not rule out the possibility that the effect of exposure on disease was driven by one of the subphenotypes. Therefore, the causative associations identified in this study are not definitive and need to be confirmed by follow-up RCTs in the future. Last but not least, our study assumed a linear shape of the association between traits and CHD for the limited information from GWAS summary data, whereas the shape could be J- or Ushaped.

## 5. Conclusions

In summary, our analysis provided evidence supporting a causal relationship between sleeplessness (not sleep duration or daytime dozing) and CHD. Further large-scale studies or longitudinal studies are required to validate these findings.
