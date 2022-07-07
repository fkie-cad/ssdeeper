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



def create_all_find_comparison_plot(csvfile, outfile, datatype=None, section=None):
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
    
    all_dfs = [df11, df12, df13, df14, df21, df22, df23, df24, df31, df32, df33, df34, df41, df42, df43, df44,
    	       df51, df52, df53, df54, df61, df62, df63, df64, df71, df72, df73, df74, df81, df82, df83, df84]
    
    for x in [df11]:
    	df = pd.concat([x])
    	outfile = ''.join(outfile.split('.')[:-1]) + df['algorithm'].tolist()[0] + '.pdf'
    
    sns.set_style('whitegrid')
    paper_rc = {'lines.linewidth': 1, 'lines.markersize': 1}
    sns.set_context("paper", rc = paper_rc, font_scale=2.5)

    df['result'] = df['result'].astype(int)          

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
        _palette = sns.husl_palette(25, h=1, l=.7, s=.85)
        palette = [_palette[0], _palette[15], _palette[16], _palette[17]]

    df_change = df.loc[(df['mod'] == 'change')]
    df_insert = df.loc[(df['mod'] == 'insert')]
    df_delete = df.loc[(df['mod'] == 'delete')]
    

    fig, axes = plt.subplots(3, 1, figsize=(30,30))

    axes[0] = plt.subplot2grid((3,1), (0,0), colspan=1)
    axes[0].set_title('Modification: Exchange bytes')
    axes[1] = plt.subplot2grid((3,1), (1,0), colspan=1)
    axes[1].set_title('Modification: Delete bytes')
    axes[2] = plt.subplot2grid((3,1), (2,0), colspan=1)
    axes[2].set_title('Modification: Insert bytes')

    g = sns.boxplot(x='similarity', y='result', hue='algorithm', fliersize=0.75, data=df_change, width=0.9, dodge=True, ax=axes[0], palette=palette)
    h = sns.boxplot(x='similarity', y='result', hue='algorithm', fliersize=0.75, data=df_insert, width=0.9, dodge=True, ax=axes[1], palette=palette)
    i = sns.boxplot(x='similarity', y='result', hue='algorithm', fliersize=0.75, data=df_delete, width=0.9, dodge=True, ax=axes[2], palette=palette)
    #g.set(ylim=(-2,102))
    #g.set(xlim=(-3,157))
    
    #fig.set_figheight(18)
    #fig.set_figwidth(30)

    #g.axes.tick_params(labelbottom=True, labeltop=False, labelleft=True, labelright=True, bottom=False, top=False, left=True, right=True)
    
    axes[0].set_xticks([0,10,20,30,40,50,60,70,80,90,100])
    axes[1].set_xticks([0,10,20,30,40,50,60,70,80,90,100])
    axes[2].set_xticks([0,10,20,30,40,50,60,70,80,90,100])
    axes[0].set(xticklabels=[100,90,80,70,60,50,40,30,20,10,0])
    axes[1].set(xticklabels=[100,90,80,70,60,50,40,30,20,10,0])
    axes[2].set(xticklabels=[100,90,80,70,60,50,40,30,20,10,0])

    g.set(ylabel="similarity output", xlabel="size of modification in percent relative to the original")
    h.set(ylabel="similarity output", xlabel="size of modification in percent relative to the original")
    i.set(ylabel="similarity output", xlabel="size of modification in percent relative to the original")

    #plt.text(16,105, ' 10', fontsize=22)
    #plt.text(56,105, ' 25', fontsize=22)
    #plt.text(96,105, '50', fontsize=22)
    #plt.text(136,105, '75', fontsize=22)
    #plt.text(53,110, ' fragment size in percent relative to the original file', fontsize=23)

    #h, l = g.get_legend_handles_labels()
    #labels=['-original', '-nocommonsub', '-nomax', '-nocommonsub-nomax']
    #legend1 = ax.legend(h[0:4], labels, loc='upper center', title='CF', markerscale=9., bbox_to_anchor=(0.153, +1.24), ncol=2, prop={'size': 22})
    
    h.legend_.remove()
    i.legend_.remove()

    for ax in axes:
        ax.tick_params(axis='x', which='major')
        ax.tick_params(axis='x', direction='out')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        ax.invert_xaxis()
    
    plt.tight_layout()
    #g.axes.add_artist(legend1)

    plt.savefig(outfile)
    plt.close('all')
 


def main(argv=None):
    if argv is None:
        argv = sys.argv
    if len(argv) != 3:
        print('Usage: {prog} CSVFILE OUTFILE'.format(prog=argv[0]))
        return 1

    create_all_find_comparison_plot(argv[1], argv[2], None, None)
    #create_all_find_comparison_plot(argv[1], argv[2], None, 'first')
    #create_all_find_comparison_plot(argv[1], argv[2], None, 'second')
    #create_all_find_comparison_plot(argv[1], argv[2], None, 'third')
    #create_all_find_comparison_plot(argv[1], argv[2], 'pdf') #1073
    #create_all_find_comparison_plot(argv[1], argv[2], 'html') #1093
    #create_all_find_comparison_plot(argv[1], argv[2], 'doc') #533
    #create_all_find_comparison_plot(argv[1], argv[2], 'text') #711
    #create_all_find_comparison_plot(argv[1], argv[2], 'ppt') #368
    #create_all_find_comparison_plot(argv[1], argv[2], 'jpg') #362
    #create_all_find_comparison_plot(argv[1], argv[2], 'xls') #250
    #create_all_find_comparison_plot(argv[1], argv[2], 'gif') #67



if __name__ == '__main__':
    sys.exit(main())
