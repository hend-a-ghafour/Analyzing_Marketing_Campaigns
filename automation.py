# Description:
# A .py file designed to collect all functions created during the project to reduce clutter in the original .ipynb file, in order to avoid Typos & Bugs.

# Imported Libraries:
import pandas as pd 
import numpy as np
import math
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest
import matplotlib.pyplot as plt 
import matplotlib.ticker as mticker
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import matplotlib.patheffects as path_effects
import seaborn as sns


# Data Assessing Functions:
#==========================

# 1- Dataset Desription - Dates:
def dates(df, cols):
    start = df[cols].astype('datetime64[ns]').min().strftime('%Y-%m-%d') 
    end = df[cols].astype('datetime64[ns]').max().strftime('%Y-%m-%d')
    return f'''
    Start : {start} 
    End   : {end}\n'''

                                                #---------------------------------------------------------#

# 2- Dataset Desription - Unique elements in each column:
def col_uniques (df, cols):
    details = []
    for x, y in enumerate(df[cols].unique(), start=1): 
        details.append(f"  {x} - {y}")
    return "\n ".join(details)

                                                #---------------------------------------------------------#

# 3- Create a function to identify Duplicated Values:
def duplicates (df): 
    if df.duplicated().sum() == 0: 
        result = f'The Dataset has no Duplicated Values with {df.shape[0]} Row'
    else: 
        result = f'''
- The Dataset has {df.duplicated().sum()} Duplicated rows and their indexes are as follows:\n 
"{", ".join(map(str, df[df.duplicated()].index.to_list()))}"\n'''
    return result
                                                #---------------------------------------------------------#


# 4- Missing Values - Create a function to identify the Null Values:
def missing(df):
    if df.isna().sum().sum() == 0: 
        result ='The Dataset has no NULL Values'
    else: 
        result = f'''The Dataset has {df.isna().sum().sum()} NULL Values that are distributed as follows: '''
    return result
    
                                                #---------------------------------------------------------#


# 5- Missing Values - Detemining the indexes of the null values for columns:
def missing_indexs (df, cols):
    result = df[cols].isna().sum()
    details = ", ".join(map(str,df[df[cols].isna()==True].index.to_list()))
    
    return f'''
- The "{cols}" Column has {result} NULL Values and their Indexes are as follows:\n 
"{details}"\n'''

                
                #############################################################################################################
                #############################################################################################################

# Data Cleaning Function: 
#========================

# Changing the dates data types:
def date_change(df, col1, col2, col3):
    df[col1] = pd.to_datetime(df[col1]) 
    df[col2] = pd.to_datetime(df[col2]) 
    df[col3] = pd.to_datetime(df[col3]) 
    check = df.loc[:,[col1,col2,col3]].info()
    return check

                
                #############################################################################################################
                #############################################################################################################

# Data Exploring functions: 
#==========================

# Initial Investigation:
#-----------------------

# a) Calculations: 

# 1- Building a Function for counting users: 
def counting (df, col_name):
    nums = df.groupby(col_name).user_id.count().reset_index().rename(columns = {'user_id': "# Users"})
    nums.columns = [x.title().replace('_',' ') for x in nums.columns]
    nums = nums.set_index(nums.columns[0])
    nums['Percentage'] = nums["# Users"]/nums["# Users"].sum()
    return nums 
    
                                                #---------------------------------------------------------#


# 2- Building a Function for unique users: 
def uniques (df,col_name):
    distinct = df.groupby(col_name).user_id.nunique().reset_index()
    distinct['Percentage'] = distinct.user_id/distinct.user_id.sum()
    return distinct 

                #############################################################################################################

# b) Visualization: 
    
# 1- Building a Function for Line Plots: 
def line_plot(df, col_name):
    # Data
    x = df.index.astype('str').to_list()
    y = df[col_name]

    # Creating the Line Chart
    fig,ax = plt.subplots(figsize = (8, 6))
    ax.plot(x, y, color = '#805D87', marker = 'H', alpha=.8)

    # Customizing Chart
    plt.title('', fontsize = 14, color = '#454775')

    plt.xlabel(df.index.name, fontsize = 12, color = '#313E4C')
    plt.xticks(rotation = 90, fontsize = 8, color = '#415366')

    plt.ylabel(col_name, fontsize = 12, color = '#313E4C')
    plt.yticks(fontsize = 8, color = '#415366')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    for spine in ax.spines.values():
        spine.set_linewidth(1.2)
        spine.set_edgecolor('#415366')
        spine.set_alpha(.8)
    
    # Data Annotation with values
    for i, v in enumerate(y):
      plt.text(i, v+15, f"{v:.0f}", ha = 'center', va = 'center', fontsize = 7, color = '#313E4C')
                
                                                #---------------------------------------------------------#

# 2-Building a Function for Horizontal Bar Plots: 
def hbar_plot(df, col_name):
    # Data
    x = df.index.to_list()
    y = df[col_name]

    # Defining colors based on performance
    colors = ['#805D87' if n == y.max() else '#94D1E7' for n in y] 

    # Creating the chart
    fig, ax = plt.subplots(figsize = (5, 5))
    ax.barh(x,y,alpha=.8,color=colors)
    
    # Customizing the Chart
    plt.gca().invert_yaxis()
    plt.title('', fontsize = 12, color = '#454775')

    plt.xlabel(col_name, fontsize = 10, color = '#313E4C')
    plt.xticks(fontsize = 8, color = '#415366')

    plt.ylabel(df.index.name, fontsize = 10, color = '#313E4C')
    plt.yticks(fontsize = 8, color = '#415366')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    for spine in ax.spines.values():
        spine.set_linewidth(1.2)
        spine.set_edgecolor('#415366')
        spine.set_alpha(.8) 
        
    # Annotating bars with values
    for i,v in enumerate(y):
        plt.text(v, i, v, va = 'center', ha = 'left', fontsize = 8, color = '#313E4C')

                                                #---------------------------------------------------------#

# 3- Building a Function for Pie Plots: 
def pie_plot (df, col_name):
    # Defining colors based on performance
    colors = ['#805D87' if x == df[col_name].max() else '#94D1E7' for x in df[col_name]]
    
    #Data
    labels=df.index.str.capitalize().to_list()  
    size = 0.45
    
    # Creating the Chart
    plt.subplots(figsize = (3.5,3.5))
    wedges, texts, autotexts=plt.pie(df[col_name], radius=1, colors= colors,labels = labels,autopct='%1.2f%%',pctdistance=.8,
                                 textprops={'fontsize': 10,'color':'#313E4C'}, wedgeprops=dict(width=size, edgecolor='w'),startangle=100)
    
    # Customizing Chart
    for w in wedges:
        w.set_alpha(0.8)  

    plt.title('',fontsize=12,color='#454775')

                                                #---------------------------------------------------------#

# 4- Building a Function for Horizontal stacked Plots: 
def stackedh_plot(df,col_name,col2_name):
    # Data
    x=df.index.to_list()
    y=df[col_name]
    z=df[col2_name]

    # Creating the Chart
    fig,ax= plt.subplots(figsize=(5,5))
    bin_size=.5
    ax.barh(x,y, label=col_name,color='#805D87',alpha=.8)
    ax.barh(x,z,bin_size,label=col2_name, color='#94D1E7',alpha=.8)

    # Chart Customization
    plt.title('', fontsize=12,color='#454775')

    plt.xlabel('', fontsize=10,color='#313E4C')
    plt.xticks(fontsize=8,color='#415366')

    plt.ylabel(df.index.name, fontsize=10,color='#313E4C')
    plt.yticks(fontsize=8,color='#415366')

    plt.legend(fontsize=9,labelcolor='#313E4C',loc='center right',fancybox=True, shadow=True)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    for spine in ax.spines.values():
        spine.set_linewidth(1.2)
        spine.set_edgecolor('#415366')
        spine.set_alpha(.8) 

                                                #---------------------------------------------------------#

