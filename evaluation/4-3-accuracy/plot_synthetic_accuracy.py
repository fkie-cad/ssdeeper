#!/usr/bin/env python3
# coding=utf-8
import json
import os
import sys
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import seaborn as sns
from itertools import cycle
import numpy as np
from os.path import basename


def plot_figure(df, outfile, size, section, palette):
    df = df.loc[(df['size'] == size)]
    df = df.loc[(df['section'] == section)]
    df_change = df.loc[(df['mod'] == 'change')]
    df_insert = df.loc[(df['mod'] == 'insert')]
    df_delete = df.loc[(df['mod'] == 'delete')]

    sns.set_style('whitegrid', {'xtick.major.size':5, 'xtick.minor.size': 2, 'ytick.major.size':5, 'ytick.minor.size':2})
    paper_rc = {'lines.linewidth': 0.7, 'lines.markersize': 0.6}
    sns.set_context("paper", rc = paper_rc)
    fig, axes = plt.subplots(1, 3, figsize=(15,5))

    axes[0] = plt.subplot2grid((1,3), (0,0), colspan=1)
    axes[0].set_title('Modification: Exchange bytes')
    axes[1] = plt.subplot2grid((1,3), (0,1), colspan=1)
    axes[1].set_title('Modification: Delete bytes')
    axes[2] = plt.subplot2grid((1,3), (0,2), colspan=1)
    axes[2].set_title('Modification: Insert bytes')

    g = sns.pointplot(x='similarity', y='result', hue='algorithm', data=df_change, palette=palette, ax=axes[0], capsize=.6)
    h = sns.pointplot(x='similarity', y='result', hue='algorithm', data=df_delete, palette=palette, ax=axes[1], capsize=.6)
    i = sns.pointplot(x='similarity', y='result', hue='algorithm', data=df_insert, palette=palette, ax=axes[2], capsize=.6)

    g.set(ylabel="similarity output", xlabel="size of modification in percent relative to the original")
    h.set(ylabel="", xlabel="size of modification in percent relative to the original")
    i.set(ylabel="similarity output", xlabel="size of modification in percent relative to the original")

    axes[0].set_xticks([0,10,20,30,40,50,60,70,80,90,100])
    axes[1].set_xticks([0,10,20,30,40,50,60,70,80,90,100])
    axes[2].set_xticks([0,10,20,30,40,50,60,70,80,90,100])
    axes[0].set(xticklabels=[100,90,80,70,60,50,40,30,20,10,0])
    axes[1].set(xticklabels=[100,90,80,70,60,50,40,30,20,10,0])
    axes[2].set(xticklabels=[100,90,80,70,60,50,40,30,20,10,0])

    h.legend_.remove()
    i.legend_.remove()

    g.axes.tick_params(labelbottom=True, labeltop=False, labelleft=True, labelright=False, bottom=False, top=False, left=True, right=False)
    h.axes.tick_params(labelbottom=True, labeltop=False, labelleft=False, labelright=False, bottom=False, top=False, left=False, right=False)
    i.axes.tick_params(labelbottom=True, labeltop=False, labelleft=False, labelright=True, bottom=False, top=False, left=False, right=True)

    for ax in axes:
        ax.invert_xaxis()

    plt.tight_layout()
    plt.savefig(outfile)
    plt.close('all')



def create_all_find_comparison_plot(csvfile, outfile, i):
    df = pd.read_csv(csvfile, delimiter=';')
    
    df1 = df.loc[(df['hash_generation'] == 'ssdeep-original')]
    df2 = df.loc[(df['hash_generation'] == 'ssdeep-refactored')]
    df3 = df.loc[(df['hash_generation'] == 'ssdeep-refactored-polynomial')]
    df3['algorithm'] = '-refactored-poly'
    df4 = df.loc[(df['hash_generation'] == 'ssdeep-refactored-djb2')]
    df5 = df.loc[(df['hash_generation'] == 'ssdeep-4b')]
    df6 = df.loc[(df['hash_generation'] == 'ssdeep-refactored-4b')]
    df7 = df.loc[(df['hash_generation'] == 'ssdeep-refactored-4b-polynomial')]
    df8 = df.loc[(df['hash_generation'] == 'ssdeep-refactored-4b-djb2')]

    df11 = df1.loc[(df1['hash_comparison'] == 'ssdeep-original')]
    df11['algorithm'] = '-original'
    df12 = df1.loc[(df1['hash_comparison'] == 'ssdeep-original-opt')]
    df12['algorithm'] = '-nocommsub'
    df13 = df1.loc[(df1['hash_comparison'] == 'ssdeep-original-max')]
    df13['algorithm'] = '-nomax'
    df14 = df1.loc[(df1['hash_comparison'] == 'ssdeep-original-opt-max')]
    df14['algorithm'] = '-nocommsub-nomax'
    
    df21 = df2.loc[(df2['hash_comparison'] == 'ssdeep-original')]
    df21['algorithm'] = '-refactored'
    df22 = df2.loc[(df2['hash_comparison'] == 'ssdeep-original-opt')]
    df22['algorithm'] = '-refactored-nocommsub'
    df23 = df2.loc[(df2['hash_comparison'] == 'ssdeep-original-max')]
    df23['algorithm'] = '-refactored-max'
    df24 = df2.loc[(df2['hash_comparison'] == 'ssdeep-original-opt-max')]
    df24['algorithm'] = '-refactored-opt-max'
   
    df31 = df3.loc[(df3['hash_comparison'] == 'ssdeep-original')]
    df31['algorithm'] = '-refactored-poly'
    df32 = df3.loc[(df3['hash_comparison'] == 'ssdeep-original-opt')]
    df32['algorithm'] = '-refactored-poly-opt'
    df33 = df3.loc[(df3['hash_comparison'] == 'ssdeep-original-max')]
    df33['algorithm'] = '-refactored-poly-max'
    df34 = df3.loc[(df3['hash_comparison'] == 'ssdeep-original-opt-max')]
    df34['algorithm'] = '-refactored-poly-opt-max'
    
    df41 = df4.loc[(df4['hash_comparison'] == 'ssdeep-original')]
    df41['algorithm'] = '-refactored-djb2'
    df42 = df4.loc[(df4['hash_comparison'] == 'ssdeep-original-opt')]
    df42['algorithm'] = '-refactored-djb2-opt'
    df43 = df4.loc[(df4['hash_comparison'] == 'ssdeep-original-max')]
    df43['algorithm'] = '-refactored-djb2-max'
    df44 = df4.loc[(df4['hash_comparison'] == 'ssdeep-original-opt-max')]
    df44['algorithm'] = '-refactored-djb2-opt-max'
    
    df51 = df5.loc[(df5['hash_comparison'] == 'ssdeep-4b')]
    df51['algorithm'] = '-4b'
    df52 = df5.loc[(df5['hash_comparison'] == 'ssdeep-4b-opt')]
    df52['algorithm'] = '-4b-opt'
    df53 = df5.loc[(df5['hash_comparison'] == 'ssdeep-4b-max')]
    df53['algorithm'] = '-4b-max'
    df54 = df5.loc[(df5['hash_comparison'] == 'ssdeep-4b-opt-max')]
    df54['algorithm'] = '-4b-opt-max'
    
    df61 = df6.loc[(df6['hash_comparison'] == 'ssdeep-4b')]
    df61['algorithm'] = '-refactored-4b'
    df62 = df6.loc[(df6['hash_comparison'] == 'ssdeep-4b-opt')]
    df62['algorithm'] = '-refactored-4b-opt'
    df63 = df6.loc[(df6['hash_comparison'] == 'ssdeep-4b-max')]
    df63['algorithm'] = '-refactored-4b-max'
    df64 = df6.loc[(df6['hash_comparison'] == 'ssdeep-4b-opt-max')]
    df64['algorithm'] = '-refactored-4b-opt-max'
    
    df71 = df7.loc[(df7['hash_comparison'] == 'ssdeep-4b')]
    df71['algorithm'] = '-refactored-4b-poly'
    df72 = df7.loc[(df7['hash_comparison'] == 'ssdeep-4b-opt')]
    df72['algorithm'] = '-refactored-4b-poly-opt'
    df73 = df7.loc[(df7['hash_comparison'] == 'ssdeep-4b-max')]
    df73['algorithm'] = '-refactored-4b-poly-max'
    df74 = df7.loc[(df7['hash_comparison'] == 'ssdeep-4b-opt-max')]
    df74['algorithm'] = '-refactored-4b-poly-opt-max' 
    
    df81 = df8.loc[(df8['hash_comparison'] == 'ssdeep-4b')]
    df81['algorithm'] = '-refactored-4b-djb2'
    df82 = df8.loc[(df8['hash_comparison'] == 'ssdeep-4b-opt')]
    df82['algorithm'] = '-refactored-4b-djb2-opt'
    df83 = df8.loc[(df8['hash_comparison'] == 'ssdeep-4b-max')]
    df83['algorithm'] = '-refactored-4b-djb2-max'
    df84 = df8.loc[(df8['hash_comparison'] == 'ssdeep-4b-opt-max')]
    df84['algorithm'] = '-refactored-4b-djb2-opt-max'       

    df11 = df1.loc[(df1['hash_comparison'] == 'ssdeep-original')]
    df11['algorithm'] = '-original'
    df12 = df1.loc[(df1['hash_comparison'] == 'ssdeep-original-opt')]
    df12['algorithm'] = '-nocommsub'
    df13 = df1.loc[(df1['hash_comparison'] == 'ssdeep-original-max')]
    df13['algorithm'] = '-nomax'
    df14 = df1.loc[(df1['hash_comparison'] == 'ssdeep-original-opt-max')]
    df14['algorithm'] = '-nocommsub-nomax'

    if 'PALETTE' in os.environ:
        palette = json.loads(os.getenv('PALETTE'))
        palette['-original'] = palette['-original-black']
        palette['-nocommsub'] = palette['-original-black']
        palette['-nomax'] = palette['-original-black']
        palette['-nocommsub-nomax'] = palette['-original-black']
        palette['-refactored-4b-djb2'] = palette['-refactored-4b-djb2']
        palette['-refactored-4b-djb2-opt'] = palette['-refactored-4b-djb2']
        palette['-refactored-4b-djb2-max'] = palette['-refactored-4b-djb2']
        palette['-refactored-4b-djb2-opt-max'] = palette['-refactored-4b-djb2']
        palette['-refactored-4b-poly'] = palette['-refactored-4b-poly']
        palette['-refactored-4b-poly-opt'] = palette['-refactored-4b-poly']
        palette['-refactored-4b-poly-max'] = palette['-refactored-4b-poly']
        palette['-refactored-4b-poly-opt-max'] = palette['-refactored-4b-poly']
        palette['-refactored-4b'] = palette['-refactored-4b']
        palette['-refactored-4b-opt'] = palette['-refactored-4b']
        palette['-refactored-4b-max'] = palette['-refactored-4b']
        palette['-refactored-4b-opt-max'] = palette['-refactored-4b']
        palette['-4b'] = palette['-4b']
        palette['-4b-opt'] = palette['-4b']
        palette['-4b-max'] = palette['-4b']
        palette['-4b-opt-max'] = palette['-4b']
        palette['-refactored-djb2'] = palette['-refactored-djb2']
        palette['-refactored-djb2-opt'] = palette['-refactored-djb2']
        palette['-refactored-djb2-max'] = palette['-refactored-djb2']
        palette['-refactored-djb2-opt-max'] = palette['-refactored-djb2']
        palette['-refactored-poly'] = palette['-refactored-poly']
        palette['-refactored-poly-opt'] = palette['-refactored-poly']
        palette['-refactored-poly-max'] = palette['-refactored-poly']
        palette['-refactored-poly-opt-max'] = palette['-refactored-poly']
        palette['-refactored'] = palette['-refactored']
        palette['-refactored-nocommsub'] = palette['-refactored']
        palette['-refactored-max'] = palette['-refactored']
        palette['-refactored-opt-max'] = palette['-refactored']
    else: 
        palette = sns.husl_palette(4, h=1, l=.7, s=.85)
        
    dfa = pd.concat([df11, df21, df31, df41]) # CF: 2b original
    dfb = pd.concat([df51, df61, df71, df81]) # CF: 4b original
    dfc = pd.concat([df12, df22, df32, df42]) # CF: 2b -opt 
    dfd = pd.concat([df52, df62, df72, df82]) # CF: 4b -opt
    dfe = pd.concat([df13, df23, df33, df43]) # CF: 2b -max
    dff = pd.concat([df53, df63, df73, df83]) # CF: 4b -max
    dfg = pd.concat([df14, df24, df34, df44]) # CF: 2b -opt-max
    dfh = pd.concat([df54, df64, df74, df84]) # CF: 4b -opt-max
    
    CF_string = ['_2b', '_4b', '_2b_opt', '_4b_opt', '_2b_max', '_4b_max', '_2b_opt_max', '_4b_opt_max']
    synthetic_dfs = [dfa, dfb, dfc, dfd, dfe, dff, dfg, dfh]  
    for size in [1000, 10000, 100000, 1000000, 10000000]:
        for section in ['first', 'second', 'third']:
             o = ''.join(outfile.split('.')[:-1]) + CF_string[i] + '_' + section + '.pdf'
             ol = o.split('/')
             o = '/'.join(ol[:-1]) + '/' + str(size) + '/' + ''.join(ol[-1::])
             plot_figure(synthetic_dfs[i], o, size, section, palette)



def main(argv=None):
    if argv is None:
        argv = sys.argv
    if len(argv) != 4:
        print('Usage: {prog} CSVFILE OUTFILE ITERATOR'.format(prog=argv[0]))
        return 1
    
    create_all_find_comparison_plot(argv[1], argv[2], int(argv[3]))


if __name__ == '__main__':
    sys.exit(main())
