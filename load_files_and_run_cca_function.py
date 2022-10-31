#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sklearn.cross_decomposition import CCA
from sklearn.utils import resample
from sklearn.utils import shuffle
import numpy as np
import random
import feather
from sklearn.preprocessing import StandardScaler

def run_shuffled_cca(ddata,vdata,n_cca_components,iteri,outfolder):
    
    #Initialize number of components for CCA and the current bootstrap iteration
    n_cca_components = int(n_cca_components)
    iteri = int(iteri)
    
    #Read in vertices and demographic files
    vertexes_data = pd.read_feather(vdata)
    #print(vertexes_data.shape)
    demographics_data = pd.read_feather(ddata)
    #print(demographics_data.shape)
    
    #shuffle data (break linkages)
    vertexes_shuffled = shuffle(vertexes_data, random_state=iteri)
    
    #Create and run CCA model
    cca_model_shuffled = CCA(n_components=n_cca_components)
    cca_model_shuffled.fit(demographics_data,vertexes_shuffled)
    
    #Calculate correlation coefficient
    test1_c, test2_c = cca_model_shuffled.transform(demographics_data, vertexes_shuffled)
    testcorrs = np.corrcoef(test1_c.T, test2_c.T).diagonal(offset=cca_model_shuffled.n_components)
    
    #Save coeeficient to file
    np.savetxt(outfolder + "//bootstrapcorrcoef" + str(iteri) + ".csv", testcorrs, delimiter=",")


if __name__ == "__main__":
    import sys
    run_shuffled_cca(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
