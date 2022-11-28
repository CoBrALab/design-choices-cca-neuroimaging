# Canonical Correlation Analyses

## Purpose
These scripts were designed to perform data reduction in matrix format and run canonical correlation analysis (CCA). This process consists of three optional steps:
  1. Either principal componen analysis (PCA) or independent component analysis (ICA) can be performed on vertexwise CT files from CIVET.
  2. Spectral clustering can be used to parcellate the data of a single .obj file from CIVET, and the result can be transformed to vertexwise files from CIVET.
  3. CCA accepts two datasets in matrix format (one from either step 1 or 2) and performs the input number of runs with permutations of this data.

## Use
Many iterations of the canonical correaltion analyses can be computationally expensive, so it is recommended to perform larger number of iterations on a capable machine or on the Niagara environment as individual jobs.
