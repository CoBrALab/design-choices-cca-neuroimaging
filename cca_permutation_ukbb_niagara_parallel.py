#!/usr/bin/env python
# coding: utf-8


import os
import re
import glob
import pandas as pd
import csv
import sys
from sklearn.cross_decomposition import CCA
from sklearn.utils import resample
from sklearn.utils import shuffle
import numpy as np
import time
import random
import run_cca_function
from sklearn.preprocessing import StandardScaler
from scipy.stats import zscore


import warnings
warnings.filterwarnings('ignore')


import multiprocessing as mp
print("Number of processors: ", mp.cpu_count())
pool = mp.Pool(mp.cpu_count())
results = []

bootstrap_iters = 500
n_cca_components = 52


#read in other demographic data to pandas dataframe
demographics_data_filename = r'ukb46307_with_civet_reduced.tab'
#approved_col_list = ['CCID', 'homeint_handedness', 'additional_qual','homeint_v349']

demographics_data = pd.read_csv(demographics_data_filename, header=0,  index_col='f.eid', sep='\t')
#approved_data = load_approved_data.load_approved_data(approved_data_filename)



all_ids = demographics_data.index.tolist()
print("Participants: " + str(len(all_ids)))



demographics_data = demographics_data.drop(columns=['countnull'])


demo_cols = demographics_data.columns


col_name_dict_file = r'ColumnHeaders-WrittenNames-Shortform.csv'
col_readable_name_dict = pd.read_csv(col_name_dict_file, header=None, index_col=0, squeeze=True).to_dict()

#list of caregorical cols
demo_cols_categorical = ['f.31.0.0','f.971.2.0', 'f.981.2.0', 'f.991.2.0', 'f.1001.2.0', 'f.1011.2.0', 'f.1021.2.0', 'f.1031.2.0', 'f.1249.2.0', 'f.1259.2.0', 'f.2634.2.0', 'f.3393.2.0', 'f.3637.2.0', 'f.3647.2.0', 'f.4792.2.0', 'f.4803.2.0', 'f.6160.2.1', 'f.6160.2.2', 'f.6160.2.3', 'f.6160.2.4', 'f.20160.2.0']

#add category to encompass nulls
for col_name in  demo_cols:
    if col_name in demo_cols_categorical:
        #change column type to category
        demographics_data[col_name] = demographics_data[col_name].astype('category')
        if 0 in demographics_data[col_name].cat.categories:
            if -1 in demographics_data[col_name].cat.categories:
                demographics_data[col_name] = demographics_data[col_name].cat.add_categories('-1.0').fillna('-1.0')
            else:
                demographics_data[col_name] = demographics_data[col_name].cat.add_categories('-4.0').fillna('-4.0')
        else:
            demographics_data[col_name] = demographics_data[col_name].cat.add_categories('0').fillna('0')
        #demographics_data[col_name] = demographics_data[col_name].cat.add_categories('-1.0').fillna('-1.0')
    else:
        demographics_data[col_name] = demographics_data[col_name].fillna(demographics_data[col_name].mean())
        demographics_data[col_name] = zscore(demographics_data[col_name])

demographics_data = demographics_data.replace(np.nan,demographics_data.mean())


#read in pca of vertices
component_file_location = r'all_600_pcas_vertex.csv'
vertexes_data = pd.read_csv(component_file_location, header=None, index_col=0)#.transpose()


print(vertexes_data.shape)
print(demographics_data.shape)


demographics_data = pd.merge(vertexes_data,demographics_data,how="inner",left_index=True,right_index=True)[demo_cols]


vertexes_data.sort_index(inplace=True, ascending=True)
demographics_data.sort_index(inplace=True, ascending=True)


print(vertexes_data.shape)
print(demographics_data.shape)


# corrcoefs_bstrap = np.zeros((n_cca_components, bootstrap_iters))
# print(corrcoefs_bstrap.shape)
# fwe_vals = np.zeros((n_cca_components,1))
# count_bins=np.zeros(10)


print(time.ctime(time.time()))

results = [pool.apply(run_cca_function.run_shuffled_cca, args=(demographics_data, vertexes_data, n_cca_components, b_iter)) for b_iter in range(0,bootstrap_iters)]

        
print(time.ctime(time.time()))
print(results)

corrcoefs_bstrap_fileout = r'corrcoefs_bstrap_.csv'
with open(corrcoefs_bstrap_fileout, 'w') as f:
    cwriter = csv.writer(f, delimiter=',', lineterminator='\n')
    cwriter.writerows(results)

pool.close()
pool.join()

print("Pool is closed")
