# -*- coding: utf-8 -*-

#modified version of the spectral clustering for brain vertex files from https://pubmed.ncbi.nlm.nih.gov/33857618/

from os import path
import sys
from optparse import OptionParser
import numpy as np
import vtk
from vtk.util import numpy_support
from sklearn.cluster import SpectralClustering


#specify the brain object file to be used and the number of parcels desired
obj_filename = "lh_average.obj"
num_parcels = 180 #int(sys.argv[0])

def myreadMeshFile(filename, clean=True, verbose=False, recompute_normals=True):
    """Read mesh file.
    The input format is determined by file name extension.
    Polygons get split into triangles to support various restrictive output
    formats.
    If clean, degenerate data gets removed."""

    informat = path.splitext(filename)[1].strip('.')
    # set reader based on filename extension
    if informat=='stl':
        reader = vtk.vtkSTLReader()
    elif informat=='vtk':
        reader = vtk.vtkPolyDataReader()
    elif informat=='obj':
        reader = vtk.vtkMNIObjectReader()
    elif informat=='ply':
        reader = vtk.vtkPLYReader()
    elif informat=='vtp':
        reader = vtk.vtkXMLPolyDataReader()
    #elif informat=='tag':
    #    reader = vtk.vtkMNITagPointReader()
    else:
        raise ValueError('cannot read input format: ' + informat)
    reader.SetFileName(filename)
    reader.Update()

    if verbose:
        print("read %i polygons from file %s" % \
                               (reader.GetOutput().GetNumberOfPolys(), filename))

    # merge duplicate points, and/or remove unused points and/or remove degenerate cells
    if clean:
        polydata = vtk.vtkCleanPolyData()
        polydata.SetInputConnection(reader.GetOutputPort())
        poly_data_algo = polydata
        if verbose:
            print("cleaned poly data")
    else:
        poly_data_algo = reader

    # convert input polygons and strips to triangles
    triangles = vtk.vtkTriangleFilter()
    triangles.SetInputConnection(poly_data_algo.GetOutputPort())
    
    
    #ADDDED
    polydata = reader.GetOutput()
    points = polydata.GetPoints()
    return points
    ####

    if recompute_normals:
        normals = vtk.vtkPolyDataNormals()
        normals.SetInputConnection(triangles.GetOutputPort())

        normals.SplittingOff()
        normals.ComputePointNormalsOn()
        normals.AutoOrientNormalsOn()
        normals.ConsistencyOn()
        normals.NonManifoldTraversalOn()
        if verbose:
            print("recomputed normals")
            print("finished reading", filename)
        return normals
    else:
        if verbose:
            print("finished reading", filename)
        return triangles

brain_triangles = myreadMeshFile(obj_filename, recompute_normals=False)
#print(brain_triangles)

as_numpy = numpy_support.vtk_to_numpy(brain_triangles.GetData())
#print(len(as_numpy))

#run spectral clustering
clustering = SpectralClustering(n_clusters=num_parcels,assign_labels='discretize',random_state=0).fit(as_numpy)

#save output (text file with each vertex labelled)
f = open('workfile_lh_' + str(num_parcels) + '.txt', 'w')
for label in clustering.labels_:
   f.write(str(label) + '\n')
f.close()
