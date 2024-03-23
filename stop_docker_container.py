import subprocess
import os, sys


def find_docker_executable():
    """
    This program search for docker exe if it exist in default PATH
    then return its file_path from the common path list below
    """
    # Check common installation paths
    common_paths = [
        r"C:\Program Files\Docker\Docker\resources\bin\docker.exe",
        r"C:\Program Files\Docker Toolbox\docker.exe",
    ]
    for path in common_paths:
        if os.path.exists(path):
            return path

    # Check directories listed in the PATH environment variable
    path_dirs = os.environ.get("PATH", "").split(os.pathsep)
    for path_dir in path_dirs:
        docker_path = os.path.join(path_dir, "docker.exe")
        if os.path.exists(docker_path):
            return docker_path

    # Docker executable not found
    return None


def stop_docker_container(docker_exe_path, container_name):
    """
    This module run docker stop container_name via command line within qgis
    docker_exe_path             :  docker exe file path
    container_name              :  docker container name, not to be confused with container ID
    """
    try:
        subprocess.run(
            [docker_exe_path, "stop", container_name],
            capture_output=True,
            shell=True,
            text=True,
            check=True,
        )
        return print(f"Container '{container_name}' stopped successfully.")

    except subprocess.CalledProcessError as e:
        return print(f"Error stopping container '{container_name}': {e}")


def switch_off_docker(container_name_to_stop):
    """
    This function switch on the docker container
    container_name_to_stop : container name
    """
    # Find Docker executable
    docker_executable = find_docker_executable()

    if docker_executable:
        print(f"Docker executable found: {docker_executable}")
        stop_docker_container(docker_executable, container_name_to_stop)
    else:
        print("Docker executable not found.")

    return


# Replace 'your_container_name' with the actual name of your Docker container
# container_name_to_stop = "map2loop_local_qgis_server-map2loop-1"
# docker_exe_file_path = r"C:\Program Files\Docker\Docker\resources\bin\docker.exe"
# stop_docker_container(docker_exe_file_path, container_name_to_stop)
