# $\color{#454775}{Analyzing}$ $\color{#454775}{Marketing}$ $\color{#454775}{Campaigns}$
## $\color{#454775}{Introduction:}$ 
This report analyzes a simulated marketing dataset representing ad-driven subscription activity for an online service during January 2018, covering 7,309 users with multi-channel exposures and subscription behaviors. The objective was to examine the determinants of user conversion and retention, identify performance variations across marketing channels, evaluate A/B test results, uncover demographic influences, and explore subscription patterns across time, languages, and ad exposure frequency. A thorough data assessment and cleaning process were applied to correct inconsistencies, handle duplicates and missing values, standardize dates, and reconcile logical mismatches before analyzing the cleaned dataset.
## $\color{#454775}{Objectives:}$ 
1.	Identify key drivers of user conversion and retention.
2.	Measure the impact of repeated ad exposures on conversion outcomes.
3.	Examine how demographic elements (age, language) influence performance.
4.	Evaluate channel effectiveness across distribution, conversion, and retention.
5.	Detect temporal patterns in ad performance and subscription behavior.
6.	Diagnose issues such as data mismatch, technical bugs, and experiment design anomalies.
## $\color{#454775}{Challenges}$ $\color{#454775}{Faced:}$ 
-	***Duplicate and near-duplicate records*** (37 exact duplicates, multiple near-duplicates) inflated conversions and created conflicting values in age groups and retention indicators.
-	***Missing values*** often appeared in logically connected fields, requiring standardized rules for handling subscription/cancellation inconsistencies.
-	***User-level inconsistencies***, such as one user converting multiple times or being assigned different age groups, signaled systemic logging errors.
-	***Language mismatches***—97.55% of ads served in English despite multilingual users—introduced bias and skewed channel performance, especially in House Ads.
-	***Uneven distribution of exposures:*** 77.07% of users saw only one ad, while a small segment (22.93%) saw up to 12 impressions, heavily influencing conversion/retention outcomes.
-	***Technical bug in House Ads*** caused recurring language mismatches after January 10, heavily distorting conversion rates.
## $\color{#454775}{Obsevations:}$ 
-	***Peak daily exposure*** occurred on 15-01-2018 with 784 users.
-	***Weekly engagement*** was highest on Mondays (1,977 users), followed by Wednesdays (1,610) and Tuesdays (1,588).
-	***Supscription:*** 10.47% of all users converted after seeing an ad.
-	***Variant:*** Users were almost evenly assigned between the control and personalization groups.
-	***Language:*** 97.55% of ads displayed in English; language mismatch occurred 449 times, mainly from House Ads (86.68%).
-	***Age distribution*** heavily skewed toward younger users: 47.33% under age 30, with the largest segment being 19–24 (1,304 users; 16.56%).
-	***Channel distribution:*** House Ads (47.08%), Facebook + Instagram (≈29%), Push (9.96%), Email (5.65%).
-	***Ad repetition:*** 77.07% one-time exposure, 22.93% multi-exposure.
-	***Conversion Rates:***
    - _Overall Conversion Rate ≈ 13.01%_
    -	_Email (33.75%) highest overall - Despite its low distribution (5.65% of total Ads), & House Ads (7.40%) – Despite its extensive ad distribution (47.08%)._
    -	_Personalized ads: 16.80% vs Control: ≈10%_
    -	_Language match: 13.25%, non-matched: ≈6.70%_
    -	_German: 72.6%, Arabic: 50%, Spanish: 20%, English: 12.12%_
    -	_Younger Users (under 30) ≈ 19.29%, Older Users (above 30) ≈ 7.29%_
    -	_The 16th and 17th of January recorded the highest conversion rates at 25.52% & 21.95, respectively._
-	***Retention Rates:***
    -	_Overall Retention Rate ≈ 65.95%._
    -	_Email 76.47% (Highest), House Ads 58.05 (Lowest)._
    -	_Control ads: 67.63% vs Personalized: ≈65.5%_
    -	_German: 66.04%, Arabic: 58.33%, Spanish: 66.67%, English: 66.03%_
    -	_matched language (66.33%) is significantly higher than non-matched language (51.85%)._
    -	_Ages 19-24 & 30-36 form the highest Retention Rates (68.65% & 64.53%, respectively)._
    -	_Ages 30-36 & 55+ tend to remain in a moderate Retention Rate despite their lower Conversion Rates._
- ***Multi-exposure users:*** Conversion 17.83%, Retention 70.19%, & ***One-time exposure:*** Conversion 11.58%, Retention 64.01%.
- ***Demographic Influence:***
    - _Arabic and German outperformed other languages overall, showing strong conversion rates across most age groups, & English had the weakest performance, especially among users aged 30 and above, where conversion rates drop significantly._
  - _Ages 19–24 consistently exhibit the highest conversion rates across all marketing channels, within this age group, Email performs strongest (45.79%), followed by Instagram (31.23%) and Facebook (23.26%)._
-	***Supscription Pattern:*** Email is the strongest marketing channel across all age groups, especially for users younger than 30.
-	***Variant Pattern:*** Personalized ads are highly effective among younger audiences (under 30), while simpler, non-personalized messages may resonate better with older users (30+).
-	***Language Bug Impact:*** The Overall Estimated Lost Subscribers via House Ads _(with no bug)_ ≈ 26, Arabic ≈ 12, German ≈ 10, & Spanish ≈ 6.
-	The Email Personalization Group outperformed Control Group by 38.85%. 
-	***A/B Testing:***
    - _Email Personalized Ads in English & Spanish performed well with an increase by 31.85% & 166.67 % respectively._
    - _Ages below 30: Email Personalized Ads outperformed Control Ads, showing strong positive lift (121.40% for 0-18, 106.24% for 19-24, & 161.19% for 24-30)._
### $\color{#454775}{Insights:}$ 
1.	***Marketing channels strongly influence performance:*** Email and Instagram are the most efficient, with Email generating the highest conversion and retention rates despite low distribution.
2.	***Personalization increases conversions but not retention:*** Personalized ads outperform control in conversions but underperform in long-term retention, especially for users aged 30+.
3.	***Demographic influences are significant:*** Younger users (under 30) convert and retain better; German and Arabic-speaking users show exceptionally high conversion rates across age groups.
4.	***Multi-exposure campaigns are effective:*** Users shown ads multiple times demonstrate significantly higher conversion and retention rates, confirming the positive reinforcement effect.
5.	***House Ads underperform severely:*** High distribution but low conversion/retention due to technical language mismatches. After January 10, mismatches rose sharply while conversions dropped.
6.	***Temporal patterns matter:*** Mid-month peaks, particularly January 15–17, strongly correlate with the impact of email campaigns.
7.	***A/B Testing confirms Email personalization success:*** Statistically significant improvement in conversion suggests personalized email content is effective (p-value ≈ 0.65%).
8.	***Bias exists in conversion/retention comparisons:*** uneven exposure, disproportionate language distribution, and small subgroup sizes limit generalizability.
## $\color{#454775}{Data}$ $\color{#454775}{Bias}$ $\color{#454775}{Consideration:}$
***Upon reviewing the conversion and retention metrics, it is evident that several bias factors may be influencing the observed results:***
1. The distribution of users across languages and age groups is highly uneven, with some segments containing very small sample sizes, leading to extreme or unrealistic retention values such as 100% or 0%. In addition, the presence of missing values (NaNs) reduces comparability between categories and introduces uncertainty into trend interpretation.
2. The multi-touch versus single-exposure groups may also include self-selection bias, where more engaged users receive more ad impressions, inflating conversion and retention rates. <br>
***Taken together, these limitations suggest that the current findings should be interpreted with caution, as the results may not fully reflect the true performance across the broader user population.***
#### ***Rcommendation:***
- _To improve reliability and reduce bias in future analyses, it is recommended to ensure balanced sample sizes across demographic segments and apply randomization techniques when assigning ad types and exposure levels._
- _Additionally, incorporating statistical validation methods such as confidence intervals, cohort filtering, and weighted averages can help stabilize rate fluctuations and provide a more accurate representation of performance._
- _Completing missing data or excluding insufficiently sized groups will further strengthen the validity of the conclusions._

### $\color{#454775}{Recommendations:}$ 
1.	***Fix the language-serving bug immediately***—language mismatches directly reduced conversions, especially for Arabic and German users.
2.	***To improve reliability and reduce bias in future analyses***, it is recommended to ensure balanced sample sizes across demographic segments and apply randomization techniques when assigning ad types and exposure levels.
3.	***Reallocate budget toward Email, Instagram, and Facebook,*** where both conversion and retention outcomes are strongest. Reduce reliance on House Ads.
4.	***Adopt multi-touch exposure strategy:*** A controlled frequency cap (2–5 exposures) increases conversions without overwhelming users.
5.	***Segment campaigns by language and age:***
    - _Younger users → focus on personalized ads and social media channels._
    - _Older users → use simpler control-style messaging through email._
6.	***Redesign personalization strategy:*** Use personalized content for acquisition but incorporate standard messaging for retention.
7.	***Improve tracking infrastructure*** to prevent duplicate conversions and inconsistent logs.
8.	***Strengthen experiment design*** by balancing exposure across language groups and ensuring randomized distribution.
9.	***Conduct a second A/B test after system fixes*** to validate personalization impact without data bias.


