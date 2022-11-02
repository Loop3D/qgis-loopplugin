
# Welcome to qgis-loopplugin's plugin overview!
============================================

## Why loopplugin?

This plugin lets you select the raster and/or vector datasets from your local directory wihtin QGIS. Once the plugin is started, you can selects your files,
and then various field names for the shapefile and raster files are then analysed and an output json file and python script are generated that is used to run map2Loop (Loop project).   

## How to install **loopplugin**?

   You can git clone this plugin from the Loop3D repository. [https://github.com/Loop3D/qgis-loopplugin](https://github.com/Loop3D/qgis-loopplugin).   
      
   You can also download the repository as a zip file from <a href="https://github.com/Loop3D/qgis-loopplugin/archive/refs/heads/master.zip">[here]</a> and upload the zip file to QGIS using the plugin manager.   

## How to run **loopplugin**?

A usage example can be seen below:

Launch the plugin by selecting the Loop Icon in QGIS, or by selecting Loop Processor from the plugin Menu:*

<p align="center">
  <img src="launch_plugin.gif?raw=true" width=30 height=30>
</p>

### Set the project path

- Select the Project Directory:
   * Click the tool button (...) at the right of the project path box.
   * Navigate between directories and select your project folder, creating a new one if desired
   * Then, click Select Folder into the pop up window
   * Finally, the project directory is printed into the project path box.

### Load geology Layer into qgis workspace

- Click into (Load Geology Polygon Layer) to load the geology shapefile
- Once loaded, if potential column (field) names can be found, they will automatically filled with associated Layer column (field) names.
-  ```diff Check that the filled values are correctly selected in the combobox.```
- Also for some fields, text may be entered where it will be searched for in within that field, such as the text that lets the code know that this unit is a sill. In these text boxes, default values are printed out, i.e sill=sill. However, you can delete those values and input your own.

- A list of potential field names based on geological survey maps is available (see help on the right of window for descriptions of the different fields), e.g.:
   * Rocktype 1* --------> rocktype1 
   * Min Age*    --------> min_age_ma

- After every layer and associated parameters are selected, the user needs to click  on (Save Layer Params) to save the parameters.
- Once (Save layer Params) is clicked, individual parameters are saved and this is 
	confirmed by the (Tick) box being selected.

 An example can be seen below:

 Automated results after the geology layer is loaded:*

<p align="center">
<img src="filter_geol_data.gif">
</p>

### Repeat the process for Fault Polyline, Structure Point and DTM Layers

- Same process as the above.
- For DTM only select the layer which in return will provide the filepath needed in the python script. 
- No need to click (Save Layer Params) for the DTM layer. 

### Loading Fold Polyline and Min Deposit Point Layer

- Hard coded for now..

### Create json and/or Py script

- After the above is completed, then:  
   * Click "Create Json File" to generate a "data.json" in your Project Directory.
   * Click "Create Py Script" to generate a "Run_test.py" in your Project Directory.

* From this point, the final output are data.json and Run_test.py available in your project directory can be used as input to Map2loop/LoopStructural software.    
* If you move the files around you will have to edit the Run_test.py script accordingly to reset the paths.
* Assuming that the files paths are correct, and that map2loop is installed, you can run map2loop by going into a python shell and typing:   
   **python Run_test.py**   and the outputs will be stored in the project directory defined earlier on. 

### Future releases:

  *ROI = Region of interest.. A polygon cliping tool which will be used to crop data and save it as a new layer.
  
  *Layer selection from Qgis frame and/or database (not shown in plugin image).

  *Verbose 1,2,3 

  *Map2loop/LoopStructural loader To run Map2Loop using the generated json and py scripts.

