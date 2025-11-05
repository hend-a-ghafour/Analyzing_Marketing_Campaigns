# $\color{#454775}{Analyzing}$ $\color{#454775}{Marketing}$ $\color{#454775}{Campaigns}$
## $\color{#454775}{Overview:}$
A fake marketing dataset based on the data of an online subscription business to investigate the following aspects:
- The key factors that strongly influence user conversion and retention.  
- The impact of repeated ads -if any- for a specific user on subscription patterns.  
- The influence of demographic factors on achieving higher conversion rates.  
- Subscription trends and patterns over a specific time period.  
- Investigating the best- and worst-performing marketing channels.  
## $\color{#454775}{Dataset}$ $\color{#454775}{Description:}$
- ***user_id*** $\color{#454775}{→}$ An identifier for each user _(7309 user)_.
  > $\color{#454775}{Note:}$ _A user may use more than one platform and engage in more than one day._
- ***date_served*** $\color{#454775}{→}$ The date when the ad was shown to the user _(01-01-2018 : 31-01-2018)_.
- ***date_subscribed*** $\color{#454775}{→}$ The date when the user subscribed after seeing the ad _(01-01-2018 : 31-01-2018)_.
- ***date_cancelled*** $\color{#454775}{→}$ The date when the user cancelled their subscription _(05-01-2018 : 09-05-2018)_.
- ***marketing_channel*** $\color{#454775}{→}$ The source through which the ad was delivered _(House Ads, Push, Facebook, Instagram, & Email)_.
- ***variant*** $\color{#454775}{→}$ Type of experiment group the user was placed in _(personalization or control)_.
  > $\color{#454775}{Note:}$
  > - _**Personalization (variant = personalization)** $\color{#454775}{→}$ The user was shown a personalized version of the ad, meaning the ad content was tailored to their profile, preferences, or past behavior (**e.g.,** language choice, recommendations, or custom offers)._
  > - _**Control (variant = control)** $\color{#454775}{→}$ The user was shown a generic version of the ad, without personalization. This group is used as a baseline to compare results and measure how effective personalization is._
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
   - ***Users may be exposed to the same ad multiple times, with engagement frequencies ranging from 1 to 12 occurrences.***
   - ***After reviewing a sample of user engagements:***
     - **A near-duplicated pattern was noticed for users' multiple exposures**
     - **One user _(ID: a100000882)_ exhibited 12 ad exposures:**
       - Within these 12 records, several entries appeared repeated, with some columns identical while others showed slight variations.
       - **For instance,** this user converted in 4 records — two under the personalized variant (served on January 14) and two under the control variant (served on January 18). The subscription dates associated with these conversions were either January 14 or January 18, suggesting minor inconsistencies or multiple conversions logged for the same user within a short period.
     - **A similar pattern was observed for another sample user with 10 ad exposures _(ID: a100000878)_:**
       - The user interacted primarily through House Ads and Email channels.
       - Multiple records showed identical values across most columns, with slight variations in date_served and date_subscribed.
       - The user converted multiple times on the same channel _(Email, control variant)_ — an unusual pattern since a user typically subscribes only once.
       - These repeated or inconsistent entries suggest potential data duplication or logging issues, where multiple impressions and conversions might have been recorded for a single actual event.
     - **For a user with 8 recorded engagements _(User ID: a100000875)_, several inconsistencies were observed:**
       - Despite being recorded as the same user, their age group alternated between 19–24 years and 45–55 years, indicating a data entry or merge error.
       - The user converted four times.
       - Subscription dates (1/7/18 and 1/11/18) were reused across records, often paired with inconsistent cancellation statuses.
       - Some records show the user as retained, while others mark them as canceled, even within the same channel and week.
       - This record highlights duplicated and conflicting user engagement logs, likely resulting from data integration or tracking issues.
     - **Out of the 13 users who saw the ad 5 times, only 8 converted.**