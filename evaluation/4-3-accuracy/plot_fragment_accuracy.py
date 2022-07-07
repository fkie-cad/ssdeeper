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
    	       df51, df52, df53, df54, df61, df62, df63, df64, #df71, df72, df73, df74, 
    	       df81, df82, df83, df84]
    
    more_dfs = pd.DataFrame()
    positions = list()
    i = 1
    j = 0
    for d in all_dfs:
        #a = d.loc[(d['size'] == 95)]
        #a['size2'] = i
        b = d.loc[(d['size'] == 90)]
        b['size2'] = i
        c = d.loc[(d['size'] == 75)]
        c['size2'] = i+40
        e = d.loc[(d['size'] == 50)]
        e['size2'] = i+80
        f = d.loc[(d['size'] == 25)]
        f['size2'] = i+120
        positions.extend([i, i+40, i+80, i+120])
        i += 1
        j += 1
        if j % 4 == 0:
           i += 1
        more_dfs = pd.concat([more_dfs, b, c, e, f])
    
    df = pd.concat([more_dfs])
    
    if datatype:
    	df = df.loc[(df['datatype'] == datatype)]
    	outfile = ''.join(outfile.split('.')[:-1]) + '_' + datatype + '.pdf'
    if section:
    	df = df.loc[(df['section'] == section)]
    	outfile = ''.join(outfile.split('.')[:-1]) + '_' + section + '.pdf'
    
    sns.set_style('whitegrid')
    paper_rc = {'lines.linewidth': 1, 'lines.markersize': 1}
    sns.set_context("paper", rc = paper_rc, font_scale=2.5)

    fig, ax = plt.subplots(figsize=(8,3))
    ax.tick_params(labelbottom=False, labeltop=True, labelleft=True, labelright=True, bottom=False, top=False, left=True, right=True)
    ax.xaxis.set_label_position('bottom')
    
    df['size'] = df['size'].replace(95, 5)
    df['size'] = df['size'].replace(90, 10)
    df['size'] = df['size'].replace(75, 26)
    df['size'] = df['size'].replace(25, 75)
    df['size'] = df['size'].replace(26, 25)
    #df = df.loc[(df['size'] > 20)]

    df['size'] = df['size'].astype(int)
    df['result'] = df['result'].astype(int)          

    if 'PALETTE' in os.environ:
        palette = json.loads(os.getenv('PALETTE'))
        palette['-refactored-4b-djb2'] = palette['-original']
        palette['-refactored-4b-djb2-opt'] = palette['-nocommsub']
        palette['-refactored-4b-djb2-max'] = palette['-nomax']
        palette['-refactored-4b-djb2-opt-max'] = palette['-nocommsub-nomax']
        palette['-refactored-4b-poly'] = palette['-original']
        palette['-refactored-4b-poly-opt'] = palette['-nocommsub']
        palette['-refactored-4b-poly-max'] = palette['-nomax']
        palette['-refactored-4b-poly-opt-max'] = palette['-nocommsub-nomax']
        palette['-refactored-4b'] = palette['-original']
        palette['-refactored-4b-opt'] = palette['-nocommsub']
        palette['-refactored-4b-max'] = palette['-nomax']
        palette['-refactored-4b-opt-max'] = palette['-nocommsub-nomax']
        palette['-4b'] = palette['-original']
        palette['-4b-opt'] = palette['-nocommsub']
        palette['-4b-max'] = palette['-nomax']
        palette['-4b-opt-max'] = palette['-nocommsub-nomax']
        palette['-refactored-djb2'] = palette['-original']
        palette['-refactored-djb2-opt'] = palette['-nocommsub']
        palette['-refactored-djb2-max'] = palette['-nomax']
        palette['-refactored-djb2-opt-max'] = palette['-nocommsub-nomax']
        palette['-refactored-poly'] = palette['-original']
        palette['-refactored-poly-opt'] = palette['-nocommsub']
        palette['-refactored-poly-max'] = palette['-nomax']
        palette['-refactored-poly-opt-max'] = palette['-nocommsub-nomax']
        palette['-refactored'] = palette['-original']
        palette['-refactored-nocommsub'] = palette['-nocommsub']
        palette['-refactored-max'] = palette['-nomax']
        palette['-refactored-opt-max'] = palette['-nocommsub-nomax']
    else:
        _palette = sns.husl_palette(25, h=1, l=.7, s=.85)
        palette = [_palette[0], _palette[15], _palette[16], _palette[17]]

    g = sns.boxplot(x='size2', y='result', hue='algorithm', ax=ax, fliersize=0.75 ,data=df, width=0.9, dodge=False, order=np.arange(157), palette=palette)
    g.set(ylim=(-2,102))
    g.set(xlim=(-3,157))
    
    fig.set_figheight(17)
    fig.set_figwidth(30)

    g.set(xlabel="SPHF", ylabel="similarity output")
    g.axes.tick_params(labelbottom=True, labeltop=False, labelleft=True, labelright=True, bottom=False, top=False, left=True, right=True)
    g.set_xticklabels(['', '', '', '-original', '', '', '', '', '-refactored', 
                       '', '', '', '', '-refactored-poly', '', '', '', '', '-refactored-djb2',
                       '', '', '', '', '-4b', '', '', '', '', '-refactored-4b', '', '', '', '', '-refactored-4b-djb2',
                       '', '', '', '', '', '', '', '', '','-original', '', '', '', '', '-refactored',
                       '', '', '', '', '-refactored-poly', '', '', '', '', '-refactored-djb2',
                       '', '', '', '', '-4b', '', '', '', '', '-refactored-4b', '', '', '', '',
                       '-refactored-4b-djb2' , '', '', '', '', '', '', '', '', '', '-original',
                       '', '', '', '', '-refactored', '', '', '', '', '-refactored-poly',
                       '', '', '', '', '-refactored-djb2', '', '', '', '', '-4b', '', '', '', '', '-refactored-4b',
                       '', '', '', '', '-refactored-4b-djb2', '', '', '', '', '', '', '', '', '', '-original',
                       '', '', '', '', '-refactored', '', '', '', '', '-refactored-poly', '', '', '', '',
                       '-refactored-djb2', '', '', '', '', '-4b', '', '', '', '', '-refactored-4b',
                       '', '', '', '', '-refactored-4b-djb2', '', '', ''], rotation=45, ha='right')

    plt.text(16,104, ' 10', fontsize=22)
    plt.text(56,104, ' 25', fontsize=22)
    plt.text(96,104, '50', fontsize=22)
    plt.text(136,104, '75', fontsize=22)
    plt.text(53,109, ' fragment size in percent relative to the original file', fontsize=23)

    h, l = g.get_legend_handles_labels()
    labels=['-original', '-nocommonsub', '-nomax', '-nocommonsub-nomax']
    #legend1 = ax.legend(h[0:4], labels, loc='upper center', title='CF', markerscale=9., bbox_to_anchor=(0.153, +1.24), ncol=2, prop={'size': 22})
    legend1 = ax.legend(h[0:4], labels, loc='upper center', title='CF', markerscale=9., bbox_to_anchor=(0.50, +1.22), ncol=4, prop={'size': 22})
    
    plt.tight_layout()
    g.axes.add_artist(legend1)

    plt.savefig(outfile)
    plt.close('all')
 


def main(argv=None):
    if argv is None:
        argv = sys.argv
    if len(argv) != 3:
        print('Usage: {prog} CSVFILE OUTFILE'.format(prog=argv[0]))
        return 1

    create_all_find_comparison_plot(argv[1], argv[2], None, None)
    return
    create_all_find_comparison_plot(argv[1], argv[2], None, 'first')
    create_all_find_comparison_plot(argv[1], argv[2], None, 'second')
    create_all_find_comparison_plot(argv[1], argv[2], None, 'third')
    create_all_find_comparison_plot(argv[1], argv[2], 'pdf') #1073
    create_all_find_comparison_plot(argv[1], argv[2], 'html') #1093
    create_all_find_comparison_plot(argv[1], argv[2], 'doc') #533
    create_all_find_comparison_plot(argv[1], argv[2], 'text') #711
    create_all_find_comparison_plot(argv[1], argv[2], 'ppt') #368
    create_all_find_comparison_plot(argv[1], argv[2], 'jpg') #362
    create_all_find_comparison_plot(argv[1], argv[2], 'xls') #250
    create_all_find_comparison_plot(argv[1], argv[2], 'gif') #67



if __name__ == '__main__':
    sys.exit(main())
