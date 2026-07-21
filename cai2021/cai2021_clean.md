# Gene

# Causal links between major depressive disorder and insomnia: A Mendelian randomisation study

Lei Cai <sup>a,1</sup>, Yiran Bao <sup>a,1</sup>, Xiaoqian Fu <sup>b,1</sup>, Hongbao Cao <sup>c</sup>, Ancha Baranova <sup>c,d</sup>, Xiangrong Zhang <sup>e</sup>, Jing Sun<sup>f</sup>, Fuquan Zhang<sup>e,f,\*</sup>

- a Bio-X Institutes, Key Laboratory for the Genetics of Developmental and Neuropsychiatric Disorders (Ministry of Education), Collaborative Innovation Center for Genetics and Development, Shanghai Key Laboratory of Psychotic Disorders (13dz2260500), Shanghai Jiaotong University, Shanghai 200240, China
- f Department of Psychiatry, The Affiliated Brain Hospital of Nanjing Medical University, Nanjing 210029, China

# Keywords:

Major depressive disorder Insomnia LD score regression Mendelian randomization

## Abstract

Both Major depressive disorder (MDD) and insomnia are two common mental disorders. However, the inherent and comprehensive genetic factors causing the links between MDD and insomnia are unclear yet. Here, based on GWAS results for each disorder, we used linkage disequilibrium (LD) score regression analysis and a multi-single nucleotide polymorphism (SNP) Mendelian randomization (MR) analysis to test the genetic relationships between these two diseases. Genetic correlation analyses indicated that MDD has a significant genetic correlation with insomnia (correlation ratio = 0.40  $\pm$  0.03, P =  $1.12 \times 10^{-52}$ ). Mendelian randomization analysis indicated that liability to MDD confers a causal effect on insomnia (b<sub>xy</sub> =  $0.16 \pm 0.02$ , P =  $1.11 \times 10^{-18}$ ), while liability to insomnia confers a causal effect on MDD (b<sub>xy</sub> = 0.57  $\pm$  0.07, P = 1.17  $\times$  10<sup>-14</sup>). We found that the transcription factor 4 (TCF4) gene may contribute to the mutual influences between MDD and insomnia. These results provide insights into the relationships between MDD and insomnia and may have implications for policy, planning, and provision of services.

#### 1. Introduction

Major depressive disorder (MDD) characterized by persistent low mood is one of the most prevalent psychiatric illness worldwide. The estimated lifetime prevalence is appropriately 17% (Blazer et al., 1994). Affected individuals have the high risk of suicide and worse medical problems than the healthy population, and thus, MDD causes massive societal burden. The core symptoms of MDD include sleep disturbances (Tsuno et al., 2005). Insomnia is another common mental disorder affecting nearly 10% of population worldwide (Bhaskar et al., 2016). Nowadays, it is widely accepted that insomnia and MDD have bidirectional relationships, i.e. insomnia can trigger depression and anxiety disorders while most people with MDD have trouble in sleeping (Franzen and Buysse, 2008). Although MDD and insomnia appear to be independent, these two disorders co-occur more than by chance. Among the subjective sleep complaints from MDD patients, insomnia is the most common (up to 88%) (Yates et al., 2004).

There are several studies to explore the factors contributing the comorbidity between insomnia and MDD (Pigeon, 2009; Lopresti et al., 2013). Sleep improvement has been found to enhance the patients' antidepressant response, while in clinical trials of antidepressant medication, nearly half of depression remitters had residual insomnia

E-mail addresses: jingsun2007@163.com (J. Sun), zhangfq@njmu.edu.cn (F. Zhang).

Abbreviations: MDD, Major depressive disorder; LD, Linkage disequilibrium; SNP, multi-single nucleotide polymorphism; TCF4, The transcription factor 4; MR, Mendelian randomization; SMR, Summary data-based MR; GSMR, Generalized SMR; GWAS, Genome wide association analysis; MAF, Minor allele frequency; MHC, Major histocompatibility complex; UKB, The UK Biobank; SZ, schizophrenia; CHR, chromosome.

<sup>\*</sup> Corresponding author at: Department of Psychiatry, The Affiliated Brain Hospital of Nanjing Medical University, 264 Guangzhou Road, Nanjing 210029, China; Department of Psychiatry, The Affiliated Brain Hospital of Nanjing Medical University, Nanjing 210029, China; Department of Psychiatry, The Affiliated Brain Hospital of Nanjing Medical University, Nanjing 210029, China.

 $<sup>^{1}</sup>$  Contribute equally to the study.

([Romera et al., 2013\)](#page-4-0). Life stressors are widely believed to initiate sleep disturbance, which can persist and become a chronic disorder. And at this stage, the produced neuroendocrine imbalances, such as: serotonergic and dopaminergic molecules, may induce series of symptoms shared by both insomnia and depression ([Lopresti et al., 2013](#page-4-0)). Besides this, there are several other possible mechanisms for the co-occurrence of insomnia and MDD [\(Pigeon, 2009\)](#page-4-0). However, the inherent genetic factors causing the links between MDD and insomnia are unclear yet.

Here, in order to trace genetic relationship between MDD and insomnia, LD score regression analysis was performed to evaluate their genetic correlation, and then based on GWAS results for each disorder, a multi-single nucleotide polymorphism (SNP) Mendelian randomization (MR) analysis was performed to test the causal relationships between these two diseases through using the GSMR [\(Zhu et al., 2018](#page-4-0)).

#### **2. Materials and methods**

#### *2.1. Data collection and extraction*

The MDD genome-wide association (GWA) study data were obtained according to a genome-wide association (GWA) meta-analysis conducted by the Major Depressive Disorder working group of the Psychiatric Genomics Consortium (PGC) ([Wray et al., 2018\)](#page-4-0). Totally, 480,359 European-ancestry subjects were collected, including 135,458 cases and 344,901 controls, from seven comparable cohorts, i.e., PGC29 ([Major](#page-4-0)  [Depressive Disorder Working Group of the Psychiatric et al., 2013](#page-4-0)), GERA [\(Banda et al., 2015\)](#page-3-0), iPSYCH ([Pedersen et al., 2018\)](#page-4-0), decode ([Major Depressive Disorder Working Group of the Psychiatric et al.,](#page-4-0)  [2013\)](#page-4-0), GenScotland ([Smith et al., 2013\)](#page-4-0), UK Biobank (UKB) [\(Allen et al.,](#page-3-0)  [2014\)](#page-3-0), and 23andMe ([Hyde et al., 2016](#page-3-0)). The diagnosis of major depressive disorder was ascertained to meet international consensus criteria, i.e., the Diagnostic and Statistical Manual of Mental Disorders-V (DSM-V), the International Classification of Diseases (ICD)-9 or − 10 using either of structured diagnostic interviews, review of electronic medical records and self-reported symptoms or treatment by a medical professional and to exclude cases with lifetime bipolar disorder or schizophrenia. While the insomnia GWA study data from UKB contained 386,533 European-ancestry subjects, including 109,402 cases and 277,131 controls ([Jansen et al., 2019](#page-3-0)). The insomnia complaints were assessed by a question via a touch screen device, which is much closer to the DSM-5 and the International Classification of Sleeping Diseases (ICSD) diagnostic criteria than Insomnia Severity Index [\(Bastien et al.,](#page-3-0)  [2001\)](#page-3-0). Detailed description of subjects' characters can be checked in each study. Ethical approval had been obtained in all original studies.

Genotyping was performed on genome DNA extracted from blood samples and completed on precast or custom genotyping arrays provided by Affymetrix or Illumina, etc. Detailed genotyping procedures can be found in the primary reports. The quality control, and imputation analysis were performed using the PGC standard pipeline or comparable procedures [\(Schizophrenia Working Group of the Psychiatric Genomics,](#page-4-0)  [2014\)](#page-4-0). The 1000 Genomes project reference panel was used to perform genotype imputation in IMPUTE2 [\(Howie et al., 2009](#page-3-0)). For either dataset of MDD and Insomnia, all bi-allelic SNPs and imputation score (INFO score) above 0.9 were included, and ambiguous SNPs were excluded. If an SNP was mapped to opposite strands in either dataset, its alleles in the second dataset were flipped. Finally, 9.6 million for MDD and 10.8 million SNPs for Insomnia were collected.

#### *2.2. Genetic correlation and MR analyses*

GWAS summary results were utilized to analyze the genetic correlation of MDD with insomnia using linkage disequilibrium (LD) score regression software (LDSC, v1.0.1) ([Bulik-Sullivan et al., 2015a, 2015b](#page-3-0)). The 1000 Genome project phase 3 [\(Genomes Project et al., 2015](#page-3-0)) were used to estimate the LD structure for European populations, which was obtained from the LD score regression website ([Bulik-Sullivan et al.,](#page-3-0)  [2015a, 2015b; Finucane et al., 2015\)](#page-3-0). Furthermore, those SNPs obtained above were filtered into 1.1 million variants with minor allele frequency (MAF) above 0.05 and with Major histocompatibility complex (MHC) and other long-range LD regions excluded [\(Altshuler et al., 2010](#page-3-0)).

Mendelian randomization (MR) is an analysis that uses genetic variants, which are expected to be independent of confounding factors, as instrumental variables to test for causality ([Zhu et al., 2018\)](#page-4-0). MR can be used to infer credible causal associations or as a strategy to rank order candidate causal associations. The power of an MR analysis could be greatly improved by exploiting GWAS summary data from two independent studies with large sample sizes, i.e., a summary data-based MR (SMR) approach. Here, the SMR approach is extended to a more general form (generalized SMR or GSMR) by leveraging power from multiple genetic variants accounting for linkage disequilibrium (LD) between the variants, which is more powerful than existing summary data-based MR methods ([Zhu et al., 2018\)](#page-4-0). This method utilizes summary-level data to test for putative causal associations between a risk factor (exposure) and an outcome by using independent genomewide significant SNPs as instrumental variables as an index of the exposure. Instrumental variants were selected based on default P ≤ 5 × 10<sup>−</sup> <sup>8</sup> . HEIDI outlier detection was used to filter genetic instruments that showed clear pleiotropic effects on the exposure phenotype and the outcome phenotype. We used a threshold P value of 0.01 for the outlier detection analysis in HEIDI, which removes 1% of SNPs by chance if there is no pleiotropic effect.

#### **3. Results and discussion**

Genetic correlation analyses indicated that MDD has a significant genetic correlation with insomnia (correlation ratio = 0.40 ± 0.03, P = 1.12 × 10<sup>−</sup> 52). MR analysis indicated that genetic liabilities to MDD and to insomnia are mutually causal: MDD confers a causal effect on insomnia with 45 independent instrumental variants being involved (bxy = 0.16 ± 0.02, P = 1.11 × 10<sup>−</sup> 18, Fig. 1A), and insomnia confers a causal effect on MDD with 15 independent instrumental variants being involved (bxy = 0.57 ± 0.07, P = 1.17 × 10<sup>−</sup> 14, Fig. 1B).

We detected a moderate genetic correlation between MDD and insomnia, suggesting shared genetic liability between the two disorders. We further revealed bidirectional causal effects between MDD and insomnia, consistent with the observation that the comorbidity between depression and insomnia typically forms a vicious cycle, known to significantly impact the course and management of one another. In clinical practice, when co-occurring with MDD, insomnia is viewed as a symptom secondary to MDD. Our results indicated that insomnia exerts a much larger causal effect on MDD than *vice versa*, supporting the independent role of genetic liability of insomnia in etiology of MDD, reminiscent of the notion of using sleep interventions as therapies for neurodegenerative and psychiatric disorders ([Akers et al., 2018](#page-3-0)).

The SNPs and genes contributing to the causal effect of insomnia on depression and depression on insomnia are listed in [Tables 1 and 2](#page-2-0). For the causal effect of insomnia on depression, the instrumental variants in depression were mapped to 30 genes, including 10 non-coding genes

**Fig. 1.** The causal effects between major depressive disorder and insomnia. A. Causal effect of major depressive disorder on insomnia. B. Causal effect of insomnia on major depressive disorder. The dot lines denote effect sizes (bxy).

<span id="page-2-0"></span>*Gene 768 (2021) 145271 L. Cai et al.* 

**Table 1**  Instrumental variants mediating causal effect of MDD on insomnia.

| SNP        | CHR | Base position | A1 | A2 | Gene name     | Gene ID     |
|------------|-----|---------------|----|----|---------------|-------------|
| rs10141157 | 14  | 104,018,105   | T  | C  | NA            | NA          |
| rs17727765 | 17  | 27,576,962    | C  | T  | CRYBA1        | 1411        |
| rs2327715  | 9   | 2,975,170     | T  | C  | CARM1P1       | 100,130,873 |
| rs7305875  | 12  | 23,971,243    | T  | A  | SOX5          | 6660        |
| rs11561993 | 7   | 109,102,855   | T  | C  | NA            | NA          |
| rs12080622 | 1   | 80,792,881    | T  | C  | NA            | NA          |
| rs1806153  | 11  | 31,850,105    | T  | G  | DKFZP686K1684 | 440,034     |
| rs10946918 | 6   | 27,380,993    | G  | A  | ZNF184        | 7738        |
| rs3132556  | 6   | 31,078,809    | T  | A  | C6ORF15       | 29,113      |
| rs4348675  | 1   | 72,515,717    | C  | T  | NEGR1         | 257,194     |
| rs10889958 | 1   | 72,956,535    | A  | T  | LOC105378797  | 105,378,797 |
| rs1923236  | 1   | 73,853,826    | T  | C  | NA            | NA          |
| rs419789   | 13  | 44,284,550    | A  | G  | ENOX1         | 55,068      |
| rs7430565  | 3   | 158,107,180   | G  | A  | RSRC1         | 51,319      |
| rs7029033  | 9   | 126,682,068   | T  | C  | DENND1A       | 57,706      |
| rs13058113 | 22  | 41,508,414    | T  | G  | EP300         | 2033        |
|            |     |               |    |    |               |             |
| rs16853930 | 4   | 42,050,818    | A  | G  | SLC30A9       | 10,463      |
| rs2451500  | 10  | 106,632,877   | C  | T  | SORCS3        | 22,986      |
| rs79883993 | 10  | 106,526,120   | A  | G  | SORCS3        | 22,986      |
| rs1152582  | 14  | 64,692,630    | G  | C  | SYNE2         | 23,224      |
| rs7200826  | 16  | 13,066,833    | T  | C  | SHISA9        | 729,993     |
| rs10464007 | 5   | 103,831,500   | A  | T  | NA            | NA          |
| rs57196886 | 2   | 157,117,768   | G  | A  | NA            | NA          |
| rs2418449  | 9   | 119,731,359   | C  | T  | ASTN2         | 23,245      |
| rs301799   | 1   | 8,489,302     | C  | T  | RERE          | 473         |
| rs2226195  | 13  | 53,628,524    | G  | A  | NA            | NA          |
| rs9427672  | 1   | 197,754,741   | A  | G  | NA            | NA          |
| rs4904738  | 14  | 42,179,732    | C  | T  | LRFN5         | 145,581     |
| rs7152906  | 14  | 75,125,540    | T  | C  | LOC100419503  | 100,419,503 |
| rs7193263  | 16  | 6,315,880     | G  | A  | RBFOX1        | 54,715      |
| rs11077204 | 16  | 7,667,187     | C  | G  | RBFOX1        | 54,715      |
| rs614443   | 15  | 37,683,804    | A  | G  | LOC105370772  | 105,370,772 |
| rs62099069 | 18  | 36,883,737    | A  | T  | LINC00669     | 647,946     |
| rs1549212  | 5   | 166,996,722   | C  | T  | TENM2         | 57,451      |
| rs6896348  | 5   | 164,477,151   | C  | G  | LOC105377703  | 105,377,703 |
| rs35267052 | 5   | 87,949,118    | G  | T  | LINC00461     | 645,323     |
| rs71639113 | 5   | 87,775,557    | T  | C  | NA            | NA          |
| rs7201225  | 16  | 72,210,050    | T  | C  | NA            | NA          |
| rs4836130  | 5   | 124,281,957   | T  | A  | NA            | NA          |
| rs13011472 | 2   | 57,961,602    | G  | C  | NA            | NA          |
| rs11663393 | 18  | 50,614,732    | A  | G  | DCC           | 1630        |
| rs12967143 | 18  | 53,099,012    | G  | C  | TCF4          | 6925        |
| rs4356032  | 1   | 90,796,112    | C  | A  | NA            | NA          |
| rs76485002 | 2   | 127,342,267   | G  | A  | LOC105373602  | 105,373,602 |
| rs1304172  | 9   | 11,402,081    | C  | T  | LOC105375974  | 105,375,974 |

**Table 2**  Instrumental variants mediating causal effect of insomnia on MDD.

| SNP        | CHR | Base position | A1 | A2 | Gene name    | Gene ID     |
|------------|-----|---------------|----|----|--------------|-------------|
| rs77217059 | 2   | 58,989,880    | A  | G  | LINC01122    | 400,955     |
| rs6735071  | 2   | 66,792,291    | T  | C  | MEIS1        | 4211        |
| rs55733009 | 2   | 66,976,354    | A  | G  | NA           | NA          |
| rs55683518 | 2   | 147,484,316   | T  | G  | NA           | NA          |
| rs62264771 | 3   | 117,647,197   | T  | G  | LOC107986022 | 107,986,022 |
| rs323509   | 5   | 104,082,179   | A  | C  | LOC105379109 | 105,379,109 |
| rs6917902  | 6   | 43,188,940    | T  | C  | CUL9         | 23,113      |
| rs221617   | 6   | 105,475,254   | T  | G  | LIN28B       | 389,421     |
| rs73197263 | 8   | 10,252,577    | A  | C  | MSRA         | 4482        |
| rs4073582  | 11  | 66,050,712    | A  | G  | CNIH2        | 254,263     |
| rs9576155  | 13  | 37,600,284    | A  | G  | SUPT20H      | 55,578      |
| rs1443917  | 13  | 54,029,409    | T  | C  | NA           | NA          |
| rs4884332  | 13  | 59,900,365    | A  | G  | NA           | NA          |
| rs4632173  | 17  | 43,260,783    | A  | G  | NA           | NA          |
| rs7228159  | 18  | 53,104,253    | A  | T  | TCF4         | 6925        |

(*CARM1P1, DKFZP686K1684, LOC105378797, LOC100419503, LOC105370772, LINC00669, LOC105377703, LINC00461, LOC105373602,* and *LOC105375974*) and 20 protein coding genes (*CRYBA1, SOX5, ZNF184, C6ORF15, NEGR1, ENOX1, RSRC1, DENND1A, EP300, SLC30A9, SORCS3, SYNE2, SHISA9, ASTN2, RERE,* 

*LRFN5, RBFOX1, TENM2, DCC*, and *TCF4*). The instrumental variants in insomnia were mapped to 10 genes, including three non-coding genes (*LINC01122, LOC107986022*, and *LOC105379109*) and seven protein coding genes (*MEIS1, CUL9, LIN28B, MSRA, CNIH2, SUPT20H*, and *TCF4*). And *TCF4* gene is the only gene that mediates the bidirectional

<span id="page-3-0"></span>*Gene 768 (2021) 145271 L. Cai et al.* 

causal effects between MDD and insomnia.

The close links between insomnia and MDD have long been known. However, the biological mechanism underlying the association between insomnia and MDD is poorly understood. Our study implicated a panel of genes that may contribute to the causal links between MDD and insomnia. Among these genes, we highlight the *TCF4* gene, since it contributes to the mutual influences between MDD and insomnia. The transcription factor 4 encoding gene, *TCF4*, is located on human chromosome 18, at one of the first genome-wide risk loci for schizophrenia (SZ) ([Stefansson et al., 2009](#page-4-0)). Later, this gene was implicated in MDD, insomnia, and other neurodevelopmental disorders [\(Wray et al., 2018;](#page-4-0)  [Jansen et al., 2019](#page-4-0)).

Presented study has two strengths. First, the large sample sizes for the traits involved permit powerful and robust evaluation of genetic relationships between MDD and insomnia. Second, to avoid potential population heterogeneity across the studies, we limited our analysis to individuals of European ancestry. Several limitations of this work are acknowledged. As our analysis was limited to a genetic component of each trait, presented results should be interpreted cautiously, with understanding that human traits result from a complex web of interactions among a plethora of psycho-social-environmental factors.

#### **4. Conclusions**

Our findings provide insights into the relationships between MDD and insomnia and may have implications for policy, planning, and provision of services.

#### *Role of the funder/sponsor*

The funders had no role in the design and conduct of the study; collection, management, analysis, and interpretation of the data; preparation, review, or approval of the manuscript; and decision to submit the manuscript for publication.
