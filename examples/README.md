## Example
Two small example files are included in the repo: example_demographics1.feather and example_demographics1.feather. Both example files contain two different demographic measures, which have been preprocessed and z-scored. 

Demographics File 1:
Measure #1 | Measure #2
--- | --- 
-0.894 | 0.779
-0.821 | 0.119 
-0.675 | 0.424 
... | ... 

Demographics File 2:
Measure #3 | Measure #4
--- | --- 
-1.424 | -0.567
-1.067 | -0.505 
-0.425 | -1.188 
... | ... 


After cloning this repo using the git clone command:
<pre><code>git clone _
</code></pre>

The conda environment with all dependencies can be set-up using the command:
<pre><code>conda env create -f environment.yml
</code></pre>

Within this environment cca can be run from the command line using:
<pre><code>python ./load_files_and_run_cca_function.py examplefile1.feather examplefile2.feather 2 1 outputfolder
</code></pre>
where 2 is the number of canonical components to keep and 1 is the iteration number.

The resulting 2x1 csv file will be saved in the specified output folder. If multiple iterations are run, they will be saved to separate outputfiles within the same folder.

CCs
--- |  
0.103 |
0.014 |
