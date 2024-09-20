#!/usr/bin/env python
# coding: utf-8

## Loop Workflow Example 3

from map2loop.project import Project
from map2loop.m2l_enums import VerboseLevel
import LoopProjectFile as LPF
import LoopStructural
import numpy as np
from scipy.interpolate import RegularGridInterpolator
import time
import os, ast, shutil

####

from loopstructuralvisualisation import Loop3DView

# from LoopStructural.visualisation import Loop3DView
# from LoopStructural.modelling.input.project_file import (
#     LoopProjectfileProcessor as LPFProcessor,
# )

from LoopStructural.modelling import (
    LoopProjectfileProcessor as LPFProcessor,
)

from osgeo import gdal


def move_vtk_files(source_directory, target_directory):
    # Ensure the target directory exists
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
        print(f"Directory '{target_directory}' created.")
    output_data_list = []
    # Loop through all files in the source directory
    for filename in os.listdir(source_directory):
        # Check if the filename contains '.vtk'

        if filename.endswith(".vtk"):
            source_file_path = os.path.join(source_directory, filename)

            # Move the file to the target directory
            destination_file_path = os.path.join(target_directory, filename)
            output_data_list.append(destination_file_path)
            shutil.move(source_file_path, destination_file_path)
            print(f"Moved {source_file_path} to {destination_file_path}")
        print(f"Outut data list: {output_data_list}")
    return output_data_list


class LoopStructural_Wrapper:
    """Wrapper class for loopStructural process"""

    def __init__(self, param_conf):
        self.param_conf = param_conf

    def run_all(self, **kwargs):

        t1 = time.time()

        config_data = self.param_conf
        print("config_data in wrapper: ", config_data)
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
            dtm_filename="./server/source_data/" + str(config_data["dtm_filename"]),
            metadata_filename="./server/source_data/server_data.json",
            clut_filename="./server/source_data/" + str(config_data["csv_file"]),
            clut_file_legacy=True,
            verbose_level=VerboseLevel.NONE,
            tmp_path="./output_data",
            working_projection=str(config_data["working_projection"]),
            bounding_box=bbox_3d,
            loop_project_filename="./server/source_data/"
            + str(config_data["LPFilename"]),
        )

        print("loop3d is: ", str(config_data["LPFilename"]))
        LPFilename = "./server/source_data/" + str(config_data["LPFilename"])
        dtm_file = "./server/source_data/" + str(config_data["dtm_filename"])
        #'LPFilename': 'server_local_source.loop3d'
        fault_params = {
            "interpolatortype": "FDI",
            "nelements": 1e4,
        }
        foliation_params = {
            "interpolatortype": "FDI",  # 'interpolatortype':'PLI',
            "nelements": 1e5,  # how many tetras/voxels
            "regularisation": 5,
        }
        projFile = LPF.ProjectFile(LPFilename)
        processedData = LPFProcessor(projFile)
        processedData.foliation_properties["sg"] = foliation_params
        processedData.fault_properties["interpolatortype"] = fault_params[
            "interpolatortype"
        ]
        processedData.fault_properties["nelements"] = fault_params["nelements"]
        model = LoopStructural.GeologicalModel.from_processor(processedData)
        model.update()

        model_name = "output_data"
        print("Checking if ./vtk folder exist inside output_data forlder on the server")
        # check whether directory 'output_data' already exists
        if not os.path.exists(str(model_name)):
            os.mkdir(str(model_name))
            print("Folder" + str(model_name) + " is created!")
        else:
            print("Folder " + str(model_name) + " already exists ")
        try:
            vtk_path = str(os.getcwd()) + "/" + str(model_name) + "/vtk/"
        except:
            print("If I am here, this mean ./vtk test failed")
            pass
        if not os.path.exists(vtk_path):
            os.mkdir(vtk_path)
        # directories
        source_directory = "./"
        vtk_directory = "output_data/vtk"
        #
        model.save("model_surface.vtk")
        t2 = time.time()

        # ## Elapsed Time

        # Print element and total processing time
        ls_time = t2 - t1
        total = ls_time
        ls_string = f"{ls_time} sec" if ls_time < 60 else f"{ls_time/60.0} min"
        total_string = f"{total} sec" if total < 60 else f"{total/60.0} min"
        print(f"LoopStructural {ls_string}, Total {total_string}")
        print("loopstructural run successfully!!! ")

        ####
        try:
            output_data_list = move_vtk_files(source_directory, vtk_directory)
            print(f"output data lists: {output_data_list}")
        except:
            pass

        ################################# uncomment the above
