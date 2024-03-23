#!/usr/bin/env python
# coding: utf-8

## Loop Workflow Example 3
#####
from map2loop.project import Project
from map2loop.m2l_enums import VerboseLevel,Datatype
#####
import LoopProjectFile as LPF
from LoopStructural.visualisation import LavaVuModelViewer
from LoopStructural.modelling.input.project_file import LoopProjectfileProcessor as LPFProcessor
import LoopStructural
import numpy as np
from scipy.interpolate import RegularGridInterpolator
from osgeo import gdal
import pandas as pd

import time
import os, ast
from datetime import datetime
#


class LoopStructural_Wrapper:
    """Wrapper class for map2loop process"""

    def __init__(self, param_conf):
        self.param_conf = param_conf

    def run_all(self, **kwargs):


        t1 = time.time()
       
        config_data = self.param_conf
        print("config_data: ", config_data)
        bbox_3d = ast.literal_eval(config_data["bounding_box"])
        print("bbox_3d: ", bbox_3d)
        # Renaming the filename so that it match the docker filenames
        print('config_data["geology_filename"]: ', config_data["geology_filename"])
        
        # Initialise the project with the shapefiles, dtm, config file
        # output locations and projection to work in
        proj = Project(
            geology_filename="./server/source_data/"
            + str(config_data["geology_filename"]),
            fault_filename="./server/source_data/" + str(config_data["fault_filename"]),
            structure_filename="./server/source_data/"
            + str(config_data["structure_filename"]),
            mindep_filename="./server/source_data/"
            + str(config_data["mindep_filename"]),
            dtm_filename="./server/source_data/server_dtm_rp.tif",
            metadata_filename="./server/source_data/server_data.json",
            clut_filename="./server/source_data/" + str(config_data["csv_file"]),
            clut_file_legacy=True,
            verbose_level=VerboseLevel.NONE,
            tmp_path="./output_data",
            working_projection=str(config_data["working_projection"]),
            bounding_box=bbox_3d,
            loop_project_filename="./server/source_data/" + str(config_data["LPFilename"]),
        )

        print('loop3d is: ', str(config_data["LPFilename"]) )
        LPFilename = "./server/source_data/" + str(config_data['LPFilename'])  
        dtm_file   = "./server/source_data/" + str(config_data['dtm_filename']) 
        #'LPFilename': 'server_local_source.loop3d'
        fault_params = {
            'interpolatortype':'FDI',
            'nelements':1e4,
        }
        foliation_params = {
            'interpolatortype':'FDI' , # 'interpolatortype':'PLI',
            'nelements':1e5,  # how many tetras/voxels
            'regularisation':5,
        }

        projFile = LPF.ProjectFile(LPFilename)
        processedData = LPFProcessor(projFile)
        processedData.foliation_properties['sg'] = foliation_params
        processedData.fault_properties['interpolatortype'] = fault_params['interpolatortype']
        processedData.fault_properties['nelements'] = fault_params['nelements']

        model = LoopStructural.GeologicalModel.from_processor(processedData)
        # model.nsteps=np.array([200,200,50])
        model.update()
       
        clip_on_dtm=True
        if(clip_on_dtm):
            bounding_box = proj.map_data.get_bounding_box()
            model_base = bounding_box['base']
            model_top = bounding_box['top']
            #dtm = gdal.Open('./source_data/dtm_rp.tif')
            dtm = gdal.Open(str(dtm_file))
            dtm_val = dtm.GetRasterBand(1).ReadAsArray().T
            geoTrans = dtm.GetGeoTransform()
            minx = geoTrans[0]
            maxx = minx + dtm.RasterXSize * geoTrans[1]
            miny = geoTrans[3]
            maxy = miny + dtm.RasterYSize * geoTrans[5]

            # Convert bounds to gdal raster bounds
            x = np.linspace(minx,maxx,dtm.RasterXSize)
            y = np.linspace(miny,maxy,dtm.RasterYSize)
            dtm_interpolator = RegularGridInterpolator((x,y),dtm_val)
            model.dtm = lambda xyz : dtm_interpolator(xyz[:,:2])
        
        model_name = 'output_data'
        print('Here is the model name: ',model_name)
        try:
           vtk_path = str(os.getcwd())+'/'+str(model_name)+'/vtk/'
           #vtk_path = os.path.join("./"+str(model_name),'/vtk/')
        except:
            print('I cant be here')
            pass
        if not os.path.exists(vtk_path):
            os.mkdir(vtk_path)
        filename = os.path.join(model_name,'vtk','surface_name_{}.vtk')
        view = LavaVuModelViewer(model)
        ###
        view.nsteps=np.array([500,500,50])
        for sg in model.feature_name_index:
            if( 'super' in sg):
                view.add_data(model.features[model.feature_name_index[sg]])
        view.nelements = 1e5
        view.add_model_surfaces(filename=filename,faults=False)
        view.nelements=1e6
        view.add_model_surfaces(filename=filename,strati=False,displacement_cmap = 'rainbow')
        view.lv.webgl(vtk_path+model_name)


        t2 = time.time()


        # ## Elapsed Time

        # Print element and total processing time
        #m2l_time = t1-t0
        ls_time = t2-t1
        total = ls_time
        ls_string = f"{ls_time} sec" if ls_time < 60 else f"{ls_time/60.0} min"
        total_string = f"{total} sec" if total < 60 else f"{total/60.0} min"
        print(f"LoopStructural {ls_string}, Total {total_string}")
        print('loopstructural run successfully!!! ')

        # Draw overlay of point data on geology map
        # (options are 'basal_contacts', contacts','orientations','faults')
        #proj.draw_geology_map(overlay="basal_contacts")

        #print('loopstructural run successfully!!! ')
        # # Extract estimate of the stratigraphic column
        # proj.stratigraphic_column.column