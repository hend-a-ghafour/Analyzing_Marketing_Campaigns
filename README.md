# $\color{#454775}{Analyzing}$ $\color{#454775}{Marketing}$ $\color{#454775}{Campaigns}$
## $\color{#454775}{Overview:}$
A fake marketing dataset based on the data of an online subscription business to investigate the following aspects:
- ***Influence Factors:***
    1. What factors most strongly influence user conversion and retention rates?
    2. Is there evidence that multi-touch exposure (users seeing multiple ads) improves conversion or retention rates?
- ***Audience & Channel Interaction:***
    3. Which combinations of age group and marketing channel yield the highest conversion rates?
    4. How do ad type and user age interact to influence conversion and retention rates?  
- ***Subscription Pattern:***
    5. How daily subscription counts differ across marketing channels?
    6. What patterns emerge in daily subscription activity among different age groups??
## $\color{#454775}{Dataset}$ $\color{#454775}{Description:}$
1. ***user_id*** → An identifier for each user _(7309 user)_.
   >***Note:*** _A user may use more than one platform and engage in more than one day_
2. ***date_served*** → The date when the ad was shown to the user _(01-01-2018 : 31-01-2018)_.
3. ***date_subscribed*** → The date when the user subscribed after seeing the ad _(01-01-2018 : 31-01-2018)_.
4. ***date_cancelled*** → The date when the user cancelled their subscription _(05-01-2018 : 09-05-2018)_.
5. ***marketing_channel*** → The source through which the ad was delivered _(House Ads, Push, Facebook, Instagram, Email)_.
6. ***variant*** → Type of experiment group the user was placed in _(personalization or control)_.
   >***Note:***
   > - ***Personalization (variant = personalization)*** → _The user was shown a personalized version of the ad, meaning the ad content was tailored to their profile, preferences, or past behavior (**e.g.,** language choice, recommendations, or custom offers)._
   > - ***Control (variant = control)*** → _The user was shown a generic version of the ad, without personalization. This group is used as a baseline to compare results and measure how effective personalization is._
   > - 👉 ***In short:***
   >    - _Personalization = test group (customized ads)_
   >    - _Control = baseline group (standard ads)_

7. ***converted*** → Indicates if the user subscribed after seeing the ad _(True/False)_.
8. ***language_displayed*** → The language in which the ad was shown _(English, German, Arabic, Spanish)_.
9. ***preferred_language*** → The user’s preferred language _(English, German, Arabic, Spanish)_.
10. ***age_group*** → Age range of the user _(0–18, 19–24, 24–30, 30–36, 36–45, 45–55, 55+)_.
11. ***subscribing_channel*** → The channel through which the user actually subscribed _(House Ads, Email, Push, Facebook, Instagram)_.
12. ***is_retained*** → Indicates if the user continued the subscription _(True/False)_.
## $\color{#454775}{Data}$ $\color{#454775}{Cleaning:}$
### ***Removing Duplicates:***
37 duplicated raws that have been removed
### ***Adjusting Dates:***
from str to datetime
### ***Handling Missing Values:***
### ***Adjusting Data Types:***
### ***Adding New Columns:***

## $\color{#454775}{Data}$ $\color{#454775}{Exploring:}$
### ***Initial Investigation:***
- The first half of the month sticks around 300 users/day. The peak was in the middle of the month "15/1/2018" 
  with number of users = 767 "on Monday".<br>
  ***This may be because we sent out a big marketing email, which reached many users who are not daily visitors of the site***

- Users were mostly engaged at the week start "on Monday"

- Nearly half of the users were reached through House Ads, making it the primary marketing channel. Social media (Instagram and Facebook combined) also plays a major role, accounting for over one-third of users, while Push and Email contribute relatively smaller shares.

- The dataset shows a nearly even distribution between control and personalization groups.<br>
  ***Which suggests that the experiment was designed to fairly compare the effectiveness of personalized ads versus standard ads.***

- The conversion rate is relatively low, with only about 11% of users subscribing after seeing an ad.<br>
  ***This suggests that while ads are reaching a wide audience, their effectiveness in driving subscriptions is limited.***

- The data indicates that English is used as the default display language, even when the user’s preferred language is different.<br>
  ***This inconsistency—particularly for Arabic, German, and Spanish—may negatively impact user engagement with the ads.***

- Users aged 19–24 represent the largest single segment (16.56%). More broadly, nearly half of all users are under 30.<br>
  ***Indicating that younger audiences are a primary group of interest for marketing efforts.***

- More than half of the subscriptions came from Instagram and Facebook, highlighting social media as the most effective subscribing channels. House Ads, Email, and Push play smaller roles.<br>
  ***This imbalance raises questions about whether ad distribution is aligned with channel effectiveness and audience targeting.***

- Despite its strong performance in attracting subscribers, House Ads ranked fourth in retention rate, with 55.93% of its subscribers retained.

- Across all channels, more than half of subscribed users were retained.\n
  ***Indicating a generally good retention performance overall.***

- Social media channels not only attract the most users but also maintain relatively high retention rates (~70%).
  ***Suggesting both strong acquisition and engagement potential.***
### $\color{#454775}{Q1:}$ ***What factors most strongly influence user conversion and retention rates?***
#### Key Findings:
- ***Conversion Rate*** = 13.92% , and ***Retention Rate*** = 67.09%.
- ***Marketing Channels:***
    - **House Ads**, exhibit a performance gap, with extensive ad distribution ***(≈47%)***, not translating into results — both conversion (7.51%) and 
  retention (58.05%) rates remain the lowest.<br>
      ***This indicates that despite being the most widely used marketing channel, House Ads are the least effective in driving both subscriptions and long-term retention.***
    - **Email**,emonstrates the highest performance, achieving both the top conversion rate (29.11%) and retention rate (77.01%).
    - **Push notifications** rank second in retention (70.13%), despite their low distribution and conversion rates, suggesting strong post-conversion engagement.
- ***Variant Classifications:***
  - Despite being almost evenly distributed across marketing channels, **personalized ads** successfully encouraged more users to subscribe compared to **standard (control) ads**
      - **Personalized ads** achieved a higher *conversion rate* (16.80%) than both the control group (9.29%) and the overall conversion rate (13.92%).
      - **Personalized ads** not only converted more users but also achieved a higher retention rate (66.23%) compared to the control group (62.79%).<br>
      ***This indicates that users acquired through personalized ads are more likely to stay subscribed, reinforcing the effectiveness of personalization in both conversion and retention.***
- ***Displayed Language:***
  - Non-English languages show notably higher conversion rates compared to English.
  - German (71.62%) & Arabic (50%) conversion rates  are significantly higher than the overall conversion rate (13.92%)
  - German and English users show the highest retention rates (66.04% & 64.79%), both aligning closely with or slightly above the overall retention rate (64.53%).
  - While Arabic and Spanish users have moderate retention rates (58.33% & 54.17%), these are below the overall average.
- ***Language sataus:***
  - Users are more likely to subscribe when the ad language matches their preferred language:
    - Achieving a conversion rate of 14.16%, which is above the overall conversion rate (13.92%) compared to 6.70% for the Non-matching Languages.<br>
      ***This highlights the importance of language alignment and localization when distributing ads to maximize engagement and conversions.***
    - Retention rate for matched languages (64.98%) is significantly higher than that of non-matched languages (48.15%), mirroring the conversion rate trend.
    - The matched-language retention rate (64.98%) is also very close to the overall retention rate (67.09%).<br>
      ***reinforcing the importance of language consistency in maintaining user engagement.***
- ***Age Groups:***
   - Ages 19–24 show the highest conversion rate (23.24%) and retention rate (68.98%), making this the most responsive and loyal segment.
   - Ages 24–30 and 0–18 also perform well, with relatively strong conversion and retention rates above 15%.
  - Older age groups (30+) show significantly lower conversion rates (~7%) and slightly lower retention rates, except for 55+, which shows a better retention (67.11%) despite low conversion.
- ***Date Served:***
  - The 16th and 17th of January recorded the highest conversion rates at 25.52% and 21.95%, respectively.<br>
    ***This spike aligns with the peak in ad views on January 15 (786 Views).***
  - The retention rates across different dates show no clear or consistent pattern.  
#### Insights:  
- A rising concerns about the efficiency of Ad distribution, suggesting that reallocating ad resources toward higher-performing channels (like Email or Instagram) could improve overall results.
- Increase investment in Email campaigns, as this channel delivers the highest conversion and retention performance.
- Leverage Push notifications more strategically — their strong retention suggests they effectively keep users engaged post-subscription.
- personalization positively influences user engagement and conversion, reinforcing the value of tailoring ad content to user preferences.
- Personalized ads outperform control ads in both conversion and retention, showing stronger user engagement overall.
- localized ads successfully attract users, but sustaining their engagement may depend on post-subscription experience and language consistency.
- Understanding the ad plays a major role in driving user engagement — ads that are clearly understood (e.g., those matching the user’s preferred language) show significantly higher conversion and retention rates _(14.16% & 64.89% respectively)_.
- Younger audiences (under 30) are more likely to engage and remain retained after conversion, while engagement among users above 30 is weaker.
- Ages above 55, While less likely to convert, exhibit better loyalty once they do.
- Increased exposure and campaign intensity could positively influence user conversions over the following days.
- There is no strong or consistent relationship between the date served and the retention rate, suggesting that ad timing alone does not significantly influence user retention.
### $\color{#454775}{Q2:}$ ***Is there evidence that multi-touch exposure (users seeing multiple ads) improves conversion or retention rates?***
#### Key Findings:
- Users who saw multiple ads converted ~3x more often , and were slightly more likely to be retained afterward.
- Multi-touch exposure conversion rate (25.53%) is nearly double the overall conversion rate (13.92%).
#### Insights: 
-multi-touch exposure improves conversion performance, with a modest positive impact on retention.

