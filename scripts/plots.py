import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Count plot
def plot_count(data:pd.DataFrame,col:str)->None:
    plt.figure(figsize=(13,6.5))
    sns.countplot(data[col])
    plt.title(f'Count of Cancer {col}')
    plt.show()
    
# Pie plot
def plot_pie(data:pd.DataFrame,col:str)->None:
    pie, ax = plt.subplots(figsize=[13,6.5])
    labels=['Benign','Malign']
    plt.pie(data[col].value_counts(), explode=(0,0.1), labels=labels, autopct="%.1f%%", shadow=True)
    plt.title('Percentage of diagnosis', fontsize=14)
    plt.legend()
    plt.show()
    
# Scatter plot
def plot_scatter(df,col1,col2):
    #fig, ax = plt.subplots(2,1, figsize=(15, 15))
    plt.figure(figsize=(13, 6.5))
    sns.scatterplot(x=col1, y=col2, hue="diagnosis", data = df, palette='magma')
    plt.title(f'{col1} vs {col2}', size=16)
    plt.xticks(fontsize=14)
    plt.yticks( fontsize=14)
    plt.show()
    
# Heat map
def plot_heat(data:pd.DataFrame)->None:
    f, ax = plt.subplots(figsize = (20, 20))
    corr = data.corr()
    #plt.figure(figsize=(20,20))
    #sns.heatmap(corr, cbar=True, square= True, fmt='.1f', annot=True, annot_kws={'size':15}, cmap='summer_r')
    sns.heatmap(data.corr(), annot = True, linewidth = 0.5, fmt = '.1f', ax = ax )
    #plt.savefig("../figures/correlation.png")
    plt.show()
    
# Hisogram plot
def plot_hist(df:pd.DataFrame, column:str, color:str)->None:
    plt.figure(figsize=(13, 6.5))
    sns.displot(data=df, x=column, color=color, kde=True, height=7, aspect=2)
    plt.title(f'Distribution of {column}', size=20, fontweight='bold')
    plt.show()
    
#Distribution plot    
def plot_distribution(data:pd.DataFrame,col:str)->None:
    sns.FacetGrid(data, hue="diagnosis", height=6).map(sns.distplot, col).add_legend()
    plt.show()