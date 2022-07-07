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

    
def plot_size_vs_runtime_4(df1, df2, outfile, size):
    df = pd.concat([df1, df2])
    df = df.loc[(df['size'] == size)]

    newdf1 = df.loc[(df['algorithm'] == 'ssdeep-original')]             # sphf: ssdeep-original 
    newdf1['algorithm'] = '-original'
    newdf2 = df.loc[(df['algorithm'] == 'ssdeep-original-opt')]
    newdf2['algorithm'] = '-nocommsub'
    newdf3 = df.loc[(df['algorithm'] == 'ssdeep-original-max')]
    newdf3['algorithm'] = '-nomax'
    newdf4 = df.loc[(df['algorithm'] == 'ssdeep-original-opt-max')]
    newdf4['algorithm'] = '-nocommsub-nomax'
    newdf5 = df.loc[(df['algorithm'] == 'ssdeep-original-pa')]
    newdf5['algorithm'] = '-nopa'
    newdf6 = df.loc[(df['algorithm'] == 'ssdeep-original-opt-pa')]
    newdf6['algorithm'] = '-nocommsub-nopa'
    newdf7 = df.loc[(df['algorithm'] == 'ssdeep-original-pa-max')]
    newdf7['algorithm'] = '-nopa-nomax'
    newdf8 = df.loc[(df['algorithm'] == 'ssdeep-original-opt-pa-max')]
    newdf8['algorithm'] = '-nocommsub-nopa-nomax'
    newdf1['size'] = 1
    newdf2['size'] = 2
    newdf3['size'] = 3
    newdf4['size'] = 4
    newdf5['size'] = 5
    newdf6['size'] = 6
    newdf7['size'] = 7
    newdf8['size'] = 8
    
    df1 = pd.concat([newdf1, newdf2, newdf3, newdf4, newdf5, newdf6, newdf7, newdf8])

    newdf11 = df.loc[(df['algorithm'] == 'ssdeep-4b')]                 #sphf: ssdeep-4b
    newdf11['algorithm'] = '-4b'
    newdf12 = df.loc[(df['algorithm'] == 'ssdeep-4b-opt')]
    newdf12['algorithm'] = '-4b-nocommsub'
    newdf13 = df.loc[(df['algorithm'] == 'ssdeep-4b-max')]
    newdf13['algorithm'] = '-4b-nomax'
    newdf14 = df.loc[(df['algorithm'] == 'ssdeep-4b-opt-max')]
    newdf14['algorithm'] = '-4b-nocommsub-nomax'
    newdf15 = df.loc[(df['algorithm'] == 'ssdeep-4b-pa')]
    newdf15['algorithm'] = '-4b-nopa'
    newdf16 = df.loc[(df['algorithm'] == 'ssdeep-4b-opt-pa')]
    newdf16['algorithm'] = '-4b-nocommsub-nopa'
    newdf17 = df.loc[(df['algorithm'] == 'ssdeep-4b-pa-max')]
    newdf17['algorithm'] = '-4b-nopa-nomax'
    newdf18 = df.loc[(df['algorithm'] == 'ssdeep-4b-opt-pa-max')]
    newdf18['algorithm'] = '-4b-nocommsub-nopa-nomax'
    newdf11['size'] = 11
    newdf12['size'] = 12
    newdf13['size'] = 13
    newdf14['size'] = 14
    newdf15['size'] = 15
    newdf16['size'] = 16
    newdf17['size'] = 17
    newdf18['size'] = 18
    
    df2 = pd.concat([newdf11, newdf12, newdf13, newdf14, newdf15, newdf16, newdf17, newdf18])
    df = pd.concat([df1, df2])
    
    sns.set_style('whitegrid')
    paper_rc = {'lines.linewidth': 1, 'lines.markersize': 0.5}
    sns.set_context("paper", rc = paper_rc, font_scale=2.4)
        
    fig, ax = plt.subplots(figsize=(25,7)) 
    
    if 'PALETTE' in os.environ:
        palette1 = json.loads(os.getenv('PALETTE'))
        palette1['-4b-nocommsub-nopa-nomax'] = palette1['-nocommsub-nopa-nomax']
        palette1['-4b-nopa-nomax'] = palette1['-nopa-nomax']
        palette1['-4b-nocommsub-nopa'] = palette1['-nocommsub-nopa']
        palette1['-4b-nopa'] = palette1['-nopa']
        palette1['-4b-nocommsub-nomax'] = palette1['-nocommsub-nomax']
        palette1['-4b-nomax'] = palette1['-nomax']
        palette1['-4b-nocommsub'] = palette1['-nocommsub']
        palette1['-4b'] = palette1['-original']
    else: 
        _palette = sns.husl_palette(25, h=1, l=.7, s=.85)
        palette1 = [_palette[0], _palette[16], _palette[17], _palette[18], _palette[20], _palette[21], _palette[22], _palette[23]]
    
    g = sns.boxplot(x='size', y='time', hue='algorithm', fliersize=0.75, data=df, width=0.9, dodge=False, order=np.arange(19), palette=palette1)

    g.set(xlabel="SPHF", ylabel="runtime in ms")
    g.set(xlim=(0,19))
    if size == 100000:
        g.set(ylim=(60,680))
    elif size == 10000:
        g.set(ylim=(1,70))
    elif size == 1000:
        g.set(ylim=(1,10))
    elif size == 100:
        g.set(ylim=(1,3.5))

    g.axes.tick_params(labelbottom=True, labeltop=False, labelleft=True, labelright=False, bottom=False, top=False, left=True, right=False)
    g.set_xticklabels(['', '', '', '                          -original', '', '', '', '', '', '', '', '', '',  '', '         -4b', '', '', '', ''])
    
    h, l = g.get_legend_handles_labels()
    labels=['-original', '-nocommonsub', '-nomax', '-nocommonsub-nomax', '-nopa', '-nocommonsub-nopa', '-nopa-nomax', '-nocommonsub-nopa-nomax']
    legend1 = ax.legend(h[0:8], labels, loc='upper center', title='CF', markerscale=11., bbox_to_anchor=(1.2, +1.025), ncol=1, prop={'size': 22})
    
    plt.tight_layout()
    g.axes.add_artist(legend1)
    plt.savefig(outfile)
    plt.close('all')    


def create_runtime_comparison_plot(csvfile, o):
    df = pd.read_csv(csvfile, delimiter=';')
    df['size'] = df['size']
    df['time'] = df['time']/1000000
    plotname = 'ssdeep'
    newdf1 = df.loc[(df['algorithm'] == 'ssdeep-original')]             # sphf: ssdeep-original 
    newdf2 = df.loc[(df['algorithm'] == 'ssdeep-original-opt')]
    newdf3 = df.loc[(df['algorithm'] == 'ssdeep-original-max')]
    newdf4 = df.loc[(df['algorithm'] == 'ssdeep-original-opt-max')]
    newdf5 = df.loc[(df['algorithm'] == 'ssdeep-original-pa')]
    newdf6 = df.loc[(df['algorithm'] == 'ssdeep-original-opt-pa')]
    newdf7 = df.loc[(df['algorithm'] == 'ssdeep-original-pa-max')]
    newdf8 = df.loc[(df['algorithm'] == 'ssdeep-original-opt-pa-max')]

    newdf11 = df.loc[(df['algorithm'] == 'ssdeep-4b')]                 #sphf: ssdeep-4b
    newdf12 = df.loc[(df['algorithm'] == 'ssdeep-4b-opt')]
    newdf13 = df.loc[(df['algorithm'] == 'ssdeep-4b-max')]
    newdf14 = df.loc[(df['algorithm'] == 'ssdeep-4b-opt-max')]
    newdf15 = df.loc[(df['algorithm'] == 'ssdeep-4b-pa')]
    newdf16 = df.loc[(df['algorithm'] == 'ssdeep-4b-opt-pa')]
    newdf17 = df.loc[(df['algorithm'] == 'ssdeep-4b-pa-max')]
    newdf18 = df.loc[(df['algorithm'] == 'ssdeep-4b-opt-pa-max')]

    all_df1 = [newdf1, newdf2, newdf3, newdf4, newdf5, newdf6, newdf7, newdf8]
    all_df2 = [newdf11, newdf12, newdf13, newdf14, newdf15, newdf16, newdf17, newdf18]
    
    df_total1 = pd.DataFrame()
    for df in all_df1:
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
        print(algo, df100000['time'].mean())
        df_total1 = pd.concat([df_total1, df])
    
    df_total2 = pd.DataFrame()    
    for df in all_df2:
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
        print(algo, df100000['time'].mean())
        df_total2 = pd.concat([df_total2, df])

    for s in [100, 1000, 10000, 100000]:
        plot_name = ''.join(o.split('.')[:-1]) + '_' + str(s) + '.pdf'
        plot_size_vs_runtime_4(df_total1, df_total2, plot_name, s)



def main(argv=None):
    if argv is None:
        argv = sys.argv
    if len(argv) != 3:
        print('Usage: {prog} CSVFILE OUTFILE'.format(prog=argv[0]))
        return 1
    create_runtime_comparison_plot(argv[1], argv[2])

if __name__ == '__main__':
    sys.exit(main())
