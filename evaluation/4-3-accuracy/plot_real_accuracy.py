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



def create_all_find_comparison_plot(csvfile, outfile, datatype=None, section=None, comparison=None):
    df = pd.read_csv(csvfile, delimiter=';')
    
    df = df.loc[(df['hash_comparison'] == comparison)]
    df['algorithm'] = '-original' # palette color
    
    
    if datatype:
    	df = df.loc[(df['datatype'] == datatype)]
    if section:
    	df = df.loc[(df['section'] == section)]
    
    
    if df.empty:
        return
    
    file_name = csvfile.split('/')[-1]
    file_name = file_name.split('.')[-2]
    
    sns.set_style('whitegrid')
    paper_rc = {'lines.linewidth': 1, 'lines.markersize': 1}
    sns.set_context("paper", rc = paper_rc, font_scale=2.5)

    df['result'] = df['result'].astype(int)          

    if 'PALETTE' in os.environ:
        palette = json.loads(os.getenv('PALETTE'))
        palette['-original'] = palette['-original']
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
    h = sns.boxplot(x='similarity', y='result', hue='algorithm', fliersize=0.75, data=df_delete, width=0.9, dodge=True, ax=axes[1], palette=palette)
    i = sns.boxplot(x='similarity', y='result', hue='algorithm', fliersize=0.75, data=df_insert, width=0.9, dodge=True, ax=axes[2], palette=palette)
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
    
    g.legend_.remove()
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


    outfile = ''.join(outfile.split('.')[:-1]) + '_' + file_name + '_' + comparison + '.pdf'

    plt.savefig(outfile)
    plt.close('all')
 


def main(argv=None):
    if argv is None:
        argv = sys.argv
    if len(argv) != 3:
        print('Usage: {prog} CSVFILE OUTFILE'.format(prog=argv[0]))
        return 1

    comparison_functions = ["ssdeep-original", "ssdeep-original-max", "ssdeep-original-opt", "ssdeep-original-opt-max", "ssdeep-4b", "ssdeep-4b-max", "ssdeep-4b-opt", "ssdeep-4b-opt-max"]

    for comparison in comparison_functions:
        create_all_find_comparison_plot(argv[1], argv[2], None, None, comparison)


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
