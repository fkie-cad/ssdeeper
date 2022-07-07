#!/usr/bin/env python3
# coding=utf-8
import json
import os
import matplotlib.pyplot as plt
from matplotlib.patches import PathPatch
import numpy as np
import pandas as pd
import seaborn as sns
from os.path import basename
import sys
from itertools import cycle 


def plot_runtime_box_plot(df1, df2, outfile, _palette=None, datatype=None):
    sns.set_style('whitegrid')
    paper_rc = {'lines.linewidth': 1, 'lines.markersize': 0.5}
    sns.set_context("paper", rc = paper_rc, font_scale=1)
    if _palette is None:
        _palette = 'colorblind'
    
    fig, axes = plt.subplots(2, 1, figsize=(10,1))

    axes[0] = plt.subplot2grid((1,2), (0,0), colspan=1)
    axes[0].set_title('real data')
    axes[1] = plt.subplot2grid((1,2), (0,1), colspan=1)
    if datatype:
    	axes[1].set_title('%s' % (datatype))
    else:
    	axes[1].set_title('synthetic data')
    
    axes[0].tick_params(labelbottom=True, labeltop=True, labelleft=True, labelright=False, bottom=False, top=False, left=True, right=False)
    axes[1].tick_params(labelbottom=True, labeltop=True, labelleft=False, labelright=True, bottom=False, top=False, left=False, right=True)
    
    g = sns.boxplot(x='i', y='n/t', hue='algorithm', fliersize=0.8, ax=axes[0], data=df1, palette=_palette, width=0.8, dodge=False, order=np.arange(15))
    h = sns.boxplot(x='i', y='n/t', hue='algorithm', fliersize=0.8, ax=axes[1], data=df2, palette=_palette, width=0.8, dodge=False, order=np.arange(15))
    
    g.set(xlabel="SPHF", ylabel="throughput in KB/ms")
    g.set(ylim=(-10,290))
    g.set(xlim=(0, 13))
    g.set_xticklabels(['', '', '', '', '', '', '', '', '', '',
                       '', '', '', '', ''])
                                         
    h.set(xlabel="SPHF", ylabel="")
    h.set(ylim=(-10,290))
    h.set(xlim=(0, 13))
    h.set_xticklabels(['', '', '', '', '', '', '', '', '', '',
                       '', '', '', '', ''])
    
    x, l = h.get_legend_handles_labels()
    g.legend_.remove()
    h.legend_.remove()
    
    plt.tight_layout()
    fig.legend(x, l, loc='upper center', title='SPHF', markerscale=1., bbox_to_anchor=(0.515,0.79), ncol=6, prop={'size': 9})
    fig.set_figheight(8)
    
    plt.savefig(outfile)
    plt.close('all')    


def get_df(csvfile, datatype=None):
    df = pd.read_csv(csvfile, delimiter=';')
    if datatype:
    	df = df.loc[(df['datatype'] == datatype)]
    df['size'] = df['size']/1000
    df['time'] = df['time']/1000000
    plotname = 'ssdeep'
    newdf1 = df.loc[(df['algorithm'] == 'ssdeep-original')]
    newdf1 = newdf1.groupby('filename').mean()
    newdf1['algorithm'] = '-original'
    newdf2 = df.loc[(df['algorithm'] == 'ssdeep-bug')]
    newdf2 = newdf2.groupby('filename').mean()
    newdf2['algorithm'] = '-bugfix'    
    newdf3 = df.loc[(df['algorithm'] == 'ssdeep-feature')]
    newdf3 = newdf3.groupby('filename').mean()
    newdf3['algorithm'] = '-no32lim'
    newdf4 = df.loc[(df['algorithm'] == 'ssdeep-djb2')]
    newdf4 = newdf4.groupby('filename').mean()
    newdf4['algorithm'] = '-djb2'
    newdf5 = df.loc[(df['algorithm'] == 'ssdeep-polynomial')]
    newdf5 = newdf5.groupby('filename').mean()
    newdf5['algorithm'] = '-poly'
    newdf6 = df.loc[(df['algorithm'] == 'ssdeep-4b')]
    newdf6 = newdf6.groupby('filename').mean()
    newdf6['algorithm'] = '-4b'
    newdf7 = df.loc[(df['algorithm'] == 'ssdeep-refactored')]
    newdf7 = newdf7.groupby('filename').mean()
    newdf7['algorithm'] = '-refactored'
    newdf8 = df.loc[(df['algorithm'] == 'ssdeep-refactored-4b')]
    newdf8 = newdf8.groupby('filename').mean()
    newdf8['algorithm'] = '-refactored-4b'
    newdf9 = df.loc[(df['algorithm'] == 'ssdeep-refactored-djb2')]
    newdf9 = newdf9.groupby('filename').mean()
    newdf9['algorithm'] = '-refactored-djb2'
    newdf10 = df.loc[(df['algorithm'] == 'ssdeep-refactored-polynomial')]
    newdf10 = newdf10.groupby('filename').mean()
    newdf10['algorithm'] = '-refactored-poly'
    newdf11 = df.loc[(df['algorithm'] == 'ssdeep-refactored-4b-djb2')]
    newdf11 = newdf11.groupby('filename').mean()
    newdf11['algorithm'] = '-refactored-4b-djb2'
    newdf12 = df.loc[(df['algorithm'] == 'ssdeep-refactored-4b-polynomial')]
    newdf12 = newdf12.groupby('filename').mean()
    newdf12['algorithm'] = '-refactored-4b-poly'
    i = 1
    for df in [newdf1, newdf2, newdf3, newdf4, newdf5, newdf6, newdf7, newdf8, newdf9, newdf10, newdf11, newdf12]:
    #for df in [newdf1, newdf2, newdf3, newdf7, newdf4, newdf5, newdf9, newdf10, newdf6, newdf8, newdf11, newdf12]:
        df['n/t'] = df['size'] / df['time']
        df['i'] = i
        i += 1
        print(df['algorithm'][0], df['n/t'].mean())
    df_total = pd.concat([newdf1, newdf2, newdf3, newdf4, newdf5, newdf6, newdf7, newdf8, newdf9, newdf10, newdf11, newdf12])
    #df_total = pd.concat([newdf1, newdf2, newdf3, newdf7, newdf4, newdf5, newdf9, newdf10, newdf6, newdf8, newdf11, newdf12])
    return df_total 


def create_runtime_comparison_plot(csvfile1, csvfile2, o):
    df1 = get_df(csvfile1)
    df2 = get_df(csvfile2)

    if 'PALETTE' in os.environ:
        _palette = json.loads(os.getenv('PALETTE'))
    else: 
        _palette = sns.husl_palette(25, h=1, l=.7, s=.85)
        
    # plot box plot for chosen SPHFs
    plot_runtime_box_plot(df1, df2, o, _palette)

    # plot box plot for some data types
    for datatype in ['pdf', 'text', 'doc', 'html']:
    	dft = get_df(csvfile1, datatype)
    	outfile = ''.join(o.split('.')[:-1]) + '_' + datatype + '.pdf'
    	plot_runtime_box_plot(df1, dft, outfile, _palette, datatype)


def main(argv=None):
    if argv is None:
        argv = sys.argv
    if len(argv) != 4:
        print('Usage: {prog} CSVFILE CSVFILE OUTFILE'.format(prog=argv[0]))
        return

    df1 = create_runtime_comparison_plot(argv[1], argv[2], argv[3])
    

if __name__ == '__main__':
    sys.exit(main())
