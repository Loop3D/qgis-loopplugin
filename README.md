
# Welcome to qgis-loopplugin's plugin overview!
============================================

## Why qgis-loopplugin(version=0.9.1)?

This plugin version process various qgis layer such as a dtm raster, geology, fault and structure point layers.
These various layers can be loaded using 4 ways for the dtm, while the others in two options.

For example, we can load a dtm raster, using the following 4 Qcheckbox options:
  - **http**: if selected, the plugin generate a QLineeditor where the user will enter their own server address, then save it.
  - **File**: if selected, the plugin let you navigate to your local directory to select your file.
  - **Qgis**: if selected, the plugin generate a list of layer in which the user will have to select one.
  - **Aus** : if selected, the plugin will then select Geoscience Australia server address.

However, only **qgis** and **File** Qcheckbox options are active for the other type of layers.
Once a project directory and all layers with their Qcheckbox selected, a json and python files are created, and a processed data folder with only columns that are required for further calculations. 
All the outputs are then used as the input for map deconstruction (**run map2loop**) and/or for 3D modelling module(**LoopStructural**).

# 1. Environment Installation
## 1.1. Package Required
This plugin will requires the below dependencies: 
- QGIS version: 3.28.4-Firenze
- Qt version  : 5.15.3
- Python 3.9.5
- Docker Desktop version 4.26.1 (131620) or higher

## 1.2. How to install **loopplugin**?
  You will need a python package manager [see here](https://docs.anaconda.com/anaconda/install/index.html).
  Clone the qgis plugin repository from the Loop3D repository with the following link:
  [https://github.com/Loop3D/qgis-loopplugin](https://github.com/Loop3D/qgis-loopplugin)
  or from the <a href="https://github.com/Loop3D/qgis-loopplugin/archive/refs/heads/master.zip">[Download]</a> button. 
  To install from the QGIS Plugin Manager via ZIP, navigate to **Plugins**--> **Manage and Install Plugins**-->**Install from ZIP**, 
  input the path to the zipped folder, and click **Install Plugin**.
  More details about installing qgis plugin can be found here: [https://plugins.qgis.org/](https://plugins.qgis.org/)  

# 2. How to run **loopplugin**?

If the plugin is availaible in QGIS plugin tabs launch it by clicking the Loop icon,
in case, it is not available, select then Loop Processor from the plugin menu/installed.


The hierarchy chart that show the functional plugin flow through a program-parts (modules) and how they are related is shown below:*
<p align="center">
<img src="https://github.com/ShebMichel/qgis-animated_gif/blob/main/plugin_structure_chart_v05.gif">
</p>


A usage example of the automated results after the geology layer is loaded:*
<p align="center">
<img src="https://github.com/ShebMichel/qgis-animated_gif/blob/main/plugin_launch_v05.gif"/>
</p>

# 3. Loading the layers and project directory

## 3.1. Setting the project path into qgis workspace

- Select the Project Directory:
   * Click the tool button (...) at the end of the QLineEdit widget.
   * Navigate between directories and select your project folder
   * Then, click Select Folder into the pop up window
   * Finally, the project directory is printed into the QLineEdit.

## 3.2. Loading a geology layer into qgis workspace

* Click **Geology** layer to load the geology polygon (shapefile),
  * Once loaded, automatically the multiple combobox will be filled with multiple variable names (Layer columns names).
  ``` **Check that the filled values are correctly selected in the combobox.**```
  * Also, **sill** and **Intrusion **intrusive** are respectively the default for **Sill Text:** and **Intrusion Text:** Qtext labels.
  However, if you have the field knowledge, please edit it to the text that correspond to your geology attribute.
* In mapping the labels to your combobox, for example one can use the below example:
   * Rocktype 1* --------> rocktype1   (i.e: select the column header value from the layer table drop-down that corresponds to the Rocktype 1 attribute)
   * Min Age*    --------> min_age_ma  (i.e: select the column header value from the layer table drop-down that corresponds to the Min Age attribute)
* Once happy with all the parameters selected, to save the data, click **Fault** layer so that the Qcheckbox next to **geology** to be selected.
  Note that, you can also click **Structure** layer to for the above checkbox tick.
 

## 3.3. Repeat the process for Fault Polyline, Structure Point and DTM Layers

* Same process as the above for both **Fault** and **Structure** layers.
* For **DTM** raster, this layer is activated only when the above 3 layers are selected.
  However, when loaded no parameter is required to map attributes, the checkbox is ticked at load.  


## 3.4. Loading Fold Polyline and Min Deposit Point Layer

* Hard coded for now (future releases).

# 4. Output/Input: Configuration file and processed data

* Once the **Project Directory** is defined, and all the **Geology**, **Fault**, **Structure** and **DTM** layers checked, 
  click **Save Config File** to generate both "data.json" and "Run_test.py" in Project Directory/process_source_data_timestamp/.
* There are more 4 folders to expect insode your project directory:
   - for map2loop: process_source_data_timestamp and output_data_timestamp folder.
     - The process_source_data_timestamp: contain the newly saved shapefile/geojson with the only selected parameters during layer processing.
     - output_data_timestamp: contain the map2loop results locally be stored in your pc.
   - for loopstructural: loopstructural_source_data_timestamp and loopostructural_output_data_timestamp
     - loopstructural_source_data_timestamp: processed data for loop algorith 
     - loopostructural_output_data_timestamp: result data local storage
 

# 5. RUN map2loop (map deconstruction)
  This module will ask you to select the environment in which your calculations will be running (i.e: remote or personal computer) .
  
  Click **Run map2loop**, then the option below will be prompted:  
    * Yes : local server (i.e running docker locally)
    * No  : remote server(i.e running the calculation remotely)
  
  * Yes 
    * For local calculation, it is required to have Docker Desktop for window user. If not, 
      <a href="https://www.docker.com/products/docker-desktop/">[Click]</a> to follow the install instruction and launch the Docker Desktop app.
      Once the Docker Desktop launched, go back to QGIS Plugin front-end to click **Yes**. Then wait and relax so that the magic happen.

  * No
    * For remote calculation, ensure that you have the **map2loop-server** running on your remote machine.
    * Otherwise, please turn on the server, just open the terminal in the root directory of the clone map2loop-server repository and run:
       ```bash
       docker compose up --build
       ```
    then, go back to QGIS Plugin front end to click **No**. Just wait and relax so that the magic happen.
    
  By selecting either **Yes**/ **No**, the local process data and configuration files are transmitted to the Docker server within a container using a WebSocket client.  
  Subsequently, multiple batch calculations are performed until completion. Afterward, the resulting outputs are transferred to your local PC inside the output_data_**stamptime** directory. 
  Note that the timestamp corresponds to the date and time when the data is received on your end.
  
  ## 5.1. Turn ON and OFF your docker container
After the result ouptuts are reviewed or you are done sending back and forth the data to the server, click **Docker** QPushButton to either turn ON/OFF.

For now, Only use it to turn OFF, but if its already on, it will restart the docker. In the next release, the user will be asked to go and click **Docker** button before sending the data for calculation into the docker container.
  
# 6. RUN LoopStructural (3D Geological modelling)
 This module will ask you to select the environment in which your calculations will be running (i.e: remote or personal computer) .
  
  Click **LoopStructural**, then the option below will be prompted:  
    * Yes : local server (i.e running docker locally)
    * No  : remote server(i.e running the calculation remotely)
   The rest is as mentionned in the Run Map2loop section. If succesfull, then wait and relax so that the magic happen.
## 6.1. 3D:: Vizualisation
This module is enabled only when the loopstructural calculation engine is completed. 
Once active, if clicked, it will populate the 3D visualization of the model on your defaul browser. 
# 7. RUN LoopUI (Ensemble of model generators)
 coming soon
# 8. RUN TomoFast (3D Geophysical modelling)
 coming soon
 <!---RUN TomoFast (3D Geophysical modelling)-->
# 9. Extra modules:
  This section offers optional features for 3D modeling. Users can leverage the clipping tool for data manipulation to select their area of interest.
## 9.1. Create your Region Of Interest (ROI)
 Utilize the **ROI** as your clipping tool to trim data and save it as a new layer. The resulting layer is stored as **yourfilename**_clip.shp in your project directory.
 To ensure successful use, please make sure to provide the **Project Directory** path in its QlineEdit. 
 When **ROI** is clicked, you and no layers are available in the QGIS layer panel, you will:
 
    * Be prompted to load a layer from two options.
      * Yes : to create your ROI 
        * If **Yes** a newly temp_layer will be created into your QGIS layer panel. 
        * While the drawing tools are toggle into QGIS, now manually draw your ROI,
        * Once drawing is done click **OK**, and finally click **clip your layer** to generate roi data
      * No  : to locally upload your layer only when the 4 required layers are loaded 
       **(upgrade coming to make it independent)**
    * Once you click clipped_your_layer, all the loaded layer should be clipped and add to the panel.
    
## 9.2. HelpU
  A documentation database that capture geological layer header column names as well as sill and intrusion text for example (coming soon for future releases.
# 10. Future releases:

  * REQUIRED: This will be embedded during plugin installation into the next release.
  * LoopUI.clicked.connect()
  * TomoFast.clicked.connect()
  * HelpU: A feature attached to the help function in which the user can upload their own library.

