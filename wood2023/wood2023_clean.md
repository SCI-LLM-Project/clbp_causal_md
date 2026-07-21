# Journal of PHYSIOTHERAPY

#### Research

# Pain catastrophising and kinesiophobia mediate pain and physical function improvements with Pilates exercise in chronic low back pain: a mediation analysis of a randomised controlled trial

Lianne Wood <sup>a,b,c</sup>, Geronimo Bejarano <sup>d</sup>, Ben Csiernik <sup>e</sup>, Gisela C Miyamoto <sup>f</sup>, Gemma Mansell <sup>g</sup>, Jill A Hayden <sup>h</sup>, Martyn Lewis <sup>b</sup>, Aidan G Cashin <sup>i,j</sup>

<sup>a</sup> Spinal Surgical Division, Nottingham University Hospitals NHS Trust, Nottingham, UK; <sup>b</sup> School of Medicine, Keele University, Newcastle-under-Lyme, UK; <sup>c</sup> Faculty of Health and Life Sciences, University of Exeter, Exeter, UK; <sup>d</sup> University of Texas Health Science Center (UTHealth), Austin, Texas, USA; <sup>e</sup> Department of Health Sciences, Ontario Tech University, Oshawa, Ontario, Canada; <sup>f</sup> Masters and Doctoral Program in Physical Therapy, Universidade Cidade de São Paulo, São Paulo, Brazil; <sup>g</sup> School of Psychology, College of Health & Life Sciences, Aston University, Aston Triangle, Birmingham, UK; <sup>h</sup> Department of Community Health and Epidemiology, Dalhousie University, Halifax, Canada; <sup>i</sup> Centre for Pain IMPACT, Neuroscience Research Australia, Sydney, Australia; <sup>j</sup> School of Health Sciences, Faculty of Medicine & Health, University of New South Wales, Sydney, Australia

#### KEY WORDS

Exercise Low back pain Mediation analysis Pilates Physical therapy

## Abstract

Question: How much are the reductions in pain intensity and improvements in physical function from Pilates exercise mediated by changes in pain catastrophising and kinesiophobia? Design: This was a secondary causal mediation analysis of a four-arm randomised controlled trial testing Pilates exercise dosage (once. twice or thrice per week) against a booklet control. Participants: Two hundred and fifty-five people with chronic low back pain. Data analysis: All analyses were conducted in R software (version 4.1.2) following a preregistered analysis plan. A directed acyclic graph was constructed to identify potential pre-treatment mediator-outcome confounders. For each mediator model, we estimated the intervention-mediator effect, the mediator-outcome effect, the total natural indirect effect (TNIE), the pure natural direct effect (PNDE), and the total effect (TE). Results: Pain catastrophising mediated the effect of Pilates exercise compared with control on the outcomes pain intensity (TNIE MD -0.21, 95% CI -0.47 to -0.03) and physical function (TNIE MD -0.64, 95% CI -1.20 to -0.18). Kinesiophobia mediated the effect of Pilates exercise compared with control on the outcomes pain intensity (TNIE MD -0.31, 95% CI -0.68 to -0.02) and physical function (TNIE MD -1.06, 95% CI –1.70 to –0.49). The proportion mediated by each mediator was moderate (21 to 55%). **Conclusion**: Reductions in pain catastrophising and kinesiophobia partially mediated the pathway to improved pain intensity and physical function when using Pilates exercise for chronic low back pain. These psychological components may be important treatment targets for clinicians and researchers to consider when prescribing exercise for chronic low back pain. [Wood L, Bejarano G, Csiernik B, Miyamoto GC, Mansell G, Hayden JA, Lewis M, Cashin AG (2023) Pain catastrophising and kinesiophobia mediate pain and physical function improvements with Pilates exercise in chronic low back pain: a mediation analysis of a randomised controlled trial. Journal of Physiotherapy 69:168-174]

#### Introduction

Chronic low back pain (CLBP) is the leading cause of impaired physical function worldwide; <sup>1,2</sup> approximately 577 million people are affected with CLBP at any one time. <sup>2</sup> CLBP is the most common reason that people seek healthcare intervention in the United States and United Kingdom. <sup>3-7</sup> It is important to provide more effective and cost-effective interventions to reduce the socioeconomic impact of CLBP. International guidelines consistently recommend exercise therapy as a first-line treatment; <sup>8-11</sup> it is cost-effective and provides moderate improvements in pain and physical function compared with usual care. <sup>8,10–12</sup>

Exercise is a complex intervention that may exert its effects through many plausible biological, psychological and social mechanisms; <sup>13</sup> however, the exact mechanisms are not fully understood and require further investigation. <sup>14,15</sup> Pilates is one type of exercise therapy that is increasingly being used and has demonstrated clinically important improvements in pain and physical function compared with other exercise types. <sup>16</sup> Developed by Joseph Pilates in the 1920s, Pilates is a mind-body exercise originally named 'Contrology'. <sup>17</sup> The exercises can be performed on a mat or with specialised equipment following six basic principles: centring, concentration, control, precision, flow and breathing. <sup>18,19</sup> These six principles may target several psychological mechanisms (eg, kinesiophobia, pain catastrophising)<sup>20</sup> or biological

Research 169

mechanisms (eg, muscle strength and control).[18](#page-5-10),[21](#page-5-13) Wun et a[l14](#page-5-6) proposed that exercise may work through neuromuscular, psychosocial, neurophysiological, cardiometabolic and tissue-healing mechanisms. However, the exact mechanism(s) for how Pilates exercise affects patient-important outcomes are unclear.

Due to their clinical importance to participants and providers, pain and physical function are agreed core outcomes for randomised controlled trials (RCTs) of exercise therapy for CLBP.[22](#page-5-14) However, most exercise therapies tested in RCTs are not designed to directly target pain or physical function (primary outcomes) but likely target mediating variables or mechanisms that are assumed to improve pain or physical function[.23](#page-5-15) The United Kingdom Medical Research Council's guidance on the evaluation of complex interventions recommend the use of process evaluation to explore how interventions create change.[24](#page-5-16) Psychological variables (eg, pain catastrophising and kinesiophobia) have increasingly been acknowledged as important mediating effects in explaining how interventions create change[.14](#page-5-6)[,15](#page-5-7) These mediating effect(s) require further evaluation through the use of mediation analysis to quantify the relationship between the intervention, proposed mediator and primary outcome. This is achieved by deconstructing the total effect, which is the entire effect of the intervention on the outcome, into indirect effect(s), which operate through the mediator(s), and direct effects, which do not.[25](#page-5-17) Understanding these mediating variables is important to improve future design, delivery and evaluation of exercise therapy in clinical settings and in RCT design.[26](#page-5-18) Few mediation studies have been performed on exercise therapy RCTs for LBP.[27](#page-5-19)–<sup>31</sup> The dataset[20](#page-5-12) included in this study is one of seven studies that were identified in a review that pre-specified their exercise intervention with potential mechanisms of effect for how Pilates effected change in pain and physical function outcomes[.32](#page-5-20)

This study aimed to use causal mediation analysis to determine whether the effect of Pilates exercise on pain intensity and physical function was mediated by changes in pain catastrophising and kinesiophobia.

Therefore, the research question for this mediation analysis was:

How much are the reductions in pain intensity and improvements in physical function from Pilates exercise mediated by changes in pain catastrophising and kinesiophobia?

# Method

# Design and participants

This study is reported according to AGReMA (A Guideline for Reporting Mediation Analyses[\)33](#page-5-21) and is a secondary causal mediation analysis of a four-arm RCT that assessed Pilates exercise dosage (once, twice or thrice per week) in addition to advice compared with advice only. In brief, this RCT was set in a physiotherapy clinic in Sao Paulo, Brazil, with blinding of research staff and statisticians. Participants were recruited through community advertisements. Randomisation was performed after baseline assessment using computer-generated random numbers concealed in sealed, opaque envelopes. All groups received advice through an educational booklet and participants were allowed to use their normal medication. Two hundred and ninety-six participants with CLBP were included. The primary trial was powered for 296 participants, but no formal sample size was calculated for the mediation analysis. Due to the nature of a secondary mediation analysis, patient and public involvement was not possible.

Statistically significant differences in the primary outcomes of pain intensity and physical function were found in favour of all Pilates arms at 6 weeks after randomisation in comparison with advice only. Pain intensity was measured on the Numerical Rating Scale from 0 'no pain' to 10 'the worst possible pain' [34](#page-5-22) (MD 21.2, 95% CI 22.2 to 20.3 for once weekly; MD 22.3, 95% CI 23.2 to 21.4 for twice weekly; MD 22.1, 95% CI 23.0 to 21.1 for thrice weekly). Physical function was measured with the Roland Morris Disability Questionnaire[35](#page-5-23)[,36](#page-5-24) using 24 dichotomous questions; higher summed scores indicated greater disability (MD 21.9, 95% CI 23.6 to 20.1 for once weekly; MD 24.7, 95% CI 26.4 to 23.0 for twice weekly; MD 23.3, 95% CI 25.0 to 21.6 for thrice weekly). The full description and results of the RCT have been described elsewhere[.20](#page-5-12)

#### Interventions

#### Pilates treatment

All participants in the Pilates arms received supervised individualised one-to-one mat and apparatus exercises for 6 weeks with varying dosages. Treatment sessions lasted for 1 hour. The three different Pilates groups compared dosages of once weekly, twice weekly and thrice weekly. There was no clinically significant difference between these three groups so they were collapsed into one group for this analysis. Most participants adhered to the treatment dosage, with 85% attendance in the once and twice weekly arms, and 82% attendance in the thrice weekly arm. TIDieR and CERT assessments were conducted (see Appendices 1 and 2, respectively, on the eAddenda).[20](#page-5-12),[37](#page-5-25)

#### Control arm

The control group did not receive any additional treatment other than an information booklet. The booklet contained recommendations related to posture and movements of activities of daily living, information on low back pain and anatomy of the spine and pelvis[.20](#page-5-12) They were informed that they would receive Pilates after the 12 month follow-up.

#### Data collection

All questionnaires and scales used to assess outcomes and mediators were translated and adapted to Brazilian Portuguese and had acceptable measurement properties,[35,](#page-5-23)[38](#page-6-0)–<sup>42</sup> with equivalent results to the original versions. All outcomes and mediators were measured at baseline and at 6 weeks and 6 months after randomisation.

# Outcome measures

The primary outcomes for the causal mediation analyses were pain intensity, rated on an 11-point Numeric Rating Scale (0 to 10 points), and physical function on the 24-item Roland-Morris Disability Questionnaire (0 to 24 points) at 6 months after randomisation.[35](#page-5-23),[38,](#page-6-0)[39](#page-6-1) Higher scores indicated worse outcomes in both instruments.

# Putative mediators

The putative mediators were pain catastrophising (Pain Catastrophising Scale: 0 to 52 points) and kinesiophobia (Tampa Scale of Kinesiophobia: 17 to 68 points) measured at 6 weeks after randomisation. Higher scores demonstrated worse outcomes in both scales. Both measures are common in research and clinical practice[.40](#page-6-2)–<sup>44</sup>

# Confounders

No confounding of the intervention-mediator and interventionoutcome relationships was assumed due to random allocation of participants. A directed acyclic graph (DAG) was constructed to identify potential pre-treatment confounders of the mediatoroutcome relationship for each mediator and outcome of interest (see Appendix 3 on the eAddenda). This was modified according to literature and peer feedback.[45,](#page-6-3)[46](#page-6-4) Our DAG implied that the following pre-treatment confounders required adjustment: sex, age, duration of LBP, educational level, use of pain medication, feeling depressed (mood) and income level. The analysis included: age and duration of LBP (each of which was measured as a continuous variable in years); and previous treatment, use of pain medicine and feeling depressed (each of which was recorded as a dichotomous variable in response to a single yes/no question at baseline).

### Data analysis

A preregistered analysis plan registered on Open Science Framework was followed for the mediation analysis. All analyses were conducted in free softwarea using the 'mediation' package[.47](#page-6-5) The

<span id="page-2-0"></span>Figure 1. Single mediator model for pain intensity outcome. The total natural indirect effect (TNIE) is represented by the orange and yellow lines through the mediator pain catastrophising (the combination of paths a and b); the pure natural direct effect (PNDE) is represented by the purple line; and the total effect (TE) is the combination of the orange, yellow and purple lines. The influence of possible confounders is represented by the green lines.

primary aim of identifying single mediator mechanisms through kinesiophobia and pain catastrophising to physical function and pain intensity was estimated from single mediator models. A single mediator model was constructed for each outcome (pain intensity and physical function) and mediator combination, with four models in total.

For each single mediator model, we estimated the interventionmediator effect, the mediator-outcome effect, the total natural indirect effect (TNIE), the pure natural direct effect (PNDE) and the total effect (TE) were estimated (see [Figure 1](#page-2-0)). The TNIE is the average intervention effect through the mediator; the PNDE is the average intervention effect that works through all other mechanisms, excluding the selected mediator; and the TE is the average effect of the intervention on the outcome. The TE is the sum of the TNIE and PNDE on the additive scale (see [Figure 1](#page-2-0) for example). The proportion mediated is the fraction of TE that is explained by TNIE.

For each single mediator model, we fitted two regression models: a mediator model and an outcome model. Linear regression models were used for all analyses because in each case the outcome variable was measured on a continuous scale[.47](#page-6-5) We ran the mediator models using linear regression, with treatment allocation as the independent variable and the mediator as the dependent variable, and the baseline values of the mediator as a covariate. Each of the outcome models for physical function and pain intensity used linear regression. The outcome models were constructed with the mediator as the independent variable; the outcome as the dependent variable; and the treatment allocation, baseline values of the meditator and outcome variables in addition to the set of observed pre-treatment confounders as covariates. To improve model flexibility, we included an interaction term (treatment allocation with mediator) in the outcome models[.47](#page-6-5) The regression outputs of each model were checked for posterior predictive checks, linearity, homogeneity of variance, collinearity, influential observations and normality of residuals. The 'mediate' function[47](#page-6-5) was used to compute TE, TNIE and PNDE. We used 1,000 bootstrapped simulations to generate 95% confidence intervals. Modelling assumptions for linear regression models (linearity and normally distributed residuals) were checked using graphical methods. The 'Tmint' function was used to assess the statistical significance of the intervention-mediator interactions[.47](#page-6-5)

We conducted sensitivity analyses to determine the robustness of the TNIE to bias introduced by residual confounding.[47](#page-6-5) The 'medsens' function was used to estimate the magnitude of residual confounding that would cause the point estimate of the TNIE to be zero.[47](#page-6-5) We also repeated the causal mediation analyses using the same four single mediator models comparing the Pilates twice weekly arm only and the control arm. We had planned to use multiple mediator models, but as only small proportions of mediation were found in the single mediator models, this was not performed.

#### Missing data

Missing data did not exceed 15% so post hoc sensitivity analyses were not conducted to assess the possible impact of missing data. All analyses were conducted on complete cases using listwise deletion.

#### Interpretation of results

To assist in interpreting the size of the mediated effects, the proportions mediated were classified as: 0 to 20% small, . 20 to 50% moderate and . 50% large[.48](#page-6-6)

# Results

# Participants

Participants (n = 255) were predominantly female (n = 201, 75%), middle-aged (47 years, SD 15) and had a long duration of LBP symptoms (mean 6.44 years, SD 6.91) [\(Table 1](#page-2-1)). A total of 6.42% of missing data was identified in both the mediation variables at 6 weeks (pain catastrophising and kinesiophobia) and 10.47% was identified in the 6-month post-randomisation data for both pain intensity and physical function. Complete case analysis was used, resulting in the reduction of sample size from 296 to 255 (see Appendix 4 on the eAddenda). There was no difference between the excluded cases in the mediation dataset and the original dataset.

<span id="page-2-1"></span>Table 1 Baseline variables of the meditation dataset compared with the original dataset.

| Variable                                     | Original dataset<br>(n = 296) | Mediation dataset<br>(n = 255) |
|----------------------------------------------|-------------------------------|--------------------------------|
| Age (y), mean (SD)                           | 48 (15)                       | 47 (15)                        |
| Female, n (%)                                | 224 (76)                      | 201 (76)                       |
| Pain intensity (0 to 10), mean (SD)          | 6.2 (1.9)                     | 6.3 (1.9)                      |
| Physical function (0 to 24), mean (SD)       | 11.7 (5.1)                    | 11.9 (5.1)                     |
| Possible confounders                         |                               |                                |
| Duration of symptoms (y), mean (SD)          | 6.48 (6.93)                   | 6.44 (6.91)                    |
| Previous treatment, n (%)                    | 142 (48)                      | 133 (50)                       |
| Medication use, n (%)                        | 160 (54)                      | 148 (52)                       |
| Feeling depressed, n (%)                     | 176 (59)                      | 160 (60)                       |
| Pain catastrophising (0 to 52),<br>mean (SD) | 25 (11)                       | 25 (11)                        |
| Kinesiophobia (17 to 68), mean (SD)          | 40 (8)                        | 40 (8)                         |

Research 171

<span id="page-3-0"></span>Table 2 Causal mediation analysis of pain intensity at 6 months after randomisation.

| Variable                                      | Pain catastrophising<br>(n = 255)             | Kinesiophobia<br>(n = 255)                    |
|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|
|                                               | Mean difference (95% CI)                      |                                               |
| Intervention-mediator effect<br>(path a)      | –4.17 (–7.17 to –1.17)                        | –4.65 (–6.70 to –2.60)                        |
| Mediator-outcome effect<br>(path b)           | –0.03 (–0.09 to 0.03)                         | –0.00 (–0.09 to 0.09)                         |
| TNIE                                          | –0.21 (–0.47 to –0.03)                        | –0.31 (–0.64 to –0.05)                        |
| PNDE                                          | –0.75 (–1.62 to 0.07)                         | –0.67 (–1.50 to 0.19)                         |
| Proportion mediated (treated)<br>Total effect | 0.20 (0.03 to 1.08)<br>–0.96 (–1.75 to –0.17) | 0.30 (0.03 to 1.45)<br>–0.98 (–1.79 to –0.14) |

TNIE = total natural indirect effect; PNDE = pure natural direct effect.

We calculated the correlation between baseline variables and found kinesiophobia and pain catastrophising to be correlated at 59%, which was insufficiently collinear to prevent the planned study proceeding (see Appendix 5 on the eAddenda)[.49](#page-6-7)

#### Causal mediation analysis

The causal mediation analysis showed that changes in pain catastrophising and kinesiophobia could partially explain how Pilates exercise reduced pain intensity and improved physical function outcomes. Specifically, significant indirect effects were found for pain catastrophising (MD –0.21, 95% CI –0.47 to –0.03) and kinesiophobia (MD –0.31, 95% CI –0.64 to –0.05) on pain intensity (see [Table 2](#page-3-0)). Significant indirect effects were also found for pain catastrophising (MD –0.64, 95% CI –1.21 to –0.20) and kinesiophobia (MD –1.06, 95% CI –1.74 to –0.46) on physical function (see [Table 3\)](#page-3-1). The proportion of TE mediated by pain catastrophising and kinesiophobia was 0.20 (95% CI 0.03 to 1.08) and 0.30 (95% CI –0.03 to 1.45) on pain intensity and 0.34 (95% CI 0.07 to 1.61) and 0.55 (95% CI –0.20 to 2.88) on physical function, respectively. Intervention-mediator interactions were statistically significant for both pain catastrophising and kinesiophobia for physical function but not for pain intensity (see Appendix 6 on the eAddenda). Sensitivity analyses demonstrated that these effects were likely to be robust to residual confounding (see [Figure 2](#page-4-0) - middle and far right panels), as moderate confounding (0 to 5 points) would be required to reduce the TNIE effect to 0. The results in the Pilates twice weekly group only in comparison with the control arm demonstrated a partial mediating effect of pain catastrophising and kinesiophobia on physical function but not on pain intensity (see Appendix 6 on the eAddenda).

# Discussion

This study aimed to investigate how Pilates exercise reduced pain intensity and improved physical function compared with an educational booklet control. Through causal mediation analysis, it found that both pain catastrophising and kinesiophobia were treatment mediators explaining a small to moderate proportion of the effect of Pilates exercise on pain intensity and physical function. Changing kinesiophobia appears to be an important treatment target of

<span id="page-3-1"></span>Table 3 Causal mediation analysis on physical function at 6 months after randomisation.

| Variable                                 | Pain catastrophising<br>(n = 255) | Kinesiophobia<br>(n = 255) |
|------------------------------------------|-----------------------------------|----------------------------|
|                                          | Mean difference (95% CI)          |                            |
| Intervention-mediator effect<br>(path a) | –4.18 (–7.19 to –1.17)            | –4.73 (–6.78 to –2.67)     |
| Mediator-outcome effect<br>(path b)      | –0.00 (–0.12 to 0.11)             | –0.00 (–0.19 to 0.15)      |
| TNIE                                     | –0.64 (–1.21 to –0.20)            | –1.06 (–1.74 to –0.46)     |
| PNDE                                     | –1.23 (–2.92 to 0.44)             | –0.82 (–2.42 to 0.83)      |
| Proportion mediated (treated)            | 0.34 (0.07 to 1.61)               | 0.55 (0.20 to 2.88)        |
| Total effect                             | –1.87 (–3.45 to –0.35)            | –1.88 (–3.34 to –0.39)     |

TNIE = total natural indirect effect; PNDE = pure natural direct effect.

exercise therapies, explaining around a half of the improvement in physical function.

Pain intensity and physical function are two of the agreed core outcomes for LBP research.[50](#page-6-8) These are the most commonly used primary outcomes in RCTs of exercise and CLBP.[23](#page-5-15),[32](#page-5-20),[51](#page-6-9) In this secondary analysis, pain catastrophising and kinesiophobia were both mediators on the pathway to changing pain intensity and physical function.[20](#page-5-12) Increasingly, CLBP is recognised as a condition with multidimensional effects, with an interaction between physical, psychological, social, lifestyle, comorbid health states and nonmodifiable factors (genetics, sex and life stage)[.52](#page-6-10) The fearavoidance model is well-established, and suggests that fear of pain drives persistent pain states and pain-related disability (conceptual theory). Kinesiophobia (fear of movement) is a construct included within this model. The 'activity' avoidance model suggests that when fear of pain exists, this leads to a conditioned response of increased fear, anxiety and muscle tension.[53](#page-6-11) More recently, the common-sense model recognised fear of movement as a natural response to CLBP and suggested that it is a key treatment target for physiotherapists[.54](#page-6-12)

Many interventions for CLBP, such as mind-body, exercise and cognitive behavioural treatments, appear to share similar mediating pathways via shared psychological mechanisms such as pain catastrophising, kinesiophobia, self-efficacy and distress.[55](#page-6-13) Woby et a[l56](#page-6-14) found, in an observational study, that changes in fear-avoidance beliefs and increased perceptions of control over pain were predictive of changes in physical function in those with CLBP. Previous studies have demonstrated the mediating role of pain catastrophising in Tai Chi exercise and aerobic exercise on pain intensity and physical function in comparison with waitlist controls[.27,](#page-5-19)[28](#page-5-26) Fear-avoidance beliefs mediated the effect of physical function when individualised exercises were prescribed in comparison with usual care[.31](#page-5-27) Other studies have found mediating effects of pain self-efficacy in cognitive functional therapy compared with group exercise and education on physical function outcomes.[57](#page-6-15) Many of the mediation analyses performed to date on studies of exercise and psychological interventions suggest that these psychological mechanisms may explain around 20 to 30% of the pathways to changes in outcomes.[58](#page-6-16) This is in contrast to the results of this study, which demonstrated that kinesiophobia appeared to moderate half (55%) of the pathway of Pilates exercise to improved physical function. All other combinations of mediatoroutcome relationships in this study only mediated 20 to 34% of the pathways to improved pain and physical function. This study adds further evidence that kinesiophobia may have an important mediation role in changing the outcome of physical function. However, the proportion mediated is strongly influenced by the control group, such that if the control group is also likely to change the mediator slightly, this will result in a smaller proportion mediated; this is in contrast to a scenario where the control group does not address the mediator at all and the proportion mediated is likely to be larger.

Although Pilates exercises seem to be more effective than other exercise types for patients with CLBP, there are no studies that have investigated mediators that may contribute to the overall effects of Pilates exercise on pain intensity and physical function. Thus, the results of this study provide novel results to fill this gap in the literature. Furthermore, this mediation study is a secondary analysis of a high-quality RCT with a large sample size, concealed allocation, intention-to-treat analysis, , 15% missing data, and adherence to treatment of . 82%. This analysis provides exploratory findings that warrant further evaluation, as the original RCT was not powered to provide definitive evidence on mediators in the original RCT analysis plan. We preregistered the analysis plan for the mediation analysis, and the analysis and results were reported according to AGReMA recommendations. This study had limitations in that the RCT was not designed to conduct mediation analyses, but proposed mediators were identified and measured a priori, which is a strength of the trial design and this analysis. Although the sample size was reduced due to the presence of missing data, this was likely completely at random and unlikely to bias results. There may have been residual confounding through unmeasured confounders, but sensitivity analyses were performed to ensure robustness of these results.

<span id="page-4-0"></span>Figure 2. Summary plots of causal single mediation models. Within the sensitivity plots, the average mediation effects are plotted as a function of the sensitivity parameter (magnitude of residual confounding). A sensitivity parameter of 0 represents null hypothesised levels of residual confounding, and the extremes of –1 and 1 represent maximum hypothesised levels of residual confounding. Grey zones represent 95% confidence limits of the estimated mediation effect across a range of hypothesised levels of residual confounding.

CLBP is a condition with multidimensional effects, and it is still unclear which components of intervention are needed to improve patient's symptoms. The importance of focusing on the biopsychosocial nature of CLBP in treatment prescription has become a priority in recent years[.3,](#page-5-2)[52,](#page-6-10)[59](#page-6-17)[,60](#page-6-18) The findings from this study can help clinicians to optimise the provision of Pilates exercise through a biopsychosocial lens by identifying and directly targeting the identified psychological components. Doing so may lead to reductions in pain intensity and improvements in physical function in patients with CLBP. Clinicians could consider targeting their Pilates exercise treatments to better address these identified psychological components by first conducting a biopsychosocial assessment,[61,](#page-6-19)[62](#page-6-20) including the use of patient-reported outcome measures (eg, Tampa Scale of Kinesiophobia or Pain Catastrophising Scale), to identify the importance of these psychological components in CLBP. A greater understanding of the patient's biopsychosocial presentation, including primary contributor factors, will provide greater opportunity for exercise prescription and communication to be individualised to the patient and their respective goals[.62](#page-6-20)[,63](#page-6-21) Second, clinicians could consider optimising their clinical encounter by prescribing or supervising Pilates exercise to better reduce fear of movement and worrisome thoughts about pain. This could be achieved through both verbal and non-verbal communication that emphasises safety and confidence in the person's ability to perform the exercise[.62](#page-6-20) Clinicians could further support their exercise prescription by providing additional education regarding the benefit of exercise and physical activity, robustness of

the body to movement, and importance of physical activity in recovery to help further reduce pain catastrophising and fear of movement.[64](#page-6-22)–<sup>66</sup> These educational messages could be verbally communicated during exercise or non-verbally through environmental cues such as posters in the clinic.

This mediation analysis contributes to the initial understanding of the underlying positive effect of the addition of Pilates exercise to advice on pain intensity and physical function when compared with advice only. Further research identifying the best methods to target these components may be useful for improving treatment delivery. However, a limited number of potential mediating factors were investigated in this study. Future research could also investigate other key factors that may be important in the process of changing clinical outcomes (such as pain self-efficacy or pain-related distress) in Pilates exercise-based treatment, as well as physical measures (such as motor control, strength, range of motion) given the hypothesised mind-body effects. The non-specific effects of therapeutic engagement and alliance and their effect on overall outcomes and psychological aspects of CLBP are increasingly being recognised and may account for part of the unmeasured mediation effect.[67](#page-6-23)–<sup>70</sup> Other mediators that may also contribute to the effect on pain intensity and physical function include personal components such as exercise selfefficacy (measured with the exercise self-efficacy scal[e71\)](#page-6-24) or the patient's locus of control.[72](#page-6-25) Trials wishing to prospectively capture these data need to ensure that there is a justifiable theoretical basis for the proposed mediators, there are sufficient measurement points to allow Research 173

evaluation of change, and that the mediator is temporally measured in comparison with the outcome variable, such that the impact of the mediator on a later outcome time point can be assessed.[26](#page-5-18) Understanding the discrete components that mediate pathways of exercise to changes in pain intensity and physical function will allow clinicians to more accurately target their interventions to greatest effect.

Reductions in pain catastrophising and kinesiophobia mediated some of the pathway to improved pain intensity and physical function when using Pilates exercise for CLBP. Kinesiophobia particularly appeared to mediate a significant proportion of the pathway to improved physical function. These psychological components may be important treatment targets to consider when tailoring exercise for CLBP. Clinicians should focus on the psychological elements associated with CLBP through assessment and targeting of treatments to these factors, as they may be important intermediate factors to create change in the outcomes pain intensity and physical function. This study provides exploratory results that suggest further prospective evaluation in a fully-powered RCT is warranted.

What was already known on this topic: Pilates is one type of exercise therapy that has been increasingly used and has demonstrated clinically important improvements in low back pain and its associated dysfunction compared with other exercise types.

What this study adds: Reductions in pain catastrophising and kinesiophobia partially mediated the pathway to improved pain intensity and physical function when using Pilates exercise for chronic low back pain. These psychological components may be important treatment targets for clinicians and researchers to consider when prescribing exercise for chronic low back pain.

Footnotes: <sup>a</sup> R software V4.1.2, R Core Team, Vienna, Austria. eAddenda: Appendices 1 to 6 can be found online at [https://doi.](https://doi.org/10.1016/j.jphys.2023.05.008) [org/10.1016/j.jphys.2023.05.008](https://doi.org/10.1016/j.jphys.2023.05.008)

Ethics approval: No ethical approval was required for this secondary analysis of existing data. All participants signed informed consent documents and ethical approval was granted by the Research Ethics Committee of the Universidade Cidade de São Paulo (CAAE:29303014.7.0000.0064) for the original trial.

Competing interests: The authors have no conflicts of interest to declare.

Source(s) of support: LW's time was funded with an Orthopaedic Research UK Early Career Fellowship and an NIHR Post-doctoral bridging fellowship during the time this project was conceived and undertaken.

Acknowledgements: Prof Cristina Maria Nunes for sharing the trial dataset with LW.

Data sharing: The authors are happy to share the code used on direct request.

Correspondence: Lianne Wood, Faculty of Health and Life Sciences, University of Exeter, UK. Email: [l.wood2@exeter.ac.uk](mailto:l.wood2@exeter.ac.uk)

# Websites

Open Science Framework protocol <https://osf.io/jt6p4/>
