# $\color{Red}{Analyzing}$ $\color{Red}{Marketing}$ $\color{Red}{Campaigns}$
## $\color{Red}{Overview:}$
A fake marketing dataset based on the data of an online subscription business to answer the following questions:
1. Was the campaign successful?
## $\color{Red}{Dataset}$ $\color{Red}{Description:}$
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
8. ***displayed_language*** → The language in which the ad was shown _(English, German, Arabic, Spanish)_.
9. ***preferred_language*** → The user’s preferred language _(English, German, Arabic, Spanish)_.
10. ***age_group*** → Age range of the user _(0–18, 19–24, 24–30, 30–36, 36–45, 45–55, 55+)_.
11. ***subscribing_channel*** → The channel through which the user actually subscribed _(House Ads, Email, Push, Facebook, Instagram)_.
12. ***is_retained*** → Indicates if the user continued the subscription _(True/False)_.
## $\color{Red}{Data}$ $\color{Red}{Cleaning:}$
### ***Removing Duplicates:***
### ***Adjusting Dates:***
### ***Handling Missing Values:***
### ***Adjusting Data Types:***
### ***Adding New Columns:***

## $\color{Red}{Initial}$ $\color{Red}{Investigation:}$
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
