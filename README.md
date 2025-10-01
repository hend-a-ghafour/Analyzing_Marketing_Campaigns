# $\color{Red}{Analyzing}$ $\color{Red}{Marketing}$ $\color{Red}{Campaigns}$
## $\color{Red}{Overview:}$
A fake marketing dataset based on the data of an online subscription business
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

