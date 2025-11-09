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
- ***ad_repeated:*** to check whether the user saw the ad multiple times or once.
### $\color{#454775}{7.}$ ***Mapping Values:***
Due to the way pandas stores data, in a large dataset, it can be computationally inefficient to store columns of strings. In such cases, it can speed things up to instead store these values as numbers. <br>
***converted will be as follows:***
- _True = 1_
- _False = 0_
## $\color{#454775}{Data}$ $\color{#454775}{Exploring:}$
### $\color{#454775}{-}$ ***Initial Investigation:***
### $\color{#454775}{Observations:}$
- The highest number of users who saw an ad was recorded on 15-01-2018 (Monday), with a total of 784 users. Before this peak, the average daily users were around 327, and afterward, around 284 users per day.
- Users were most engaged at the beginning of the week, particularly on Mondays (1,977 users), followed by Wednesdays (1,610) and Tuesdays (1,588).
- Users were almost evenly assigned between the control and personalization groups, suggesting that the experiment was fairly designed to compare the effectiveness of personalized ads versus standard ads.
- Approximately 10.47% of users subscribed after seeing the ad, indicating that while ads reached a wide audience, their effectiveness in driving subscriptions was limited.
- Around 97.55% of ads were displayed in English, regardless of the user’s preferred language.
- For Arabic, German, and Spanish users, the number of ads displayed in their preferred language was significantly lower than the number of users who preferred those languages.
- House Ads accounted for the largest share of language mismatches (449 occurrences, 86.68%), likely due to a technical bug affecting ad performance.
- Users aged 19–24 formed the largest segment (1,304 users, 16.56%), with nearly half of all users under 30 (47.33%), indicating that younger audiences were a primary target group.
- About 47% of users were reached through House Ads, making it the primary marketing channel.
- Facebook and Instagram together contributed around 29%, while Push and Email accounted for 9.96% and 5.65%, respectively.
### $\color{#454775}{Key}$ $\color{#454775}{Findings:}$
- ***The experiment was fairly designed to compare the effectiveness of personalized ads versus standard ads.***
- ***Social media channels (Instagram and Facebook) generated more than half of total subscriptions, highlighting their effectiveness in driving conversions.***
- ***Despite its large reach, House Ads showed relatively low subscription and retention rates, suggesting inefficiency in converting exposure into meaningful engagement.***
- ***Email marketing, though having the lowest ad distribution, showed a notable subscription pattern, indicating potential for higher efficiency if optimized.***
- ***The misalignment between ad distribution and conversion performance suggests that marketing efforts might not be fully optimized for channel effectiveness or audience targeting.***
- ***Across all channels, more than half of the subscribed users were retained, reflecting a generally strong retention performance once users converted.***
### $\color{#454775}{a)}$ ***Influence Factors:***
### $\color{#454775}{1-}$ **key factors that strongly influence user conversion and retention:** 
### $\color{#454775}{-}$ _Marketing Channels:_
### $\color{#454775}{Observations:}$
- Email demonstrates the highest performance, achieving both the top conversion rate (3.75%) and retention rate (76.47%) _-Despite its low distribution (5.65% of total Ads)_.
- Social Media Platforms had a moderate performance with a retention rate close to the overall rate (13.01%), but facebook subscribers were tending to retain more with  a retention rate of 68.30% _(2nd ranking)_.
- Push notifications rank second in retention (67.95%), despite their low distribution (9.96%) and conversion rate (7.94%), suggesting strong post-conversion engagement.
- House Ads exhibit a performance gap, with extensive ad distribution (47.08%) not translating into results — both conversion (7.40%) and retention (58.05) rates remain the lowest.
### $\color{#454775}{-}$ _Variant:_
### $\color{#454775}{Observations:}$
- Personalized ads show significantly higher conversion rate of 16.80%, _indicating that personalized messages were more effective at encouraging users to subscribe initially_.
- A Higher retention rate of was achieved by Controlled Ads 67.63%, exceeding the Personalized group (65.50%) -_Although personalization increased conversions, it did not translate into stronger long-term retention_.
### $\color{#454775}{Key}$ $\color{#454775}{Findings:}$
- ***Adopting a more strategic distribution of ads could improve the engagement quality.***
- ***The initial observation on Ad Classification showed that tailored advertising attracts more users to subscribe but doesn't guarantee maintaining them.***
