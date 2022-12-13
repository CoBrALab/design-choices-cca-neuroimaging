# Canonical Correlation Analyses
Canonical correlation analysis (CCA) is used to identify and measure the associations among two sets of variables while maximizing correlation. Canonical correlation can be used in place of multiple regression, but accounts for scenarios where there are multiple intercorrelated outcome variables.

## Purpose
These scripts were designed to perform data reduction in matrix format and run canonical correlation analysis (CCA). This process consists of three optional steps:
  1. Either principal componen analysis (PCA) or independent component analysis (ICA) can be performed on a matrix stored in .csv format, with values for the left and right brain hemispheres being stored in separate files. Note: This program is was designed to use the vertexwise cortical thickness files from CIVET (https://www.bic.mni.mcgill.ca/ServicesSoftware/CIVET) but can use input matrices of any size.
  2. Spectral clustering can be used to parcellate the data of a single .obj file and assign each vertex to an individual group. Note: This implementation was designed to use the .obj file containing surface area vertices from CIVET and the result is a brain parcellation which can then be applied to further vertexwise files from CIVET.
  3. CCA accepts two datasets in matrix format (one can be obtained from the results of either step 1 or 2 but does not need to be) and performs the input number of runs with permutations of this data.

## Usage
Running many iterations of the canonical correaltion analysis may be computationally expensive dependning on the size of the dataset and the number of iterations, so it is recommended to perform larger number of iterations on a capable machine or on a distributed environment so that multiple iterations can be run simultaneously. Example input and instructions are provided in the example folder. 

## Dependencies 
The python libraries used to implement these fuctionalities include:

sklearn (https://scikit-learn.org/stable/)

pandas (https://pandas.pydata.org/)

numpy (https://numpy.org/)

feather (https://arrow.apache.org/docs/python/feather.html)

Spectral clustering requires the following additional library:

vtk (https://vtk.org/)
