import argparse
import json
import random
import math
import sys
import os
import sys
import matplotlib.pyplot as plt
from matplotlib.patches import PathPatch
import numpy as np
import pandas as pd
import seaborn as sns
from os.path import basename
from itertools import cycle


def histogram_plot(df, outfile, _palette=None):
    sns.set_style('whitegrid', {'patch.edgecolor': '#888'})
    paper_rc = {'lines.linewidth': 1, 'lines.markersize': 0.5}
    sns.set_context("paper", rc = paper_rc, font_scale=1.7)
        
    df_unfit = df.loc[(df['len2'] <= 10)]
        
    fig, ax = plt.subplots(3, 1, figsize=(16,8))

    _palette = sns.husl_palette(25, h=1, l=.7, s=.85)
    p = [_palette[0]]
    if 'PALETTE' in os.environ:
        p = json.loads(os.getenv('PALETTE'))
    h = sns.histplot(df, x='len1', hue='algorithm', multiple="dodge", shrink=.5, discrete=True, ax=ax[0], palette=p)
    g = sns.histplot(df, x='len2', hue='algorithm', multiple="dodge", shrink=.5, discrete=True, ax=ax[1], palette=p)
    i = sns.histplot(df_unfit, x='len2', hue='algorithm', multiple="dodge", shrink=.5, ax=ax[2], palette=p, discrete=True)

    h.set(xlabel="length of first signature", ylabel="count")
    g.set(xlabel="length of second signature", ylabel="count")
    i.set(xlabel="length of second signature", ylabel="count")

    fig.set_figwidth(12)
    fig.set_figheight(15)

    h.legend_.set_title(None)
    g.legend_.set_title(None)
    i.legend_.set_title(None)
    
    plt.tight_layout()
    plt.savefig(outfile)
    plt.close('all')   

   
def plot_paper(df, outfile, _palette=None):   
    sns.set_style('whitegrid', {'patch.edgecolor': '#888'})
    paper_rc = {'lines.linewidth': 1, 'lines.markersize': 0.5}
    sns.set_context("paper", rc = paper_rc, font_scale=2.4)
        
    fig, ax = plt.subplots(figsize=(16,8))
    
    df = df.loc[(df['len2'] <= 10)]

    if 'PALETTE' in os.environ:
        p = json.loads(os.getenv('PALETTE'))
    else: 
        _palette = sns.husl_palette(25, h=1, l=.7, s=.85)
        p = [_palette[0], _palette[6], _palette[8], _palette[9]]
    
    h = sns.histplot(df, x='len2', hue='algorithm', multiple="dodge", shrink=.6, discrete=True, ax=ax, palette=p)

    h.set(xlabel="length of second signature", ylabel="count")
    
    h.set(xlim=(-0.1,10.6))
    h.set(ylim=(-1,2000))

    fig.set_figwidth(12)
    fig.set_figheight(7)

    h.legend_.set_title(None)

    h.axes.set_xticks([0,1,2,3,4,5,6,7,8,9,10])
    #h.set_xticklabels(['      0', '     1', '     2', '     3', '     4', '     5', '     6', '     7', '     8', '     9', '     10'])
    plt.tight_layout()
    plt.savefig(outfile)
    plt.close('all')   


def get_df_list(df):
    df0 = df.loc[(df['algorithm'] == 'original (NSRL)')]
    df0['algorithm'] = '-original (NSRL)'
    
    df1 = df.loc[(df['algorithm'] == 'original')]
    df1['algorithm'] = '-original'
    df2 = df.loc[(df['algorithm'] == 'bug')]
    df2['algorithm'] = '-bugfix'
    df3 = df.loc[(df['algorithm'] == 'feature')]
    df3['algorithm'] = '-no32lim'
    df4 = df.loc[(df['algorithm'] == 'polynomial')]
    df4['algorithm'] = '-poly'    
        
    df5 = df.loc[(df['algorithm'] == 'djb2')]
    df5['algorithm'] = '-djb2'
    df6 = df.loc[(df['algorithm'] == 'refactored')]
    df6['algorithm'] = '-refactored'
    df7 = df.loc[(df['algorithm'] == 'refactored-polynomial')]
    df7['algorithm'] = '-refactored-poly'
    df8 = df.loc[(df['algorithm'] == 'refactored-djb2')]
    df8['algorithm'] = '-refactored-djb2'
        
    df9 = df.loc[(df['algorithm'] == '4b')]
    df9['algorithm'] = '-4b'
    df10 = df.loc[(df['algorithm'] == 'refactored-4b')]
    df10['algorithm'] = '-refactored-4b'
    df11 = df.loc[(df['algorithm'] == 'refactored-4b-polynomial')]
    df11['algorithm'] = '-refactored-4b-poly'
    df12 = df.loc[(df['algorithm'] == 'refactored-4b-djb2')]
    df12['algorithm'] = '-refactored-4b-djb2'

    return [df0, df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12]

def main(argv=None):
    if argv is None:
        argv = sys.argv
    if len(argv) != 2:
        print('Usage: {prog} CSVFILE'.format(prog=argv[0]))
        return
    df = pd.read_csv(argv[1], delimiter=',')
    df_list = get_df_list(df)
    
    plot_paper(pd.concat([df_list[1], df_list[6], df_list[8], df_list[7]]), 'histogram_paper.pdf')
    for df in df_list:
       plotname = 'histogram' + df['algorithm'].tolist()[0] + '.pdf'
       histogram_plot(df, plotname)
        
    
if __name__ == "__main__":
    main()
