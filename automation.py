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
def dates (df, cols):
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
def missing (df):
    if df.isna().sum().sum() == 0: 
        result = 'The Dataset has no NULL Values'
    else: 
        result = f'''The Dataset has {df.isna().sum().sum()} NULL Values that are distributed as follows: '''
    return result
    
                                                #---------------------------------------------------------#


# 5- Missing Values - Detemining the indexes of the null values for columns:
def missing_indexs (df, cols):
    result = df[cols].isna().sum()
    details = ", ".join(map(str, df[df[cols].isna() == True].index.to_list()))
    
    return f'''
- The "{cols}" Column has {result} NULL Values and their Indexes are as follows:\n 
"{details}"\n'''

                
                #############################################################################################################
                #############################################################################################################

# Data Cleaning Function: 
#========================

# Changing the dates data types:
def date_change (df, col1, col2, col3):
    df[col1] = pd.to_datetime(df[col1]) 
    df[col2] = pd.to_datetime(df[col2]) 
    df[col3] = pd.to_datetime(df[col3]) 
    check = df.loc[:, [col1, col2, col3]].info()
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
    nums = df.groupby(col_name).user_id.count().reset_index().rename(columns = {'user_id' : "# Users"})
    nums.columns = [x.title().replace('_', ' ') for x in nums.columns]
    nums = nums.set_index(nums.columns[0])
    nums['Percentage'] = nums["# Users"] / nums["# Users"].sum()
    return nums 
    
                                                #---------------------------------------------------------#


# 2- Building a Function for unique users: 
def uniques (df, col_name):
    distinct = df.groupby(col_name).user_id.nunique().reset_index().rename(columns = {'user_id' : "# Users"})
    distinct.columns = [x.title().replace('_', ' ') for x in distinct.columns]
    distinct = distinct.set_index(distinct.columns[0])
    distinct['Percentage'] = distinct["# Users"]/distinct["# Users"].sum()
    return distinct 

                                                #=========================================================#

# b) Visualization: 
    
# 1- Building a Function for Line Plots: 
def line_plot (df, col_name):
    # Data
    x = df.index.astype('str').to_list()
    y = df[col_name]

    # Creating the Line Chart
    fig, ax = plt.subplots(figsize = (8 , 6))
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
def hbar_plot (df, col_name):
    # Data
    x = df.index.to_list()
    y = df[col_name]

    # Defining colors based on performance
    colors = ['#805D87' if n == y.max() else '#94D1E7' for n in y] 

    # Creating the chart
    fig, ax = plt.subplots(figsize = (5 , 5))
    ax.barh(x, y, alpha = .8, color = colors)
    
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
    for i, v in enumerate(y):
        plt.text(v, i, v, va = 'center', ha = 'left', fontsize = 8, color = '#313E4C')

                                                #---------------------------------------------------------#

# 3- Building a Function for Pie Plots: 
def pie_plot (df, col_name):
    # Defining colors based on performance
    colors = ['#805D87' if x == df[col_name].max() else '#94D1E7' for x in df[col_name]]
    
    #Data
    labels = df.index.str.title().to_list()  
    size = 0.45
    
    # Creating the Chart
    plt.subplots(figsize = (3.5 , 3.5))
    wedges, texts, autotexts=plt.pie(df[col_name], radius = 1, colors = colors, labels = labels, autopct = '%1.2f%%', pctdistance = .8,
                                     textprops = {'fontsize' : 10, 'color' : '#313E4C'}, wedgeprops = dict(width = size, edgecolor = 'w'), 
                                     startangle = 100)
    
    # Customizing Chart
    for w in wedges:
        w.set_alpha(0.8)  

    plt.title('', fontsize = 12, color = '#454775')

                                                #---------------------------------------------------------#

# 4- Building a Function for Horizontal stacked Plots: 
def stackedh_plot (df, col_name, col2_name):
    # Data
    x = df.index.to_list()
    y = df[col_name]
    z = df[col2_name]

    # Creating the Chart
    fig, ax = plt.subplots(figsize=(5 , 5))
    bin_size=.5
    ax.barh(x, y, label = col_name, color = '#805D87', alpha = .8)
    ax.barh(x, z, bin_size, label = col2_name, color = '#94D1E7',alpha = .8)

    # Chart Customization
    plt.title('', fontsize = 12, color = '#454775')

    plt.xlabel('', fontsize = 10, color = '#313E4C')
    plt.xticks(fontsize=8, color = '#415366')

    plt.ylabel(df.index.name, fontsize = 10, color = '#313E4C')
    plt.yticks(fontsize = 8, color = '#415366')

    plt.legend(fontsize = 9, labelcolor = '#313E4C', loc = 'center right', fancybox = True, shadow = True)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    for spine in ax.spines.values():
        spine.set_linewidth(1.2)
        spine.set_edgecolor('#415366')
        spine.set_alpha(.8) 


                #############################################################################################################

# Influence Factors:
#-------------------

# a) Calculations: 

# Comparison between Conversion & Retention Rates function:
def comparison (df, df2, df3, cols, target): 
    first = df.groupby(cols)[target].nunique().reset_index()
    second = df2.groupby(cols)[target].nunique().reset_index()
    result1 = first.merge(second,on= cols)
    result1['Conversion Rate'] = round(result1.iloc[:, -1] / result1.iloc[:, -2], 4)
    
    third = df3.groupby(cols)[target].nunique().reset_index()
    result2 = second.merge(third, on = cols)
    result2['Retention Rate'] = round(result2.iloc[:, -1] / result2.iloc[:, -2], 4)
    
    required_cols = list(cols) + ['Conversion Rate', 'Retention Rate']
    
    final_result = result1.merge(result2, on = cols).loc[:, required_cols]
    final_result.columns = [x.replace('_', ' ').title() if x in cols else x for x in final_result.columns]
    final_result = final_result.sort_values('Conversion Rate', ascending = False).set_index(final_result.columns[0])
    return final_result




                                                #=========================================================#

# b) Visualization: 

# 1- Combo Chart function:
def combo (df, col1, col2, rate1, rate2): 
    # Data
    x = df.index.to_list()
    y = df[col1]
    z = df[col2]

    # Defining colors based on performance
    colors1 = ['#805D87' if n > rate1 else '#94D1E7' for n in y]
    colors2 = ['#454775' if m > rate2 else '#EA9FBB' for m in z]

    # Creating the chart 
    fig, ax1 = plt.subplots(figsize=(5 , 5))

    # 1- Bar Plot 
    ax1.bar(x, y, width = .5, alpha = .8, color = colors1)

    # 2- Line & Scatter Plots
    ax2 = ax1.twinx()
    ax2.plot(x, z, ls = 'dotted', color = '#51687F', alpha = .5)
    ax2.scatter(x, z , color = colors2)

    # Customizing the chart
    plt.title('', fontsize = 12, color = '#454775')

    ax1.set_xlabel('\n' + df.index.name + '\n', fontsize = 10, color = '#313E4C')
    ax1.tick_params(axis='x', labelcolor = '#415366', labelsize = 8) 

    ax1.set_ylabel('\n' + col1 + '\n', fontsize = 10, color = '#313E4C')
    ax1.tick_params(axis='y', labelcolor = '#415366', labelsize = 8)
    ax1.yaxis.set_major_formatter(mticker.PercentFormatter(1, decimals = False)) 
    ax1.set_ylim(0) 
    
    ax2.set_ylabel('\n' + col2 + '\n', fontsize = 10, color = '#313E4C')
    ax2.tick_params(axis='y', labelcolor = '#415366', labelsize = 8)
    ax2.yaxis.set_major_formatter(mticker.PercentFormatter(1, decimals = False)) 
    ax2.set_ylim(0,.8)

    ax1.spines['top'].set_visible(False)
    ax2.spines['top'].set_visible(False)
    for spine in ax1.spines.values():
        spine.set_linewidth(1.2)
        spine.set_edgecolor('#415366')
        spine.set_alpha(.8)
    for spine in ax2.spines.values():
        spine.set_linewidth(1.2)
        spine.set_edgecolor('#415366')
        spine.set_alpha(.8) 
         
    # Legend
    above_cr = mpatches.Patch(color = '#805D87', label = col1 + f' > {rate1:.2%}')
    below_cr = mpatches.Patch(color = '#94D1E7', label = col1 + f' ≤ {rate1:.2%}')
    above_rr = mlines.Line2D([], [], color = '#454775', marker = 'o', linestyle = 'None', label = col2 + f' > {rate2:.2%}')
    below_rr = mlines.Line2D([], [], color = '#EA9FBB', marker = 'o', linestyle = 'None', label = col2 + f' ≤ {rate2:.2%}')
    plt.legend(handles = [above_cr, below_cr, above_rr, below_rr], fontsize = 8, labelcolor = '#313E4C', loc = 'upper right',
                bbox_to_anchor = (1.6, 1), alignment = 'center', fancybox = True, shadow = True)


                                                #---------------------------------------------------------#


# 2- Bar Plot function:
def bars (df, col1, col2, rate):
    # Data
    x = df[col1].astype('str').apply(lambda x: x.title()).to_list()
    y = df[col2]

    # Defining colors based on performance
    colors = ['#805D87' if n > rate else '#94D1E7' for n in y] 

    # Creating the chart
    fig, ax = plt.subplots(figsize = (4.5 , 4.5))
    ax.bar(x, y, width = .5, color = colors, alpha = .8)
    ax.axhline(y = rate, color = '#454775', linestyle = '--', linewidth = 1, label = 'Overall ' + col2, alpha = .5)

    # Customizing the chart
    plt.title('', fontsize = 12, color = '#454775')

    plt.xlabel('\n' + col1 + '\n', fontsize = 10, color = '#313E4C')
    ax.tick_params(axis = 'x', color = '#415366', labelcolor = '#415366', labelsize = 8)  
    plt.ylabel('\n' + col2 + '\n', fontsize = 10, color = '#313E4C')
    ax.tick_params(axis = 'y', color = '#415366', labelcolor = '#415366', labelsize = 8)  

    plt.legend(fontsize = 9, labelcolor = '#313E4C', loc = 'best', alignment = 'center', fancybox = True, shadow = True)
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    for spine in ax.spines.values():
        spine.set_linewidth(1.2)
        spine.set_edgecolor('#415366')
        spine.set_alpha(.8)

    # Annotating chart with values
    plt.text(x[-1], rate, f'\u2003\u2003\u2003{rate:.2%}', ha = 'left', va = 'bottom', fontsize = 9, color = '#313E4C', 
             fontstyle = 'italic', weight = 'semibold')

    for i,v in enumerate(y):
        plt.text(i, v + .005, f'{v:.2%}', va = 'bottom', ha = 'center', fontsize = 8, color = '#313E4C')


                                                #---------------------------------------------------------#


# 3- Horizontal Bar Chart function:
def h_bar (df, col1, rate):
    # Data
    x = df.index.astype('str').to_list()
    y = df[col1]

    # Defining colors based on performance
    colors = ['#805D87' if n > rate else '#94D1E7' for n in y] 

    # Creating the chart
    fig, ax = plt.subplots(figsize = (6.5 , 6.5))
    ax.barh(x, y, .85, color = colors, alpha = .8)
    ax.axvline(x = rate, color = '#454775', linestyle ='--', linewidth = 1, label ='Overall ' + col1, alpha = 1)

    # Customizing the chart
    plt.gca().invert_yaxis()

    plt.title('', fontsize = 12, color = '#454775')

    plt.xlabel(col1, fontsize = 10, color = '#313E4C')
    plt.xticks(fontsize = 8, color = '#415366')

    plt.ylabel(df.index.name, fontsize = 10, color = '#313E4C')
    plt.yticks(fontsize = 8, color = '#415366')

    plt.legend(fontsize = 8, labelcolor = '#313E4C', loc = 'upper right', fancybox = True, shadow = True, bbox_to_anchor = (1, 1.05)) 

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    for spine in ax.spines.values():
        spine.set_linewidth(1.2)
        spine.set_edgecolor('#415366')
        spine.set_alpha(.8)
    
    # Annotating chart with values
    plt.text(rate, -1.01, f'{rate:.2%}', ha = 'left', va = 'center', fontsize = 9, color = '#313E4C', fontstyle = 'italic', weight = 'semibold')

    for i, v in enumerate(y):
        plt.text(v ,i , f'{v:.2%}', va = 'center', ha = 'right', fontsize = 6.5, color = '#313E4C')

                #############################################################################################################


# Demographic Influence:
#----------------------

# a) Calculations: 

# Conversion & Retention Rates function:
def con_ret (df, df2, cols, target): 
    first = df.groupby(cols)[target].nunique().reset_index()
    second = df2.groupby(cols)[target].nunique().reset_index()
    result = first.merge(second, on = cols, suffixes = ('_total', '_part'))
    result['Rate']= round(result.iloc[:, -1] / result.iloc[:, -2], 4)
    result = result.sort_values('Rate', ascending = False)
    required_cols = cols + ['Rate']
    result = result.loc[:, required_cols]
    result.columns = [x.replace('_', ' ').title() if x in cols else x for x in result.columns]
    return result

                                                #=========================================================#

# Heatmap Function:
def heatmap_chart(df): 
    col_list=df.columns.to_list()
    result_pivot=df.pivot_table(values=col_list[-1], index=col_list[1],columns=col_list[0])
    
    palette_10 = sns.color_palette(['#C9EFF5', '#C5E2ED', '#BECFE3', '#B4BADA', '#AA9ED2', '#A083C7', '#9879B7', '#9070A7', '#886797', '#805D87'])

    # Creating the Chart:
    ax=sns.heatmap(result_pivot, cmap=palette_10, annot=True, fmt=".2%", annot_kws={'color':'#313E4c','fontsize':9},
               linewidths=.4)

    # Customizing the Chart:
    plt.title('', fontsize=12, color='#454775')

    cbar = ax.collections[0].colorbar
    cbar.ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, pos: f'{x*100:.0f}%'))
    cbar.set_label('\nPercentages', fontsize=10, color='#313E4c')
    cbar.ax.tick_params(labelsize=9, colors='#415366')

    ax.set_xlabel(f'\n{col_list[0]}',fontsize=10, color='#313E4c')
    ax.set_ylabel(f'{col_list[1]}\n',fontsize=10, color='#313E4c')
    ax.tick_params(axis='both',labelsize=9, colors='#415366',labelrotation=0)


                #############################################################################################################


# Subscription Pattern:
#----------------------
    
# Creating the line charts function:
def group_line_plots (df1, df2, df3, cols, target): 
    # Gathering the tables of interest:
    first = df1.groupby(cols).user_id.count().reset_index().rename(columns = {target : 'Daily Users'})
    second = df2.groupby(cols).user_id.count().reset_index().rename(columns = {target : 'Converted'})
    third = df3.groupby(cols).user_id.count().reset_index().rename(columns = {target : 'Retained'})

    # Merging tables:
    result = first.merge(second, how = 'left', on = cols).merge(third, how = 'left', on = cols)
    
    # Table customization
    result.fillna(0, inplace = True)
    result.columns = [x.replace('_', ' ').title() if x in cols else x for x in result.columns]

    #Visualization
    df_list = list(result[result.columns[1]].unique())
    
    for i in range(len(df_list)):
        selects = result[result[result.columns[1]] == df_list[i]]
        label = selects.columns[0]
        x = selects[label].astype('str').to_list() 
        y1 = selects[selects.columns[2]].astype('int64') # Total Users
        y2 = selects[selects.columns[3]].astype('int64') # Converted
        y3 = selects[selects.columns[4]].astype('int64') # Retained
         
        # Creating the Chart:
        fig, ax = plt.subplots(figsize = (8 , 5))
        
        ax.plot(x, y1, color = '#EA9FBB', marker = 'H', markersize = 4, alpha = .5, ls = "--", label = selects.columns[2])
        
        ax.plot(x, y2, color='#805D87', marker = 'H', markersize=2, alpha=.8,label=selects.columns[3])
        
        ax.plot(x,y3,color='#94D1E7', marker = 'H', markersize=2, alpha=.8, label=selects.columns[4])
        
        # Customization
        plt.title('\n\n' + result.columns[1] + ": " + df_list[i] + '\n\n\n\n', fontsize = 14, color = '#454775', loc = 'left')

        plt.xlabel(label, fontsize = 12, color = '#313E4C')
        plt.xticks(rotation=90, fontsize = 8, color = '#415366')

        plt.ylabel('Total', fontsize = 12, color = '#313E4C')
        plt.yticks(fontsize = 8, color = '#415366')

        plt.grid(axis = 'y', linestyle = ":", color = '#454775', linewidth = 1, alpha = .3)
        
        plt.legend(fontsize=8, labelcolor = '#313E4C', loc = 'center left', fancybox = True, shadow = True)
        
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        for spine in ax.spines.values():
            spine.set_linewidth(1.2)
            spine.set_edgecolor('#415366')
            spine.set_alpha(.8)
            plt.xticks(rotation=90)
        
        # Anotating Maximun & Minimum Values:
        # Total Users
        ax.text(selects[y1 == y1.max()][label].astype('str').iloc[0], y1.max(), y1.max(), ha = 'center', va = 'center', fontsize = 7, color = '#313E4C')
        ax.text(selects[y1 == y1.min()][label].astype('str').iloc[0], y1.min(), y1.min(), ha = 'center', va = 'center', fontsize = 7, color = '#313E4C')

        # Converted
        ax.text(selects[y2 == y2.max()][label].astype('str').iloc[0], y2.max(), y2.max(), ha = 'right', va = 'bottom', fontsize = 7, color = '#313E4C')
        ax.text(selects[y2 == y2.min()][label].astype('str').iloc[0], y2.min(), y2.min(), ha = 'right', va = 'bottom', fontsize = 7, color = '#313E4C')
        
        # Retained
        ax.text(selects[y3 == y3.max()][label].astype('str').iloc[0], y3.max(), y3.max(), ha = 'left', va = 'top', fontsize = 7, color = '#313E4C')
        ax.text(selects[y3 == y3.min()][label].astype('str').iloc[0], y3.min(), y3.min(), ha = 'left', va = 'top', fontsize = 7, color = '#313E4C')

        # Creating Maximum & Minimum Tables
        rows=['Daily Users','Converted','Retained']
        row_colors=['#EA9FBB','#805D87','#94D1E7']

        # Maximum Table
        data_max = [[y1.max(), selects[y1 == y1.max()][label].astype(str).iloc[0]],
                    [y2.max(), selects[y2 == y2.max()][label].astype(str).iloc[0]], 
                    [y3.max(), selects[y3 == y3.max()][label].astype(str).iloc[0]]]
        
        columns_max = ['Maximum', label]
        
        table_max = ax.table(cellText = data_max, colLabels = columns_max, loc = 'top right',rowLoc = 'left', rowLabels = rows, rowColours = row_colors) 
        
        table_max.scale(2, 1.5)

        # Table_max Customization
        for key, cell in table_max.get_celld().items():
            cell.set_text_props(color = '#313E4C', fontsize = 10)
            cell.set_edgecolor('#454775')
            cell.set_linewidth(1)
        
        for (row,col), cell in table_max.get_celld().items():
            cell.set_alpha(.3)
        
        table_max.auto_set_column_width(col = list(range(len(selects.columns))))
        
        # Minimum Table
        data_min = [[y1.min(), selects[y1 == y1.min()][label].astype(str).iloc[0]],
                    [y2.min(), selects[y2 == y2.min()][label].astype(str).iloc[0]], 
                    [y3.min(), selects[y3 == y3.min()][label].astype(str).iloc[0]]]
        
        columns_min = [ 'Minimum', label]
        
        table_min=ax.table(cellText = data_min, colLabels = columns_min, loc = 'right', rowLoc = 'left', rowLabels = rows, rowColours = row_colors)
        
        table_min.scale(2, 1.5)
        
        # Table_min customization
        for key, cell in table_min.get_celld().items():
            cell.set_text_props(color = '#313E4C', fontsize = 10)
            cell.set_edgecolor('#454775')
            cell.set_linewidth(1)
        
        for (row,col), cell in table_min.get_celld().items():
            cell.set_alpha(.3)
        
        table_min.auto_set_column_width(col = list(range(len(selects.columns))))


                #############################################################################################################


# House Ads In-Depth Analysis:
#-----------------------------
# a) Calculations: 

# expected lost subscribers Function
def lost_sub (df1, df2):
    estimated_con = df1.sum().sum()
    actual_con = df2.sum().sum()
    expected_lost = estimated_con - actual_con 
    return np.ceil(expected_lost)

                                                 #=========================================================#


# Visualization:

# 1- Creating a line chart function
def two_lines (df, col1, col2, col3): 
    # Data
    x = df[col1].astype('str').to_list()
    y = df[col2]
    z = df[col3]
    
    # Creating the Chart
    fig, ax = plt.subplots(figsize = (8 , 5))
    
    ax.plot(x, y, color = '#805D87', marker = 'H', markersize = 2, alpha = .8, label = df.columns[1])
    
    ax.plot(x, z, color = '#EA9FBB', marker = 'H', markersize = 4, alpha = .5, ls = "--", label = df.columns[2])

    # Chart Customization
    plt.title('', fontsize = 14, color = '#454775', loc = 'left')

    plt.xlabel(df.columns[0], fontsize = 12, color = '#313E4C')
    plt.xticks(rotation = 90, fontsize = 8, color = '#415366')

    plt.ylabel('Total', fontsize = 12, color = '#313E4C')
    plt.yticks(fontsize = 8, color = '#415366')

    plt.grid(axis = 'y', linestyle = ":", color = '#454775', linewidth = 1, alpha = .3)
        
    plt.legend(fontsize = 8, labelcolor = '#313E4C', loc = 'upper right', fancybox = True, shadow = True)
        
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    for spine in ax.spines.values():
        spine.set_linewidth(1.2)
        spine.set_edgecolor('#415366')
        spine.set_alpha(.8)
    
    # Anotating Values on Chart
    for i, v in enumerate(y): 
        plt.text(i, v, v, ha = 'center', va = 'bottom', fontsize = 7, color = '#313E4C')
    
    for i, v in enumerate(z): 
        plt.text(i, v, v, ha = 'center', va = 'top', fontsize = 7, color = '#313E4C')


                                                #---------------------------------------------------------#


# 2- Creating a line chart function
def two_lines_pct (df , col1, col2, col3): 
    # Data
    x = df[col1].astype('str').to_list()
    y = df[col2]
    z = df[col3]
    
    # Creating the Chart
    fig, ax = plt.subplots(figsize = (8 , 5))
    
    ax.plot(x, y, color = '#805D87', marker = 'H', markersize = 2, alpha = .5, label = col2[1])
    
    ax.plot(x , z, color = '#EA9FBB', marker = 'H', markersize = 4, alpha = .8, ls = "--", label = col3[1]);

    # Chart Customization
    plt.title('\n\n Actual vs. Estimated Conversion Rates - ' + col2[1].replace('_Actual', '') + '\n', fontsize = 14, color = '#454775', loc = 'left')

    plt.xlabel(col1.title().replace('_' , ' '), fontsize = 12, color = '#313E4C')
    plt.xticks(rotation = 90, fontsize = 8, color = '#415366')

    plt.ylabel('Total', fontsize = 12, color = '#313E4C')
    plt.yticks(fontsize = 8, color = '#415366')

    plt.grid(axis = 'y', linestyle = ":", color = '#454775', linewidth = 1, alpha = .3)
        
    plt.legend(fontsize = 8, labelcolor = '#313E4C', loc = 'upper right', fancybox = True, shadow = True)
        
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    for spine in ax.spines.values():
        spine.set_linewidth(1.2)
        spine.set_edgecolor('#415366')
        spine.set_alpha(.8)
    
    # Anotating Values on Chart
    for i, v in enumerate(y): 
        plt.text(i, v, f'{v:.0%}', ha = 'center', va = 'bottom', fontsize = 7, color = '#313E4C')
    
    for i, v in enumerate(z): 
        plt.text(i, v, f'{v:.0%}', ha = 'center', va = 'top', fontsize = 7, color = '#313E4C')
