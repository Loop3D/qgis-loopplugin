#!/usr/bin/env python
# coding: utf-8

# # Loop Workflow Example 3

# * High level approach to making a 3D model from just a bounding box and source files as input. (In Australia only for now. Documentation to come)
# This is the wrapper module to pass data and execute calculation in your container
from map2loop.project import Project
from map2loop.m2l_enums import Datatype, VerboseLevel
from map2loop.sampler import SamplerSpacing, SamplerDecimator
from map2loop.sorter import (
    SorterUseHint,
    SorterUseNetworkX,
    SorterAgeBased,
    SorterAlpha,
)
import time
import os, ast

##

from datetime import datetime
#
#import pyproj
# Enable network access
#pyproj.network.set_network_enabled(True)
#import os
#os.environ['PROJ_NETWORK'] = 'ON'
#
# import shutil, subprocess


class M2l_Wrapper:
    """Wrapper class for map2loop process"""

    def __init__(self, param_conf):
        self.param_conf = param_conf

    def run_all(self, **kwargs):

        nowtime = datetime.now().isoformat(timespec="minutes")
        model_name = nowtime.replace(":", "-").replace("T", "-")
        loop_project_filename = os.path.join('./output_data', "local_source.loop3d")
        #loop_project_filename = os.path.join(model_name, "local_source.loop3d")

        t0 = time.time()

        # Specify the boundary of the region of interest in the appropriate projection coordinates
        print("I am here now @", t0)
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
            loop_project_filename=loop_project_filename,
        )

        print("Now:::Remove faults less than 5km")
        # Remove faults less than 5km
        proj.set_minimum_fault_length(5000.0)

        print("Now:::sampling distance for geology and fault maps to 200m")
        # Set sampling distance for geology and fault maps to 200m
        proj.set_sampler(Datatype.GEOLOGY, SamplerSpacing(200.0))
        proj.set_sampler(Datatype.FAULT, SamplerSpacing(200.0))

        print("Now:::taking every second orientation observation (0 or 1 means take all observations)")
        # Set to only take every second orientation observation (0 or 1 means take all observations)
        proj.set_sampler(Datatype.STRUCTURE, SamplerDecimator(2))

        print('Now:::what text is expected for intrusions (contained within the description field)')
        # Set what text is expected for intrusions (contained within the description field)
        proj.map_data.config.geology_config["intrusive_text"] = "mafic intrusive"

        print('Now:::specific layers from the geology map to be ignored (commonly "cover" or "water")')
        # Set specific layers from the geology map to be ignored (commonly "cover" or "water")
        proj.set_ignore_codes(["cover", "Fortescue_Group", "A_FO_od"])

        # Specify which stratigraphic columns sorter to use, other options are
        # (SorterAlpha, SorterAgeBased, SorterUseHint, SorterUseNetworkX, SorterMaximiseContacts, SorterObservationProjections)
        proj.set_sorter(SorterAlpha())
        proj.run_all()
        print('map2loop run successfully!!! ')
        # Or you can run map2loop and pre-specify the stratigraphic column
        column = [
            # youngest
            "Turee_Creek_Group",
            "Boolgeeda_Iron_Formation",
            "Woongarra_Rhyolite",
            "Weeli_Wolli_Formation",
            "Brockman_Iron_Formation",
            "Mount_McRae_Shale_and_Mount_Sylvia_Formation",
            "Wittenoom_Formation",
            "Marra_Mamba_Iron_Formation",
            "Jeerinah_Formation",
            "Bunjinah_Formation",
            "Pyradie_Formation",
            "Fortescue_Group",
            # oldest
        ]

        
# proj.run_all(user_defined_stratigraphic_column=column)

# Or you can get map2loop to run all column sorting algorithms it has and takes the one
# that has the longest total basal contact length
#proj.run_all(take_best=True)



