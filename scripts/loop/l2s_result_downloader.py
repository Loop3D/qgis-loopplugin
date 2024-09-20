# This module is to download data from loop3d server
# and save it into the loopstructural_output_data
import subprocess
import pyvista as pv
from pyvistaqt import BackgroundPlotter
import panel as pn
from pathlib import Path


def download_3d_data(docker_executable, source_path, destination_path, idx, N):
    """
    docker_executable : docker exe file path
    source_path       : the source path of the output_data within the container
    destination_path  : the destination file path including its name
    idx               : data idx
    N                 : Total nbre of data to be downloaded
    """
    try:
        res = subprocess.run(
            [str(docker_executable), "cp", source_path, destination_path],
            capture_output=True,
            text=True,
            shell=True,
        )

        if res.returncode != 0:
            print("Error:", res.stderr)
        else:
            print(
                f"STATUS: Saving data from container id {source_path.split(':')[0]} into loop output locally: Success"
            )
            if idx == N - 1:
                flag = "All loop data are downloaded"
            return res.returncode, flag

    except:
        print("Cant run the subprocess.run (docker cp , ..)")
    return


def vtk_pyvista_visualizer(list_of_files, flag):
    """
    This is a vtk visualiser using pyvista module
    """

    for filepath in list_of_files:
        # print("filepath is: ", filepath)
        try:
            # # Load the VTK file
            mesh = pv.read(filepath)
            if flag == "block_model" and flag in filepath:
                print(f" file to be used is {filepath}")
                # Create a plotter to visualize the model
                plotter = BackgroundPlotter()
                plotter.add_mesh(mesh)
                # Set the title using the file name
                plotter.set_background("white")  # Optional: Set background color
                plotter.add_text(
                    f"Model: {Path(filepath).name}",
                    position=(0.25, 0.95),
                    font_size=12,
                    color="black",
                    shadow=True,
                    viewport=True,
                )
                plotter.show()
        except:
            print("No selection have been made for plotting")
    print(" All surface are loaded")
    return


def plot_model_with_surfaces(filepath, list_of_files):
    # Read the block model
    mesh = pv.read(filepath)

    # Initialize the plotter
    plotter = BackgroundPlotter()

    # Add the block model mesh to the plotter
    plotter.add_mesh(mesh, color="lightblue", label="Block Model")
    surfaces = [a for a in list_of_files if "Fault" in a]
    stratigraphy = [a for a in list_of_files if "sg" in a]
    block_model_path = [a for a in list_of_files if "block_model" in a][0]
    # Add all surfaces to the plotter
    for surface_path in surfaces:
        surface_mesh = pv.read(surface_path)
        plotter.add_mesh(
            surface_mesh,
            color="green",
            opacity=0.6,
            label=f"Surface: {Path(surface_path).name}",
        )

    # Add stratigraphy layers to the plotter
    for stratigraphy_path in stratigraphy:
        stratigraphy_mesh = pv.read(stratigraphy_path)
        plotter.add_mesh(
            stratigraphy_mesh,
            color="brown",
            opacity=0.8,
            label=f"Stratigraphy: {Path(stratigraphy_path).name}",
        )

    # Set the plotter title and background
    plotter.set_background("white")
    plotter.add_text(
        f"3 Modelling of the WAXI: ",
        position=(0.25, 0.95),
        font_size=12,
        color="black",
        shadow=True,
        viewport=True,
    )
    # f"Model: {Path(filepath).name}",
    # Display the legend
    plotter.add_legend()

    # Show the plot
    plotter.show()
    return


def plot_block_model_with_surfaces_and_stratigraphy(list_of_files):

    ## Read individual dataset
    surfaces = [a for a in list_of_files if "Fault" in a]
    stratigraphy = [a for a in list_of_files if "sg" in a]
    block_model_path = [a for a in list_of_files if "block_model" in a][0]
    # Read the block model
    block_model_mesh = pv.read(block_model_path)

    # Initialize the plotter
    plotter = BackgroundPlotter()

    # Add the block model to the plotter
    plotter.add_mesh(
        block_model_mesh, color="lightblue", opacity=0.7, label="Block Model"
    )

    # Add all surfaces to the plotter
    for surface_path in surfaces:
        surface_mesh = pv.read(surface_path)
        plotter.add_mesh(
            surface_mesh,
            color="green",
            opacity=0.6,
            label=f"Surface: {Path(surface_path).name}",
        )

    # Add all stratigraphy layers to the plotter
    for stratigraphy_path in stratigraphy:
        stratigraphy_mesh = pv.read(stratigraphy_path)
        plotter.add_mesh(
            stratigraphy_mesh,
            color="brown",
            opacity=0.8,
            label=f"Stratigraphy: {Path(stratigraphy_path).name}",
        )

    # Set the plotter title and background
    plotter.set_background("white")
    plotter.add_text(
        f"3D Model",
        position=(0.25, 0.95),
        font_size=12,
        color="black",
        shadow=True,
        viewport=True,
    )
    # f"Model: {Path(block_model_path).name}",
    # Display the legend
    plotter.add_legend()

    # Show the plot
    plotter.show()
    return
