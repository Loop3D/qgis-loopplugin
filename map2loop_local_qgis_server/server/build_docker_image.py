import subprocess, os, sys


#####################
def run_docker_compose(docker_exe_path, docker_compose_file_path):
    """
    This module run docker compose up --build via command line within qgis
    docker_exe_path             :  docker exe file path
    docker_compose_file_path:  docker compose file path (.yml)
    """
    try:
        # Run the docker-compose command with build option
        # very important to run it in a detach mode docker compose -f 'file_path', 'up', '-d', '--build'
        result = subprocess.run(
            [
                docker_exe_path,
                "compose",
                "-f",
                docker_compose_file_path,
                "up",
                "-d",
                "--build",
            ],
            capture_output=True,
            text=True,
            shell=True,
        )
        if result.returncode != 0:
            print("Error:", result.stderr)
            return result.stderr
        else:
            print("Output :", result.stdout)
            return result.stdout
    except:
        print("Error:", result.stderr)
        return print("Cant connect to docker")


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


def switch_on_docker():
    """
    This function switch on the docker container
    """
    docker_compose_path = sys.argv[1]
    print("docker compose file path:   ", docker_compose_path)
    # Find Docker executable
    docker_executable = find_docker_executable()
    print("docker_executable::::::::::::", docker_executable)

    if docker_executable:
        print(f"Docker executable found: {docker_executable}")
        run_docker_compose(docker_executable, docker_compose_path)
    else:
        print("Docker executable not found.")

    return


switch_on_docker()
