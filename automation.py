import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.ticker as mticker
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import matplotlib.patheffects as path_effects
import seaborn as sns

def dates(df,cols):
    start= df[cols].astype('datetime64[ns]').min().strftime('%Y-%m-%d') 
    end= df[cols].astype('datetime64[ns]').max().strftime('%Y-%m-%d')
    return f'''
    Start: {start} 
    End  : {end}\n'''