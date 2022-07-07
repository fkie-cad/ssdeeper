#!/usr/bin/env python3
# coding=utf-8
import json
import os
import sys
import matplotlib.pyplot as plt
from matplotlib.patches import PathPatch
import numpy as np
import pandas as pd
import seaborn as sns
from os.path import basename
from itertools import cycle
 
def plot_size_vs_runtime_4c(df, outfile, s):
    df = df.loc[(df['size'] == s)]
    #SPHF original 
    newdf1 = df.loc[(df['algorithm'] == 'ssdeep-original')]
    newdf1['algorithm'] = '-original'
    newdf2 = df.loc[(df['algorithm'] == 'ssdeep-original-opt')]
    newdf2['algorithm'] = '-nocommsub'
    newdf3 = df.loc[(df['algorithm'] == 'ssdeep-original-max')]
    newdf3['algorithm'] = '-nomax'
    newdf4 = df.loc[(df['algorithm'] == 'ssdeep-original-opt-max')]
    newdf4['algorithm'] = '-nocommsub-nomax'
    newdf1['size'] = 1
    newdf2['size'] = 2
    newdf3['size'] = 3
    newdf4['size'] = 4
    
    # SPHF original-refactored
    newdf5 = df.loc[(df['algorithm'] == 'ssdeep-original-refactored')]
    newdf6 = df.loc[(df['algorithm'] == 'ssdeep-original-opt-refactored')]
    newdf7 = df.loc[(df['algorithm'] == 'ssdeep-original-max-refactored')]
    newdf8 = df.loc[(df['algorithm'] == 'ssdeep-original-opt-max-refactored')]
    newdf5['size'] = 6
    newdf6['size'] = 7
    newdf7['size'] = 8
    newdf8['size'] = 9

    # SPHF refactored-polynomial
    newdf9 = df.loc[(df['algorithm'] == 'ssdeep-original-polynomial')]
    newdf10 = df.loc[(df['algorithm'] == 'ssdeep-original-opt-polynomial')]
    newdf11 = df.loc[(df['algorithm'] == 'ssdeep-original-max-polynomial')]
    newdf12 = df.loc[(df['algorithm'] == 'ssdeep-original-opt-max-polynomial')]
    newdf9['size'] = 11
    newdf10['size'] = 12
    newdf11['size'] = 13
    newdf12['size'] = 14

    # SPHF refactored-djb2
    newdf13 = df.loc[(df['algorithm'] == 'ssdeep-original-djb2')]
    newdf14 = df.loc[(df['algorithm'] == 'ssdeep-original-opt-djb2')]
    newdf15 = df.loc[(df['algorithm'] == 'ssdeep-original-max-djb2')]
    newdf16 = df.loc[(df['algorithm'] == 'ssdeep-original-opt-max-djb2')]
    newdf13['size'] = 16
    newdf14['size'] = 17
    newdf15['size'] = 18
    newdf16['size'] = 19

    # SPHF 4b
    newdf17 = df.loc[(df['algorithm'] == 'ssdeep-4b')]
    newdf18 = df.loc[(df['algorithm'] == 'ssdeep-4b-opt')]
    newdf19 = df.loc[(df['algorithm'] == 'ssdeep-4b-max')]
    newdf20 = df.loc[(df['algorithm'] == 'ssdeep-4b-opt-max')]
    newdf17['size'] = 21
    newdf18['size'] = 22
    newdf19['size'] = 23
    newdf20['size'] = 24

    # SPHF -refactored-4b
    newdf21 = df.loc[(df['algorithm'] == 'ssdeep-4b-refactored-4b')]               
    newdf22 = df.loc[(df['algorithm'] == 'ssdeep-4b-opt-refactored-4b')]
    newdf23 = df.loc[(df['algorithm'] == 'ssdeep-4b-max-refactored-4b')]
    newdf24 = df.loc[(df['algorithm'] == 'ssdeep-4b-opt-max-refactored-4b')]
    newdf21['size'] = 26
    newdf22['size'] = 27
    newdf23['size'] = 28
    newdf24['size'] = 29

    # SPHF -refactored-4b-polynomial
    newdf25 = df.loc[(df['algorithm'] == 'ssdeep-4b-4b-polynomial')]           
    newdf26 = df.loc[(df['algorithm'] == 'ssdeep-4b-opt-4b-polynomial')]
    newdf27 = df.loc[(df['algorithm'] == 'ssdeep-4b-max-4b-polynomial')]
    newdf28 = df.loc[(df['algorithm'] == 'ssdeep-4b-opt-max-4b-polynomial')]
    newdf25['size'] = 31
    newdf26['size'] = 32
    newdf27['size'] = 33
    newdf28['size'] = 34
    
    # SPHF -refactored-4b-djb2
    newdf29 = df.loc[(df['algorithm'] == 'ssdeep-4b-4b-djb2')]             
    newdf30 = df.loc[(df['algorithm'] == 'ssdeep-4b-opt-4b-djb2')]
    newdf31 = df.loc[(df['algorithm'] == 'ssdeep-4b-max-4b-djb2')]
    newdf32 = df.loc[(df['algorithm'] == 'ssdeep-4b-opt-max-4b-djb2')]
    newdf29['size'] = 36
    newdf30['size'] = 37
    newdf31['size'] = 38
    newdf32['size'] = 39
    
    df = pd.concat([newdf1, newdf2, newdf3, newdf4, newdf5, newdf6, newdf7, newdf8, newdf9, newdf10, newdf11, newdf12, newdf13, newdf14, newdf15, newdf16, newdf17, newdf18, newdf19, newdf20, newdf21, newdf22, newdf23, newdf24, newdf25, newdf26, newdf27, newdf28, newdf29, newdf30, newdf31, newdf32])
    
    sns.set_style('whitegrid')
    paper_rc = {'lines.linewidth': 1, 'lines.markersize': 0.5}
    sns.set_context("paper", rc = paper_rc, font_scale=1.9)
    
    if 'PALETTE' in os.environ:
        _palette = json.loads(os.getenv('PALETTE'))
        _palette['ssdeep-original-refactored'] = _palette['-original']
        _palette['ssdeep-original-opt-refactored'] = _palette['-nocommsub']
        _palette['ssdeep-original-max-refactored'] = _palette['-nomax']
        _palette['ssdeep-original-opt-max-refactored'] = _palette['-nocommsub-nomax']
        _palette['ssdeep-original-polynomial'] = _palette['-original']
        _palette['ssdeep-original-opt-polynomial'] = _palette['-nocommsub']
        _palette['ssdeep-original-max-polynomial'] = _palette['-nomax']
        _palette['ssdeep-original-opt-max-polynomial'] = _palette['-nocommsub-nomax']
        _palette['ssdeep-original-djb2'] = _palette['-original']
        _palette['ssdeep-original-opt-djb2'] = _palette['-nocommsub']
        _palette['ssdeep-original-max-djb2'] = _palette['-nomax']
        _palette['ssdeep-original-opt-max-djb2'] = _palette['-nocommsub-nomax']
        _palette['ssdeep-4b-4b-djb2'] = _palette['-original']
        _palette['ssdeep-4b-opt-4b-djb2'] = _palette['-nocommsub']
        _palette['ssdeep-4b-max-4b-djb2'] = _palette['-nomax']
        _palette['ssdeep-4b-opt-max-4b-djb2'] = _palette['-nocommsub-nomax']
        _palette['ssdeep-4b'] = _palette['-original']
        _palette['ssdeep-4b-opt'] = _palette['-nocommsub']
        _palette['ssdeep-4b-max'] = _palette['-nomax']
        _palette['ssdeep-4b-opt-max'] = _palette['-nocommsub-nomax']
        _palette['ssdeep-4b-refactored-4b'] = _palette['-original']
        _palette['ssdeep-4b-opt-refactored-4b'] = _palette['-nocommsub']
        _palette['ssdeep-4b-max-refactored-4b'] = _palette['-nomax']
        _palette['ssdeep-4b-opt-max-refactored-4b'] = _palette['-nocommsub-nomax']
        _palette['ssdeep-4b-4b-polynomial'] = _palette['-original']
        _palette['ssdeep-4b-opt-4b-polynomial'] = _palette['-nocommsub']
        _palette['ssdeep-4b-max-4b-polynomial'] = _palette['-nomax']
        _palette['ssdeep-4b-opt-max-4b-polynomial'] = _palette['-nocommsub-nomax']
    else: 
        _palette = sns.husl_palette(25, h=1, l=.7, s=.85)
        palette = [_palette[0], _palette[15], _palette[16], _palette[17]]

    fig, ax = plt.subplots(figsize=(20,7))
    
    g = sns.boxplot(x='size', y='time', hue='algorithm', fliersize=0.75, linewidth=0.5, data=df, width=0.9, dodge=False, order=np.arange(40), palette=_palette)
    g.set(xlabel="SPHF", ylabel="runtime in ms")
    
    g.set(ylim=(80,240))
    g.set(xlim=(-1,41))
    
    if s == 100000:
        g.set(ylim=(80,240))
    elif s == 10000:
        g.set(ylim=(5,40))
    elif s == 1000:
        g.set(ylim=(1,10))
    elif s == 100:
        g.set(ylim=(1,10))
    
    g.axes.tick_params(labelbottom=True, labeltop=False, labelleft=True, labelright=False, bottom=False, top=False, left=True, right=False)
    g.set_xticklabels(['', '             -original', '', '',
    			'', '', '             -refactored', '',
    			'', '', '', '             -refactored\n             -poly',
    			'', '', '', '',
    			'              -refactored\n              -djb2', '', '', '',
    			'', '              -4b', '', '',
    			'', '', '             -refactored\n             -4b', '',
    			'', '', '', '             -refactored\n            -4b\n             -poly',
    			'', '', '', '',
    			'               -refactored\n              -4b\n               -djb2', '', '', ''])
    
    h, l = g.get_legend_handles_labels()
    labels=['-original', '-nocommonsub', '-nomax', '-nocommonsub-nomax']
    legend1 = ax.legend(h[0:4], labels, loc='upper center', title='CF', markerscale=9., bbox_to_anchor=(1.13, +1.023), ncol=1, prop={'size': 16})
    
    labels=['-original', '-refactored', '-refactored-polynomial', '-refactored-djb2', '-4b', '-refactored-4b', '-refactored-4b-polynomial', '-refactored-4b-djb2']
    
    plt.tight_layout()
    g.axes.add_artist(legend1)
    plt.savefig(outfile)
    plt.close('all')    
 
 

       
def create_runtime_comparison_plot_combined(csvfile, outfile):
    df = pd.read_csv(csvfile, delimiter=';')
    
    df['time'] = df['time']/1000000
    plotname = 'ssdeep'
    newdf1 = df.loc[(df['algorithm'] == 'ssdeep-original')]             # sphf: ssdeep-original 
    newdf2 = df.loc[(df['algorithm'] == 'ssdeep-original-opt')]
    newdf3 = df.loc[(df['algorithm'] == 'ssdeep-original-max')]
    newdf4 = df.loc[(df['algorithm'] == 'ssdeep-original-opt-max')]

    newdf13 = df.loc[(df['algorithm'] == 'ssdeep-4b')]                 #sphf: ssdeep-4b
    newdf14 = df.loc[(df['algorithm'] == 'ssdeep-4b-opt')]
    newdf15 = df.loc[(df['algorithm'] == 'ssdeep-4b-max')]
    newdf16 = df.loc[(df['algorithm'] == 'ssdeep-4b-opt-max')]
    
    newdf9 = df.loc[(df['algorithm'] == 'ssdeep-original-polynomial')]           #sphf: ssdeep-refactored-polynomial
    newdf10 = df.loc[(df['algorithm'] == 'ssdeep-original-opt-polynomial')]
    newdf11 = df.loc[(df['algorithm'] == 'ssdeep-original-max-polynomial')]
    newdf12 = df.loc[(df['algorithm'] == 'ssdeep-original-opt-max-polynomial')]
    
    newdf5 = df.loc[(df['algorithm'] == 'ssdeep-original-djb2')]
    newdf6 = df.loc[(df['algorithm'] == 'ssdeep-original-opt-djb2')]
    newdf7 = df.loc[(df['algorithm'] == 'ssdeep-original-max-djb2')]
    newdf8 = df.loc[(df['algorithm'] == 'ssdeep-original-opt-max-djb2')]
    
    newdf21 = df.loc[(df['algorithm'] == 'ssdeep-4b-4b-polynomial')]             #sphf: ssdeep-refactored-4b-polynomial
    newdf22 = df.loc[(df['algorithm'] == 'ssdeep-4b-opt-4b-polynomial')]
    newdf23 = df.loc[(df['algorithm'] == 'ssdeep-4b-max-4b-polynomial')]
    newdf24 = df.loc[(df['algorithm'] == 'ssdeep-4b-opt-max-4b-polynomial')]
    
    newdf17 = df.loc[(df['algorithm'] == 'ssdeep-4b-4b-djb2')]             
    newdf18 = df.loc[(df['algorithm'] == 'ssdeep-4b-opt-4b-djb2')]
    newdf19 = df.loc[(df['algorithm'] == 'ssdeep-4b-max-4b-djb2')]
    newdf20 = df.loc[(df['algorithm'] == 'ssdeep-4b-opt-max-4b-djb2')]
    
    newdf31 = df.loc[(df['algorithm'] == 'ssdeep-original-refactored')]             # sphf: ssdeep-original 
    newdf32 = df.loc[(df['algorithm'] == 'ssdeep-original-opt-refactored')]
    newdf33 = df.loc[(df['algorithm'] == 'ssdeep-original-max-refactored')]
    newdf34 = df.loc[(df['algorithm'] == 'ssdeep-original-opt-max-refactored')]

    newdf35 = df.loc[(df['algorithm'] == 'ssdeep-4b-refactored-4b')]                 #sphf: ssdeep-4b
    newdf36 = df.loc[(df['algorithm'] == 'ssdeep-4b-opt-refactored-4b')]
    newdf37 = df.loc[(df['algorithm'] == 'ssdeep-4b-max-refactored-4b')]
    newdf38 = df.loc[(df['algorithm'] == 'ssdeep-4b-opt-max-refactored-4b')]

    all_df = [newdf1, newdf2, newdf3, newdf4, newdf5, newdf6, newdf7, newdf8, newdf9, newdf10, newdf11, newdf12, newdf13, newdf14, newdf15, newdf16, newdf17, newdf18, newdf19, newdf20, newdf21, newdf22, newdf23, newdf24, newdf31, newdf32, newdf33, newdf34, newdf35, newdf36, newdf37, newdf38]
    
    
    df_total = pd.DataFrame()
    for df in all_df:
        algo = df.at[df.index.tolist()[0], 'algorithm']
        df100 = df.loc[(df['size'] == 100)]
        df100 = df100.groupby('filename').mean()
        df1000 = df.loc[(df['size'] == 1000)]
        df1000 = df1000.groupby('filename').mean()
        df10000 = df.loc[(df['size'] == 10000)]
        df10000 = df10000.groupby('filename').mean()
        df100000 = df.loc[(df['size'] == 100000)]
        df100000 = df100000.groupby('filename').mean()
        df = pd.concat([df100, df1000, df10000, df100000])
        df['algorithm'] = algo 
        print('algo -', algo, df100000['time'].mean())
        df_total = pd.concat([df_total, df])

          
    for s in [100, 1000, 10000, 100000]:
        plot_name = ''.join(outfile.split('.')[:-1]) + '_' + str(s) + '.pdf'
        plot_size_vs_runtime_4c(df_total, plot_name, s)
        

def main(argv=None):
    if argv is None:
        argv = sys.argv
    if len(argv) != 3:
        print('Usage: {prog} CSVFILE OUTFILE'.format(prog=argv[0]))
        return 1
    create_runtime_comparison_plot_combined(argv[1], argv[2])

if __name__ == '__main__':
    sys.exit(main())
