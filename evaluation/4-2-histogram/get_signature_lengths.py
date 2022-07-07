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


#python3 get_signature_lengths.py ../../corpus/nsrl_hashes/ ../../evaluation/database/hashes-100000*

def main(argv=None):
    if argv is None:
        argv = sys.argv
    if len(argv) < 2:
        print('Usage: {prog} NSRL-HASH-DIRECTORY CSV-HASHLIST-1 CSV-HASHLIST-2 ...'.format(prog=argv[0]))
        return 1
    s1_len = list()
    s2_len = list()
    s1ds2 = list()
    
    fullpath = argv[1]
    
    for path, dirs, files in os.walk(argv[1]):
        for filename in files:
            fullpath = os.path.join(path, filename)
            with open(fullpath, 'r') as f:
                hashes = f.readlines()
                for hash in hashes[1::]:
                    hash_without_filename = hash.split(',')[0]
                    hash_blocksize, s1, s2 = hash_without_filename.split(':')
                    s1_len.append(len(s1))
                    s2_len.append(len(s2))
                    s2l = len(s2)
                    if s2l == 0:
                       s2l = 1
                    s1ds2.append(len(s1)/s2l)
    print(len(s1_len))
    print("average signature 1 length:", sum(s1_len)/len(s1_len))
    print("average signature 2 length:", sum(s2_len)/len(s2_len))
    print("s1 is on average ", sum(s1ds2)/len(s1ds2), "times larger than s2")
    print("occurences of signature lenghts (sinature 1): ", dict((x,s1_len.count(x)) for x in set(s1_len)))
    print("occurences of signature lenghts (sinature 2): ", dict((x,s2_len.count(x)) for x in set(s2_len)))
    s1dict = { i : s1_len[i] for i in range(0, len(s1_len))}
    s2dict = { i : s2_len[i] for i in range(0, len(s2_len))}
    
    df1 = pd.DataFrame.from_dict(s1dict, orient='index', columns=['len1'])
    df2 = pd.DataFrame.from_dict(s2dict, orient='index', columns=['len2'])
    
    df12 = df1.join(df2, lsuffix='_caller', rsuffix='_other')
    df12['algorithm'] = 'original (NSRL)'
    df12['algorithm-id'] = 0
    
    all_df = pd.DataFrame()
    all_df = pd.concat([all_df, df12])
    i = 2
    for a in argv[2::]:
        algorithm = '-'.join(a.split('-')[2:-1:])
        print(a, algorithm)
        with open(a, 'r') as f:
            s1_len = list()
            s2_len = list()
            s1ds2 = list()
            hashes = f.readlines()
            for hash in hashes[1::]:
                hash_without_filename = hash.split(',')[0]
                hash_blocksize, s1, s2 = hash_without_filename.split(':')
                s1_len.append(len(s1))
                s2_len.append(len(s2))
                s2l = len(s2)
                if s2l == 0:
                    s2l = 1
                s1ds2.append(len(s1)/s2l)
            print("algorithm: ", algorithm)
            print("average signature 1 length:", sum(s1_len)/len(s1_len))
            print("average signature 2 length:", sum(s2_len)/len(s2_len))
            print("s1 is on average ", sum(s1ds2)/len(s1ds2), "times larger than s2")
            print("occurences of short second signatures: ", dict((x,s2_len.count(x)) for x in set(s2_len)))
            s1dict = { i : s1_len[i] for i in range(0, len(s1_len))}
            s2dict = { i : s2_len[i] for i in range(0, len(s2_len))}
    
            df1 = pd.DataFrame.from_dict(s1dict, orient='index', columns=['len1'])
            df2 = pd.DataFrame.from_dict(s2dict, orient='index', columns=['len2'])
            
            df12 = df1.join(df2, lsuffix='_caller', rsuffix='_other')
            df12['algorithm'] = algorithm
            df12['algorithm-id'] = i
            i += 1
            all_df = pd.concat([all_df, df12])
    all_df.to_csv('signature-lengths.csv', index=False)

if __name__ == "__main__":
    main()
