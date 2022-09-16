#!/usr/bin/env python
# coding: utf-8

#a simple funtion which runs permutations of CCA (shuffled) that can be called from niagara using the slurm module

import pandas as pd
from sklearn.cross_decomposition import CCA
from sklearn.utils import resample
from sklearn.utils import shuffle
import numpy as np
import random
from sklearn.preprocessing import StandardScaler

def run_shuffled_cca(ddata,vdata,n_cca_components,iter):
    demographics_shuffled, vertexes_shuffled = shuffle(ddata, vdata, random_state=iter)
    #vertexes_shuffled = shuffle(vertexes)
    cca_model_shuffled = CCA(n_components=n_cca_components)
    cca_model_shuffled.fit(ddata,vertexes_shuffled)
    #coefficients_temp = cca_model_shuffled.coef_
    #X_loadings_temp = cca_model_shuffled.x_loadings_
    #Y_loadings_temp = cca_model_shuffled.y_loadings_
    test1_c, test2_c = cca_model_shuffled.transform(ddata, vertexes_shuffled)
    testcorrs = np.corrcoef(test1_c.T, test2_c.T).diagonal(offset=cca_model_shuffled.n_components)
    return testcorrs