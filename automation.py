# Description:
'''A .py file designed to collect all functions created during the project 
to reduce clutter in the original .ipynb file.'''

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


# 1- Data Assessing Functions:
# Dataset Desription - Dates:
def dates(df,cols):
    start= df[cols].astype('datetime64[ns]').min().strftime('%Y-%m-%d') 
    end= df[cols].astype('datetime64[ns]').max().strftime('%Y-%m-%d')
    return f'''
    Start: {start} 
    End  : {end}\n'''

# Dataset Desription - Unique elements in each column:
def col_uniques (df,cols):
    details = []
    for x, y in enumerate(df[cols].unique(),start=1): 
        details.append(f"  {x} - {y}")
    return "\n ".join(details)

# Create a function to identify Duplicated Values:
def duplicates (df): 
    if df.duplicated().sum() == 0: 
        result= f'The Dataset has no Duplicated Values with {df.shape[0]} Row'
    else: 
        result =  f'''
- The Dataset has {df.duplicated().sum()} Duplicated rows and their indexes are as follows:\n 
"{", ".join(map(str,df[df.duplicated()].index.to_list()))}"\n'''
    return result

# Missing Values - Create a function to identify the Null Values:
def missing(df):
    if df.isna().sum().sum() == 0: 
        result='The Dataset has no NULL Values'
    else: 
        result = f'''The Dataset has {df.isna().sum().sum()} NULL Values that are distributed as follows: '''
    return(result)  

# Missing Values - Detemining the indexes of the null values for columns:
def missing_indexs (df,cols):
    result= df[cols].isna().sum()
    details= ", ".join(map(str,df[df[cols].isna()==True].index.to_list()))
    
    return f'''
- The "{cols}" Column has {result} NULL Values and their Indexes are as follows:\n 
"{details}"\n'''

                #############################################################################################################
                #############################################################################################################

# 2- Data Cleaning: 
# Changing the dates data types:
def date_change(df,col1,col2,col3):
    df[col1]= pd.to_datetime(df[col1]) 
    df[col2]= pd.to_datetime(df[col2]) 
    df[col3]= pd.to_datetime(df[col3]) 
    check= df.loc[:,[col1,col2,col3]].info()
    return check