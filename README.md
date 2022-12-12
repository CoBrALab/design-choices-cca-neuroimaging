# Canonical Correlation Analyses

## Purpose
These scripts were designed to perform data reduction in matrix format and run canonical correlation analysis (CCA). This process consists of three optional steps:
  1. Either principal componen analysis (PCA) or independent component analysis (ICA) can be performed on vertexwise CT files from CIVET.
  2. Spectral clustering can be used to parcellate the data of a single .obj file from CIVET, and the result can be transformed to vertexwise files from CIVET.
  3. CCA accepts two datasets in matrix format (one from either step 1 or 2) and performs the input number of runs with permutations of this data.

## Use
Many iterations of the canonical correaltion analyses can be computationally expensive, so it is recommended to perform larger number of iterations on a capable machine or on the Niagara environment as individual jobs.

## Example
Two small example files are included in the repo: example_demographics1.feather and example_demographics1.feather. These two file have been preprocessed and z-scored.

After cloning this repo using the git clone command:
*git clone _*

The conda environment with all dependencies can be set-up using the spec-file.txt:
*conda install --name myenv --file spec-file.txt*

Within this environment cca can be run from the command line using:
*python ./load_files_and_run_cca_function.py examplefile1.feather examplefile2.feather 2 1 outputfolder*
where 2 is the number of canonical components to keep and 1 is the iteration number.

The resulting 2x1 csv file will be saved in the specified output folder.
