"""
This python module is used to clear features such as combobox and QLineEditor
"""

import os, glob, shutil
import geopandas
import processing
from pathlib import Path
from qgis.core import QgsVectorLayer


def create_geojson_file(outfile, filename, data_path):
    """
    This function create a geojson file using:
    # filepath : the filepath of the data to save as geojson
    # filename : same as the original filepath
    # data_path: geojson directory
    """
    # Now create the geojson file
    myshpfile = geopandas.read_file(outfile)
    myshpfile.to_file(
        str(data_path) + "\\" + str(filename) + ".geojson", driver="GeoJSON"
    )
    return


# def create_data_for_no_del_col(parent_path, process_source_data):
#     """
#     This function is used to push process data into the new folder when col_to_del =[] (empty list)
#     """
#     process_data = glob.glob(str(parent_path) + "/*")
#     # Filter out directories from the list
#     proc_data = [f for f in process_data if not Path(f).is_dir()]
#     for file in proc_data:
#         name = str(os.path.basename(file))
#         path = str(process_source_data) + "\\" + str(name)
#         if os.path.exists(path):
#             pass
#         else:
#             shutil.copy(file, process_source_data)
#     return


def create_strip_shapefile(filepath, field_to_keep, filename, data_path):
    """
    This function create a new shapefile using split features by charcater
    # layer_cols: layer list of column id name
    # filepath  : the filepath of the data to strip to create new shp file
    # filename  : same as the original filepath
    # data_path : shp file directory same as the original one
    """

    # Layer reading from source file
    layer = QgsVectorLayer(filepath, " ")
    # read all the column id for the original data
    original_columns = layer.fields().names()
    clean_field_to_keep = field_to_keep[:-2]
    try:
        # Check if column value is 'NONE'
        if "NONE" in clean_field_to_keep:
            clean_field_to_keep.remove("NONE")
    except:
        pass
    # define the list of layer column to be removed
    columns_to_delete = list(
        set(clean_field_to_keep).symmetric_difference(original_columns)
    )

    ## define the new file name
    outfile = str(data_path) + "\\" + str(filename) + ".shp"

    parameter_for_extract = {
        "INPUT": str(filepath),
        "COLUMN": columns_to_delete,
        "OUTPUT": outfile,
    }
    # if for reprocess data
    if (
        not columns_to_delete
        or columns_to_delete == ["num", "Strike"]
        or columns_to_delete == ["Strike"]
    ):
        outfile = outfile
        for file in glob.glob(str(Path(filepath).parent) + "/*"):
            if filename in file:
                shutil.copy(file, str(data_path) + "/")
    # else to strip data .. Here we use raw data
    else:
        output = processing.run("native:deletecolumn", parameter_for_extract)
    return outfile


def count_clip_occurrences(filename):
    # Count how many times '_clip' appears in the filename
    return filename.count("_clip")


def find_clip_files(directory):
    # Find all files that contain '_clip' in their names
    clip_files = glob.glob(os.path.join(directory, "*_clip*"))
    clip_tif_files = glob.glob(os.path.join(directory, "*_clip.tif*"))

    if not clip_files:
        return []  # Return an empty list if no _clip files exist

    if not clip_tif_files:
        return []  # Return an empty list if no _clip for tif files exist

    # Create a list of tuples (file, number of _clip appearances)
    clip_file_counts = [
        (file, count_clip_occurrences(os.path.basename(file))) for file in clip_files
    ]

    # Create a list of tuples (file, number of _clip appearances)
    clip_tif_file_counts = [
        (file, count_clip_occurrences(os.path.basename(file)))
        for file in clip_tif_files
    ]

    # Find the maximum number of _clip appearances
    max_clip_count = max(count for file, count in clip_file_counts)

    # Find the maximum number of _clip appearances
    max_clip_tif_count = max(count for file, count in clip_tif_file_counts)

    # Select files with the highest _clip count
    selected_files = [
        file for file, count in clip_file_counts if count == max_clip_count
    ]

    selected_tif_files = [
        file for file, count in clip_tif_file_counts if count == max_clip_tif_count
    ]

    clipped_names = [Path(a).name for a in selected_files]
    clipped_tif_names = [Path(a).name for a in selected_tif_files]
    return max_clip_count, clipped_names, max_clip_tif_count, clipped_tif_names


def find_tif_files_with_clip(directory):
    # Find all .tif and .gif files in the directory
    tif_gif_files = glob.glob(os.path.join(directory, "*.tif")) + glob.glob(
        os.path.join(directory, "*.gif")
    )

    # Filter files that contain '_clip' in their names
    clip_files = [file for file in tif_gif_files if "_clip" in os.path.basename(file)]

    return clip_files


def rename_shapefile(file_path, L):
    # Split the file name and extension
    file_name, file_extension = os.path.splitext(file_path)

    # Ensure that the file has the correct ".shp" extension
    if file_extension.lower() != ".shp":
        raise ValueError("The file is not a shapefile (.shp)")

    # Add '_clip' multiple times based on L
    new_suffix = "_clip" * L

    # Create the new file name with the ".shp" extension
    new_file_name = file_name + new_suffix + file_extension

    # Rename the file
    os.rename(file_path, new_file_name)

    print(f"File renamed to: {new_file_name}")
    return new_file_name


# Example usage
# rename_shapefile("geol_clip.shp", L=2)
