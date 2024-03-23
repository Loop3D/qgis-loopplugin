import time
import os
from map2loop.project import Project
from map2loop.m2l_enums import VerboseLevel
from datetime import datetime

t0 = time.time()
nowtime=datetime.now().isoformat(timespec='minutes')   
model_name=nowtime.replace(":","-").replace("T","-")

proj = Project( 
                loopdata_state="WA",
                overwrite="true",
                verbose_level=VerboseLevel.NONE,
                project_path=model_name,
                working_projection="EPSG:28350",
)

proj.update_config(
                    out_dir=model_name,
                    bbox_3d={
                         "minx": 515687.31005864, # region of interest for GMD paper
                         "miny": 7473446.76593407,
                         "maxx": 562666.860106543,
                         "maxy": 7521273.57407786,
                         "base": -3200,
                         "top": 1200,
                     },
                     run_flags={                        
                        'aus': True,
                        'close_dip': -999,
                        'contact_decimate': 5,
                        'contact_dip': -999,
                        'contact_orientation_decimate': 5,
                        'deposits': "Fe,Cu,Au,NONE",
                        'dist_buffer': 10,
                        'dtb': '',
                        'fat_step': 750,
                        'fault_decimate': 5,
                        'fault_dip': 90,
                        'fold_decimate': 5,
                        'interpolation_scheme': 'scipy_rbf',
                        'interpolation_spacing': 500,
                        'intrusion_mode': 0,
                        'max_thickness_allowed': 10000,
                        'min_fault_length': 5000,
                        'misorientation': 30,
                        'null_scheme': 'null',
                        'orientation_decimate': 0,
                        'pluton_dip': 45,
                        'pluton_form': 'saucers',
                        'thickness_buffer': 5000,
                        'use_fat': False,
                        'use_interpolations': False,
                        'fault_orientation_clusters':2,
                        'fault_length_clusters':2
                    },
                  )
proj.config.c_l['intrusive']='mafic intrusive'
proj.run()