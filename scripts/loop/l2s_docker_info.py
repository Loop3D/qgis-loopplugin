# This module return the docker infos
import subprocess, os


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


def get_docker_infos(docker_path):
    """
    This function extract docker container infos
    docker_path :  docker exe absolute file path
    """
    # extract docker container info
    result2 = subprocess.run(
        [docker_path, "ps"],
        capture_output=True,
        text=True,
        shell=True,
    )
    container_info = result2.stdout.split()
    container_id = []
    for id, val in enumerate(container_info):
        if str(val) == "loopstructural_local_qgis_server-loopstructural":
            container_id.append(container_info[id - 1])
            break
    docker_container_id = container_id[0]
    # print("found container id: ", docker_container_id)
    return docker_container_id


#


def get_my_docker_infos():
    """
    This function switch on the docker container
    """
    # Find Docker executable
    docker_executable = find_docker_executable()
    # print("docker_executable::::::::::::", docker_executable)
    docker_container_id = get_docker_infos(docker_executable)
    return docker_executable, docker_container_id
