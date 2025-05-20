# QGIS Geological Data Processing Plugin

## Overview
This plugin provides a comprehensive workflow for managing and processing geological data within QGIS. It facilitates the preparation, configuration, and integration of geological, fault, and structural data for 3D geological modeling.
# Structure chart and animation coming soon

## Requirements
### Environment
- All modules in the requirements.txt can individually be installed via OSGeo4W shell, i.e: (`pip install map2loop`)
- Make sure the following versions exist:
<br>````LoopProjectFile == 0.2.2````
<br>````LoopStructural  == 1.6.8````
<br>````map2loop        == 3.2.2````
<br>````map2model       == 1.2.1````
<br>````QGIS            == 3.40.3-Bratislava````
<br>````QT              == 5.15.13 ````
 Or run the following install on your qgis python console:
 <br>````!pip install LoopProjectFile==0.2.2````
<br>````!pip install LoopStructural==1.6.8````
<br>````!pip install map2loop==3.2.2````
<br>````!pip install map2model==1.2.1````
<br>````!pip install pyvista````
<br>````!pip install pyvistaqt````
<br>````!pip install websockets````
<br>````!pip install fiona````
<br>````!pip install rasterio````
Alternatively, you can run the same command into OSGeo4W Shell terminal by droping the exclamation symbol in front of pip.
 
### Data
In order to run map2loop you will need the following input files:
1. Polygon shapefile containing your lithologies
2. LineString shapefile containing your linear features (e.g. faults)
3. Point data shapefile containing orientation data
4. Digital Terain Model (DTM)

### Test Data
The test dataset is located in the testing_data directory. 

## Features
- Multiple data loading options (shapefile, DTM, JSON)
- Coordinate reference system management
- Digital Terrain Model (DTM) integration
- Geological formation mapping
- Fault data processing
- Structural point data handling
- Integration with Map2loop and LoopStructural for 3D modeling

## Tab Descriptions

### Configuration Tab
| Feature | Description |
|---------|-------------|
| Load Input Data | Select FILE (default) to load multiple shapefiles and DTM into QGIS or JSON to preload data from a saved file. |
| Select the CRS | Choose the reference coordinate system. Use CRS Selector to append the selected CRS to Output CRS. |
| Select the DTM | QGIS: Select a DTM file path. AUS: Fetch DTM from Geoscience Australia. JSON: Use preloaded DTM data. |
| Type of Data | Raw Data: Uses existing data from QGIS. Clip Data: Select/define a Region of Interest (ROI) and clip available data. |


### Geology Layer Tab
| Feature | Description |
|---------|-------------|
| Load Geology Data | Select QGIS (default) to fill the combobox with only geology file types, then select one and click OK. Use JSON to load from an existing data.json file from the Configuration Tab. |
| Link Your Header with the Right Parameters | Verify field mapping (e.g., Formation <----> unitname) and adjust if needed. |
| Use Your Geological Field Knowledge | Modify default values based on expertise and field observations. |


### Fault Layer Tab
| Feature | Description |
|---------|-------------|
| Load Fault Data | Select QGIS (default) to fill the combobox with only geology file types, then select one and click OK. Use JSON to load from an existing data.json file. |
| Link Your Header with the Right Parameters | Verify field mapping (e.g., Dip <----> dip) and adjust if needed. |
| Use Your Geological Field Knowledge | Modify default values based on expertise and field observations. |


### Structure Layer Tab
| Feature | Description |
|---------|-------------|
| Load Structure Point Data | Select QGIS (default) to fill the combobox with only geology file types, then select one and click OK. Use JSON to load from an existing data.json file. |
| Link Your Header with the Right Parameters | Verify field mapping (e.g., Dip <----> dip) and adjust if needed. |
| Use Your Geological Field Knowledge | Modify default values based on expertise and field observations. |


### Run Tab
| Feature | Description |
|---------|-------------|
| Save Configuration | - **m2l Output**: Type the name of your Map2loop output folder (default: `m2l_output`) <br>- **l2s Output**: Type the name of your LoopStructural output folder (default: `m2l_output`). |
| Preprocessor | Prepares and processes raw geological data, save all the configuration parameters into data.json and create new shapefile which only contains the selected field name from the above Tabs.|
| Map2loop | Extracts and processes geological data from GIS sources. <br>- **Minimum Fault Length**: Minimum value with default=5000.0m,<br>- **Geology Sampler Spacing**: Sampling resolution with default=200.0m,<br>- **Fault Sampler Spacing**: Sampling resolution with default:200.0m, <br>- **Base**: Map base value  with default=-3200m, <br>- **Top**: Map top value with default=1200m, <br>- **MinX** and **MaxX**: minimun and maximun X-value, <br>- **MinY** and **MaxY**: minimun and maximun Y-value. <br> These values are automatically populated, check and edit using your expertise. |
| LoopStructural | Used for 3D geological modeling, integrating structural and geological data. Select the following server <br>- **DOCKER**: Docker server, <br>- **GCP**: Google Cloud Server, <br>- **AWS**: Amazon Web Server. Choose the server availaible for your own case.|
| 3D PLOT | Used to visualize the result of LoopStructural 3D modelling.|

## Server Environments
The Run tab supports multiple server environments:
- Docker <br>For windows machine, you need to have Docker Desktop Launch <br>If using remote machine without Docker Desktop, clone the following repo and cd remote_server/loopstructural_server and run `docker compose up --build` 
<br>- GCP (Google Cloud Platform)<br>- AWS (Amazon Web Services)

## Workflow
1. Configure input data and parameters in the Configuration Tab
2. Set up geological data in the Geology Layer Tab
3. Configure fault data in the Fault Layer Tab
4. Set up structural point data in the Structure Layer Tab
5. Run the processing workflow in the Run Tab

# ROI-Based Clipping Tool for QGIS

This tool allows users to clip spatial layers using a Region of Interest (ROI), either by creating one directly in QGIS or using an existing ROI layer.

## 🛠️ Getting Started

When you select **Clip Data**, you can define your ROI in one of two ways:

---

## 🗂 Option 1: Use Existing ROI

1. Click **Existing ROI**.
2. You will be prompted to choose one of the following:
   - **QGIS Panel**:  
     Select an ROI layer that is already loaded in your QGIS session.  
     → All layers, including the selected ROI, will be listed in the text editor below the **Save ROI and Clip** button.
   - **Local File**:  
     Load an ROI shapefile from your computer.  
     → The selected file will be displayed in the text editor below **Save ROI and Clip**.

---

## ✏️ Option 2: Create ROI

1. Click **Create ROI**.
2. A message will appear:  
   > *"Draw your Region of Interest (ROI) on the map."*
3. Click **OK**.
4. Use the **Add Polygon Feature** tool in QGIS to draw your ROI directly on the map.
5. Once finished:
   - Click the **Save ROI** button.
   - All available layers, including the newly created ROI, will be listed in the text editor below **Save ROI and Clip**.

---

## 🎯 Final Step: Select Layers to Clip

After setting up the ROI using one of the two methods above:

- Use the text editor to **select only the layers** you want to clip.
- These should be relevant to your study or region.

> **Example**:  
> To clip data for the *Hammersley Basin*, you might select:  
> `faults`, `geology`, `dtm`, and `structure`.

---

## 📌 Notes

- Ensure all layers are loaded and visible in QGIS before proceeding.
- ROI must be a polygon layer for successful clipping.
- For optimal results, ensure all layers use the same CRS (Coordinate Reference System).

---


## Support
For issues or questions, please refer to the documentation or open an issue in this repository.


