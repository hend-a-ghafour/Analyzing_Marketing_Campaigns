# $\color{#454775}{Analyzing}$ $\color{#454775}{Marketing}$ $\color{#454775}{Campaigns}$
## $\color{#454775}{Overview:}$
A fake marketing dataset based on the data of an online subscription business to investigate the following aspects:
- The key factors that strongly influence user conversion and retention.  
- The impact of repeated ads -if any- for a specific user on subscription patterns.  
- The influence of demographic factors on achieving higher conversion rates.  
- Subscription trends and patterns over a specific time period.  
- Investigating the best- and worst-performing marketing channels.  
## $\color{#454775}{Dataset}$ $\color{#454775}{Description:}$
- ***user_id*** $\color{#454775}{→}$ An identifier for each user _(7309 user)_.<br>
  >  $\color{#454775}{Note:}$ _A user may use more than one platform and engage in more than one day._
- ***date_served*** $\color{#454775}{→}$ The date when the ad was shown to the user _(01-01-2018 : 31-01-2018)_.
- ***date_subscribed*** $\color{#454775}{→}$ The date when the user subscribed after seeing the ad _(01-01-2018 : 31-01-2018)_.
- ***date_cancelled*** $\color{#454775}{→}$ The date when the user cancelled their subscription _(05-01-2018 : 09-05-2018)_.
- ***marketing_channel*** $\color{#454775}{→}$ The source through which the ad was delivered _(House Ads, Push, Facebook, Instagram, & Email)_.
- ***variant*** $\color{#454775}{→}$ Type of experiment group the user was placed in _(personalization or control)_. <br>
  > $\color{#454775}{Note:}$
  > - _**Personalization (variant = personalization)** → The user was shown a personalized version of the ad, meaning the ad content was tailored to their profile, preferences, or past behavior (**e.g.,** language choice, recommendations, or custom offers)._
  > - _**Control (variant = control)** → The user was shown a generic version of the ad, without personalization. This group is used as a baseline to compare results and measure how effective personalization is._
  > - 👉 ***In short:***
  >   - _**Personalization =** test group (customized ads)_
  >   - _**Control =** baseline group (standard ads)_
- ***converted*** $\color{#454775}{→}$ Indicates if the user subscribed after seeing the ad _(True/False)_.
- ***language_displayed*** $\color{#454775}{→}$ The language in which the ad was shown _(English, German, Arabic, & Spanish)_.
- ***preferred_language*** $\color{#454775}{→}$ The user’s preferred language _(English, German, Arabic, & Spanish)_.
- ***age_group*** $\color{#454775}{→}$ Age range of the user _(0–18, 19–24, 24–30, 30–36, 36–45, 45–55, & 55+)_.
- ***subscribing_channel*** $\color{#454775}{→}$ The channel through which the user actually subscribed _(House Ads, Email, Push, Facebook, & Instagram)_.
- ***is_retained*** $\color{#454775}{→}$ Indicates if the user continued the subscription _(True/False)_.
## $\color{#454775}{Data}$ $\color{#454775}{Assessing:}$
### $\color{#454775}{1.}$ ***Duplicated Values:***
  - ***The dataset had 37 Duplicated records.***
### $\color{#454775}{2.}$ ***Missing Values:***
   - ***date_served, marketing_channel, & converted columns:*** 
     - The three columns share the same missing rows _(except for date_served index 7038)_.
   - ***date_subscribed, date_canceled, subscribing_channel, & is_retained:***
     - These values are naturally missing depending on whether the user subscribed or not.
     - Some exceptions may arise that would require a precautionary measure to make sure that the data values are consistent with each other.
     - **For Example,** A handling step to make sure that if a user converted, the subscription information must be addressed as well.
### $\color{#454775}{3.}$ ***User Behaviour:***
***Users may be exposed to the same ad multiple times, with engagement frequencies ranging from 1 to 12 occurrences.***
#### ***After reviewing a sample of user engagements:***
- **A near-duplicated pattern was noticed for users' multiple exposures**
#### $\color{#454775}{\sf a)}$ **One user _(ID: a100000882)_ exhibited 12 ad exposures:**
- Within these 12 records, several entries appeared repeated, with some columns identical while others showed slight variations.
- **For instance,** this user converted in 4 records — two under the personalized variant (served on January 14) and two under the control variant (served on January 18). The subscription dates associated with these conversions were either January 14 or January 18, suggesting minor inconsistencies or multiple conversions logged for the same user within a short period.
#### $\color{#454775}{\sf b)}$ **A similar pattern was observed for another sample user with 10 ad exposures _(ID: a100000878)_:**
- The user interacted primarily through House Ads and Email channels.
- Multiple records showed identical values across most columns, with slight variations in date_served and date_subscribed.
- The user converted multiple times on the same channel _(Email, control variant)_ — an unusual pattern since a user typically subscribes only once.
- These repeated or inconsistent entries suggest potential data duplication or logging issues, where multiple impressions and conversions might have been recorded for a single actual event.
#### $\color{#454775}{\sf c)}$ **For a user with 8 recorded engagements _(User ID: a100000875)_, several inconsistencies were observed:**
- Despite being recorded as the same user, their age group alternated between 19–24 years and 45–55 years, indicating a data entry or merge error.
- The user converted four times.
- Subscription dates (1/7/18 and 1/11/18) were reused across records, often paired with inconsistent cancellation statuses.
- Some records show the user as retained, while others mark them as canceled, even within the same channel and week.
- This record highlights duplicated and conflicting user engagement logs, likely resulting from data integration or tracking issues.
#### $\color{#454775}{\sf d)}$ **Out of the 13 users who saw the ad 5 times, only 8 converted.**
## $\color{#454775}{Data}$ $\color{#454775}{Cleaning:}$
### $\color{#454775}{1.}$ ***Removing Duplicates:***
$\color{#454775}{a)}$ Remove Exact Duplicates (37 duplicated raws)<br>
$\color{#454775}{b)}$ Remove Near-Duplicates to ensures each user’s engagement on a given day with a specific ad type is counted only once. 
### $\color{#454775}{2.}$ ***Changing Dates Data type:***
$\color{#454775}{a)}$ ***date_served:*** _str_ to _date_ <br>
$\color{#454775}{b)}$ ***date_subscribed:*** _str_ to _date_ <br>
$\color{#454775}{c)}$ ***date_canceled:*** _str_ to _date_ <br>
### $\color{#454775}{3.}$ ***Standardize supscription Dates:***
To ensure logical and consistent relationships between engagement and subscription dates, the following adjustments were applied: 
#### $\color{#454775}{a)}$ ***For converted users:*** 
- ***Issue:*** Some records show _date_subscribed_ earlier than _date_served_. However, a user cannot subscribe before seeing the ad.
- ***Action:*** When _converted = True_ and _date_subscribed < date_served_, replace _date_subscribed_ with _date_served_.
#### $\color{#454775}{b)}$ ***For not-converted users:*** 
- ***Issue:*** Some users who were exposed to multiple ads have a _date_subscribed_ value recorded even when _converted = False_. This creates inconsistencies since non-converted records should not have a valid subscription date.
- ***Action:*** Set _date_subscribed_ to _NaN_ for all non-converted users to remove this confusion.
### $\color{#454775}{4.}$ ***Handeling Missing Value:***
#### $\color{#454775}{a)}$ Shared nulls across date_served (except for index 7038), marketing_channel, converted: 
Since those columns share the same missing rows, dropping them together avoids keeping incomplete entries that would otherwise distort the analysis.
#### $\color{#454775}{b)}$ date_served (index 7038): 
Since this is an isolated null in the middle of the dataset, forward-filling (ffill) after sorting by date is a reasonable strategy.
#### $\color{#454775}{c)}$ date_subscribed:
1. ***As a Precautionary measure,*** if the user converted,the missing values (if any) would be replaced with **date_served**.  
2. If the user didn't convert, There is no need to handle the missing values as these values are naturally missing depending on whether the user subscribed or not.
#### $\color{#454775}{d)}$ date_canceled:
There is no need to handle its missing values in as these values are naturally missing depending on whether the user canceled his subscription or not. Filling them would introduce bias.
#### $\color{#454775}{e)}$ subscribing_channel:
1. ***As a Precautionary measure,***
   - If the user converted,the missing values (if any) would be replaced with **marketing_channel**
   - If the user didn't convert & the subscribed channel isn't empty,then these values should be replaced with **NaN**.  
2. If the user didn't convert, There is no need to handle the missing values as these values are naturally missing depending on whether the user subscribed or not .
#### $\color{#454775}{f)}$ is_retained: 
1. ***As a Precautionary measure,***
   - If the user converted and there is no mention for canceling the subscription ,the missing values (if any) would be replaced with **True**.
   - If the user didn't convert & the is_retained value isn't empty,then these values should be replaced with **False**.  
2. If the user didn't convert, There is no need to handle the missing values as these values are naturally missing depending on whether the user subscribed or not.
### $\color{#454775}{5.}$ ***Adjusting user_id Column:***
Due to the inconsistences in some records, where a user may have more than one age group, it would be better to adjust the user name column by adding the first 2 charcters of age group values to the user id
### $\color{#454775}{6.}$ ***Adding New Columns:***
- ***is_house_ad:*** Identifies if a particular marketing asset was a house ad or not _(since it is the most frequent value in this column "4733 out of 10000")._
- ***matched_lang:*** conveys whether the ad was shown to the user in their preferred language.
- ***dow:*** service Days starting from Monday till Sunday, t measure the most frequent days.
- ***ad_exposure:*** to check whether the user saw the ad multiple times or once.
### $\color{#454775}{7.}$ ***Mapping Values:***
Due to the way pandas stores data, in a large dataset, it can be computationally inefficient to store columns of strings. In such cases, it can speed things up to instead store these values as numbers. <br>
***converted will be as follows:***
- _True = 1_
- _False = 0_
## $\color{#454775}{Data}$ $\color{#454775}{Exploring:}$
## $\color{#454775}{-}$ $\color{#454775}{Initial}$ $\color{#454775}{Investigation:}$
### $\color{#454775}{Observations:}$
- The highest number of users who saw an ad was recorded on 15-01-2018 (Monday), with a total of 784 users. Before this peak, the average daily users were around 327, and afterward, around 284 users per day.
- Users were most engaged at the beginning of the week, particularly on Mondays (1,977 users), followed by Wednesdays (1,610) and Tuesdays (1,588).
- Users were almost evenly assigned between the control and personalization groups, _suggesting that the experiment was fairly designed to compare the effectiveness of personalized ads versus standard ads_.
- Approximately 10.47% of users subscribed after seeing the ad, _indicating that while ads reached a wide audience, their effectiveness in driving subscriptions was limited._
- Around 97.55% of ads were displayed in English, regardless of the user’s preferred language.
- For Arabic, German, and Spanish users, the number of ads displayed in their preferred language was significantly lower than the number of users who preferred those languages.
- House Ads accounted for the largest share of language mismatches (449 occurrences, 86.68%), likely due to a technical bug affecting ad performance.
- Users aged 19–24 formed the largest segment (1,304 users, 16.56%), with nearly half of all users under 30 (47.33%), _indicating that younger audiences were a primary target group_.
- About 47% of users were reached through House Ads, _making it the primary marketing channel_.
- Facebook and Instagram together contributed around 29%, while Push and Email accounted for 9.96% and 5.65%, respectively.
- 77.07% of users exposed to the ad only once, & 22.93% saw the ad multiple times.
### $\color{#454775}{Key}$ $\color{#454775}{Findings:}$
- ***The experiment was fairly designed to compare the effectiveness of personalized ads versus standard ads.***
- ***Social media channels (Instagram and Facebook) generated more than half of total subscriptions, highlighting their effectiveness in driving conversions.***
- ***Despite its large reach, House Ads showed relatively low subscription and retention rates, suggesting inefficiency in converting exposure into meaningful engagement.***
- ***Email marketing, though having the lowest ad distribution, showed a notable subscription pattern, indicating potential for higher efficiency if optimized.***
- ***The misalignment between ad distribution and conversion performance suggests that marketing efforts might not be fully optimized for channel effectiveness or audience targeting.***
- ***Across all channels, more than half of the subscribed users were retained, reflecting a generally strong retention performance once users converted.***
## $\color{#454775}{a)}$ $\color{#454775}{Influence}$ $\color{#454775}{Factors:}$
### $\color{#454775}{1-}$ **key factors that strongly influence user conversion and retention:** 
#### $\color{#454775}{-}$ _Marketing Channels:_
### $\color{#454775}{Observations:}$
- Email demonstrates the highest performance, achieving both the top conversion rate (3.75%) and retention rate (76.47%) _-Despite its low distribution (5.65% of total Ads)_.
- Social Media Platforms had a moderate performance with a retention rate close to the overall rate (13.01%), but facebook subscribers were tending to retain more with  a retention rate of 68.30% _(2nd ranking)_.
- Push notifications rank second in retention (67.95%), despite their low distribution (9.96%) and conversion rate (7.94%), suggesting strong post-conversion engagement.
- House Ads exhibit a performance gap, with extensive ad distribution (47.08%) not translating into results — both conversion (7.40%) and retention (58.05) rates remain the lowest.
#### $\color{#454775}{-}$ _Variant:_
### $\color{#454775}{Observations:}$
- Personalized ads show significantly higher conversion rate of 16.80%, _indicating that personalized messages were more effective at encouraging users to subscribe initially_.
- A Higher retention rate of was achieved by Controlled Ads 67.63%, exceeding the Personalized group (65.50%) -_Although personalization increased conversions, it did not translate into stronger long-term retention_.
#### $\color{#454775}{-}$ _Languages:_
### $\color{#454775}{Observations:}$
- Non-English languages show notably higher Conversion Rates (German 72.60%, Arabic 50%, & Spanish 20%) compared to English 12.12%.
- Users tend to subscribe more when the ad language matches their preferrences achiving a Conversion Rate of 13.25%.
- Spanish, German, & English show a relatively close Retention Rates (66.67%, 66.04%, & 66.03%, respectively), while Arabic users had a moderate Retention Rate 58.33%.
- Retention Rate for matched language (66.33%) is significantly higher than that of non-matched language (51.85%).
  > $\color{#454775}{Note:}$ _The huge gap between the number of users with matched language (7531 user) and the nit matched language (403 users) should be taken into consideration when further investigating these noticable gaps in conversion and retention rates._
#### $\color{#454775}{-}$ _Languages:_
### $\color{#454775}{Observations:}$
- **Yonger Users (under 30) →** 19–24 years achieved the highest Conversion Rate (23.24%), followed by 24–30 years (18.72%) and 0–18 years (15.92%), _This is consistent with the Ad Distribution across Age Groups_.
- **Older Users (above 30) →** showed a significant drop in engagement, with Conversion Rates around 7.29%, & are less likely to engage or convert, _suggesting that ad content  or platform selection may not align well with their preferences_.
- Ages 19-24 & 30-36 form the highest Retention Rates (68.65% & 64.53%, respectively).
- Ages 0-18, 24-30, & 55+ had a Retention Rates that are relatively close to the Overall Retention Rate of 65.95%.
- Ages 30-36 & 55+ tend to remain in a modertae Retention Rate despite their lower Conversion Rates.
#### $\color{#454775}{-}$ _Date Served:_
### $\color{#454775}{Observations:}$
- The 16th and 17th of January recorded the highest conversion rates at 25.52% & 21.95, respectively, _This spike aligns with the peak in ad views on January 15 (784 view)_.
- The retention rates across different dates show no clear or consistent pattern, _indicating that user retention was not strongly influenced by the specific date the ad was served_.
### $\color{#454775}{Key}$ $\color{#454775}{Findings:}$
- ***Adopting a more strategic distribution of ads could improve the engagement quality.***
- ***The initial observation on Ad Classification showed that tailored advertising attracts more users to subscribe but doesn't guarantee maintaining them.***
- ***Languages other than English showed a higher conversion rates, but English successfuly managed to maintain subscribers.***
- ***Language alignment strongly influences both user engagement and continued interaction.***
- ***Increased exposure and campaign intensity could positively influence user conversions over the following days.***
- ***Younger audiences (under 30) are more likely to engage and remain retained after conversion, while engagement among users above 30 is weaker. Except for ages 30-36 & 
above 55 years who tend to retain in a high range despite their lower conversion rate.***
### $\color{#454775}{2-}$ **The impact of repeating the ad for users on Conversion & Retention Rates:** 
### $\color{#454775}{Observations:}$
- **Users who saw the ad multiple times (22.93%) showed stronger performance:**
  - Conversion Rate: 17.83%
  - Retention Rate: 70.19%
  - _Repeated exposure appears to reinforce engagement and increase the likelihood of both subscribing and staying subscribed._
- **Users exposed to the ad only once (77.07%) demonstrated moderate results:**
  - Conversion Rate: 11.58%
  - Retention Rate: 64.01%
  - _Single exposure still produced meaningful conversions but noticeably lower than multi-exposure users._
### $\color{#454775}{Key}$ $\color{#454775}{Findings:}$
- ***Multi-touch ad exposure significantly improves both conversion and retention outcomes, as users who receive repeated exposure are more likely to subscribe and continue using the service.***
- ***Single-touch exposure produces moderate impact, but not as strong as repeated exposure, this suggests that user reinforcement plays an essential role in both conversion behavior and long-term retention.***
## $\color{#454775}{b)}$ $\color{#454775}{Demographic}$ $\color{#454775}{Influence:}$
### $\color{#454775}{1-}$ **The Impcat of Age Groups & Language on Conversion Rates:** 
### $\color{#454775}{Observations:}$
#### $\color{#454775}{-}$ _Arabic:_
- Arabic shows very high conversion rates across most age groups (0–18, 19–24, 24–30).
- Performance decreases slightly for older users (45–55 and 55+), but still remains higher than English in most cases.
#### $\color{#454775}{-}$ _English:_
- Ages under 30 show moderate conversion performance, but still lower compared to Arabic and German.
- Ages 30 and above exhibit very low conversion rates, dropping to nearly 6–7% in multiple age groups.
- _English displays the most consistent decline with age._
#### $\color{#454775}{-}$ _German:_
- German shows relatively high conversion rates across all age groups, with most values around 70%–80%.
- Even older age groups maintain strong conversion performance (e.g., 30–36 at 50% and 36–45 at 80%).
- _German is the most stable language in terms of performance across ages._
#### $\color{#454775}{-}$ _Spanish:_
- Spanish shows mixed performance:
  - High values for 0–18, 30–36, and 55+.
  - Low for 19–24 and 24–30.
  - _This indicates inconsistent response depending on age group._
### $\color{#454775}{Key}$ $\color{#454775}{Findings:}$
- ***Arabic and German outperform other languages overall, showing strong conversion rates across most age groups.***
- ***English has the weakest performance, especially among users aged 30 and above, where conversion rates drop significantly.***
- ***Spanish shows age-dependent performance, with high conversion rates in some age brackets but very low in others, indicating uneven responsiveness.***
- ***German displays the highest stability, maintaining good conversion rates across almost all age segments, making it the most consistently effective language.***
- ***Arabic performs exceptionally well among younger age groups, suggesting it may be a strong cultural or linguistic driver for younger audiences.***
> $\color{#454775}{Note:}$ _These patterns highlight that personalized content may need to be tailored more precisely by both language and age group to improve overall engagement. German and Arabic audiences appear highly responsive, whereas English-speaking and middle-aged Spanish-speaking audiences may require different messaging strategies to increase conversion performance._
### $\color{#454775}{2-}$ **The impact of age groups & language on Retention Rates:** 
### $\color{#454775}{Observations:}$
#### $\color{#454775}{-}$ _Arabic:_
- Retention is extremely high across all available age groups (100% in most segments), except one moderate value (66.67% for ages 45–55).
- Ages 24-45 didn't retain after subscription.
#### $\color{#454775}{-}$ _English:_
- Consistent retention across all age groups, ranging between 63%–69%.
- Very stable and uniform pattern, _suggesting English users have predictable retention behavior_.
#### $\color{#454775}{-}$ _German:_
- High Retention rates for ages below 30 fluctuates between (66.67%) and (76.47%).
- Lower retention in ages above 30, where it reached 33.33% for for ages 30-36 and remaind at 50% for ages from 36-55+.
#### $\color{#454775}{-}$ _Spanish:_
- Exceptionally high retention (100%) for younger and mid-age groups (0–36), & a drop to 60% for 55+.
- Ages 36-55 didn't retain after subscription.
#### $\color{#454775}{Key}$ $\color{#454775}{Findings:}$
- ***English users exhibit steady and predictable retention across all age groups—neither extremely high nor low—indicating consistent engagement but limited upside.***
- ***German retention varies significantly by age, suggesting demographic sensitivity and potential need for targeted messaging strategies for older audiences.***
- ***Overall, younger usersretain better in most languages—particularly Arabic and Spanish—while older age segments show more mixed or weaker retention performance, especially in German and Spanish.***
> $\color{#454775}{Note:}$ _there is a strong likelihood of bias in the Conversion & Retention Rate data due to small sample sizes, missing values, non-random exposure, and uneven group distributions. The results are informative but should be interpreted with caution, especially when comparing across languages or age groups._
### $\color{#454775}{3-}$ **The impcat of age group and marketing channels in yielding the highest Conversion Rates:** 
### $\color{#454775}{Observations:}$
- Ages 19–24 consistently exhibit the highest conversion rates across all marketing channels, within this age group, Email performs strongest (45.79%), followed by Instagram (31.23%) and Facebook (23.26%).
- Email remains the dominant conversion driver for the 0–18 and 24–30 age groups (40.66% and 44.83%, respectively), followed by Instagram and Facebook in both cases.
- Users aged 30–55+ show lower overall conversions, but Email still outperforms other channels in these segments.
- Conversion strength mainly declines noticeably across all channels after age 30, _indicating reduced responsiveness among older audiences_.
### $\color{#454775}{Key}$ $\color{#454775}{Findings:}$
- ***Email is the strongest marketing channel across all age groups, especially for users younger than 30.***
- ***Instagram and Facebook add additional value only for younger age groups, particularly those between 19–24.***
- ***Users over 30 demonstrate weaker engagement across all non-email channels, indicating limited responsiveness to social-media-based marketing.***
- ***The overall subscription pattern shows stronger conversion performance among users below 30, regardless of channel.***
### $\color{#454775}{4-}$ **Ad type & user's age impact on engagegement:** 
### $\color{#454775}{Observations:}$
- Users under 30 show a much higher tendency to subscribe, especially when exposed to personalized ads, with an average conversion rate of 28.06%, compared to 8.42% via controlled ads.
- For users aged 30 and above, conversion rates drop notably, in this segment, control ads (with an average of 9.51%) actually perform about twice as well as personalized ads (with an average of 5.15%).
- Ages 30-36 shows the highest retention rate via controlled ads 73.58% & the lowest retention rate via Personalized ads 56%.
- Retention rates are generally higher for the control variant across all age groups.
- A noticable gap between controlled and personalized ads retention rates for ages of 30 & above (with an average of 66.58% for controlled ads & 58.94%)
- Younger users (below 30) display moderate retention for both ad types, with differences between variants being 
  relatively small.
### $\color{#454775}{Key}$ $\color{#454775}{Findings:}$
- ***Personalized ads are highly effective among younger audiences (under 30), while simpler, non-personalized messages may resonate better with older users (30+).***
- ***While personalization increases conversion among younger users, it appears to reduce long-term retention, especially for older users.***
- ***A mixed strategy—personalized content for acquisition and standard communication for retention—may achieve better overall performance.***
## $\color{#454775}{c)}$ $\color{#454775}{Subscription}$ $\color{#454775}{Pattern:}$
### $\color{#454775}{1-}$  **Daily Engagement and Subscription Patterns by Marketing Channel:** 
### $\color{#454775}{Observations:}$
#### $\color{#454775}{-}$ _Overall:_
- Users tend to engage more around the middle of the month across most marketing channels — except for House Ads, which show no clear temporal pattern.
#### $\color{#454775}{-}$ _Email:_
- A significant surge in ads occurred on 15-01-2018, marking the maximum number of daily ads.
- This spike led to the highest subscription count (63), with 57 users retained — both representing the top figures across all channels.
- Subscriptions and retentions show a strong positive relationship with the number of daily users, suggesting that increased exposure directly boosted engagement and retention.
#### $\color{#454775}{-}$ _Facebook:_
- The daily user pattern is inconsistent, with engagement levels fluctuating throughout the month and peaking near the end.
- Subscriptions (17) and retentions (10) reached their maximum on 16-01-2018.
- The overall trend shows a weak-to-moderate alignment between daily user activity, subscriptions, and retentions, implying that ad exposure alone did not strongly influence conversion outcomes.
#### $\color{#454775}{-}$ _House Ads:_
- Exhibited a significantly high but irregular number of ads during the month, yet had a limited impact on subscriptions and engagement.
- Despite the heavy ad distribution, the maximum number of subscribers (21) was lower than several other channels with fewer ads.
- Shows weak consistency between daily users, subscriptions, and retentions — suggesting overexposure through House Ads did not effectively translate into user engagement.
- A noticeable decrease in the number of conversions after 10-01-2018
#### $\color{#454775}{-}$ _Instagram:_
- Engagement peaked on 17-01-2018, coinciding with the highest levels of daily users, conversions, and retentions.
- Displays a moderate-to-strong relationship between daily activity and outcomes, indicating that well-timed exposure contributed effectively to conversions and retention.
#### $\color{#454775}{-}$ _Push Notifications:_
- Reached its peak around mid-month, reflecting moderate engagement patterns.
- Shows a moderate consistency between daily users, subscriptions, and retentions, suggesting a reasonable but not strong influence of user activity on outcomes.
### $\color{#454775}{Key}$ $\color{#454775}{Findings:}$
- ***Email & Instagram $\color{#454775}{→}$ The change in daily users contributed significantly to higher subscription and retention rates.***
- ***Facebook & Push $\color{#454775}{→}$ Daily user fluctuations had a moderate influence on subscriptions and retention.***
- ***House Ads $\color{#454775}{→}$ Should be reconsidered due to their weak and inconsistent impact on engagement, subscriptions, and retention despite extensive ad distribution.***
### $\color{#454775}{2-}$  **Daily Engagement and Subscription Patterns by Age Groups:** 
### $\color{#454775}{Observations:}$
- The daily user patterns across all age groups were generally similar, with a preference for distributing more ads to users under 30.
- Daily user counts for all age groups peaked on 15-01-2018, likely influenced by the large email campaign distributed on that day.
- Conversion and retention peaks for all age groups occurred between 15 and 17 January.
- During the first half of the month, conversions and retentions showed weak consistency among age groups 0–18, 24–30, 30–36, and 55+, while the remaining groups exhibited moderate to weak consistency.
- In the second half of the month, a noticeable change was observed, as age groups 0–18 and 19–24 showed moderate consistency, while other age groups demonstrated weak to moderate consistency.
### $\color{#454775}{Key}$ $\color{#454775}{Findings:}$
- ***targeted campaigns toward younger audiences may yield better subscription and retention outcomes, where Younger users (below 30) showed stronger and more consistent responses to ads, especially after mid-January, while older groups displayed weaker consistency overall.***
- ***User engagement peaked mid-month, mainly driven by the email campaign.***
### $\color{#454775}{3-}$  **Engagement and Subscription Patterns within Weekdays:** 
### $\color{#454775}{Observations:}$
#### $\color{#454775}{-}$ _Email:_
- Reached its peak engagement on Monday.
- The pattern, except for Monday, is mostly identical — where daily users ≈ converted ≈ retained, showing high consistency.
- Another noticeable peak occurred on Tuesday, where conversions nearly matched Monday’s levels.
- The day of ad serving is strongly aligned with the amount of conversions, indicating a clear positive response pattern.
#### $\color{#454775}{-}$ _Facebook:_
- A large number of ads distributed throughout the week resulted in relatively low conversions.
- Engagement peaked midweek (Wednesday, 314 users) and again at the week’s start (Monday), yet conversions peaked on Tuesday (43).
- The alignment between ad serving and conversions is weak to moderate, suggesting that timing alone doesn’t fully explain engagement outcomes.
#### $\color{#454775}{-}$ _House Ads:_
- The volume of ads launched during the week showed minimal impact on conversions.
- Two engagement peaks were recorded on Monday (Max = 799) and Tuesday, while conversions peaked on Wednesday.
- The match between ad serving and conversions is weak, implying that ad timing or targeting may not be optimized.
#### $\color{#454775}{-}$ _Instagram:_
- A large volume of ads distributed through the week was met with moderate conversions.
- The highest peak occurred on Wednesday, aligning with the highest conversions, followed by Monday, which also had strong conversion performance.
- The day of ad serving is strongly aligned with conversions, indicating effective timing and channel performance.
#### $\color{#454775}{-}$ _Push Notifications:_
- Two engagement peaks were observed — on Wednesday (highest: 171 users) and Monday.
- Conversions peaked on Tuesday (19 subscribers), followed by Wednesday.
- The match between ad serving and conversions is weak to moderate, reflecting partial effectiveness in timing strategy.
### $\color{#454775}{Key}$ $\color{#454775}{Findings:}$
- ***Ads were mostly launched between Monday and Wednesday, with conversions largely occurring on these same days — though not always perfectly aligned.***
- ***Email and Instagram demonstrate strong synchronization between engagement and conversions, suggesting well-timed and effective campaigns.***
- ***Facebook, House Ads, and Push channels show weaker alignment, indicating that ad timing or targeting strategies might require adjustment.***
- ***To improve performance, future ad launches should focus on days with historically higher conversion activity, such as Tuesday and Wednesday, optimizing both timing and audience reach.***
## $\color{#454775}{c)}$ $\color{#454775}{House}$ $\color{#454775}{Ads}$ $\color{#454775}{In-Depth}$ $\color{#454775}{Analysis:}$
### $\color{#454775}{1-}$  **Daily conversion and mismatch occurrence via House Ads:** 
### $\color{#454775}{Observations:}$
- Starting from January 11, 2018, there was a sharp and sustained rise in mismatch occurrences, that was met by a sharp decrease in conversions.
### $\color{#454775}{Key}$ $\color{#454775}{Findings:}$
- ***This sudden increase appears to have had a strong negative impact on conversions, as the number of converted users dropped significantly after this date and remained consistently low despite continued ad activity.***
### $\color{#454775}{2-}$  **Estimating Conversion Rates Without the Language Bug:** 
### $\color{#454775}{Observations:}$
- Arabic speakers convert at about 5.1 times the rate compared to English-speakers, while German speakers convert at about 4.7 times , and Spanish-speaking users typically convert about 1.7 times.
- The Overall Estimated Lost Subscribers ≈ 26, Arabic ≈ 12, German ≈ 10, & Spanish ≈ 6.
- English served as a reliable anchor, showing steady conversion performance throughout the period.
- Across all languages, the estimated conversion rates never dropped to zero, even on days when the actual conversion rates did.
- The estimated rates remained within a realistic range, reflecting the underlying performance relationship established before the bug.
### $\color{#454775}{Key}$ $\color{#454775}{Findings:}$
- ***Had the language bug not occurred, conversion rates for non-English users would likely have followed a stable upward trend similar to English.***
- ***The sharp decline and zeros observed in the actual data after January 10 clearly reflect the disruptive effect of the mismatch, underlining the importance of correct language targeting in maintaining user engagement and conversion effectiveness.***
## $\color{#454775}{c)}$ $\color{#454775}{A/B}$ $\color{#454775}{Testing:}$
### $\color{#454775}{1-}$  *The impact of Email Personalized Ads on Conversion Rate:** 
### $\color{#454775}{Observations:}$
- Ad types were relatively even with Email Personalized Ads taking up to 51.26% & the controlled ones with 48.74%.
- The 95% Confidence Interval for the Personalization Group shows that:
   - _No Evidence of Systematic Imbalance._
   - _The Personalization Group is within the Confidence Interval Range of 47.10% & 55.43%_
- Personalization Conversion Rate ≈ 39.08% & Control Conversion Rate ≈ 28.15%. 
- The Personalization Group outperformed Control Group by 38.85%.
- The performed T-Test resulted in a P-Value ≈ 0.65% & SE ≈ -2.73.
### $\color{#454775}{Key}$ $\color{#454775}{Findings:}$
- ***This represents a substantial improvement and provides a strong statistical indication that implementing personalized emails can significantly increase conversion rates.***
- ***The difference has been confirmed as statistically significant, reinforcing confidence in the effectiveness of the personalization strategy.***
