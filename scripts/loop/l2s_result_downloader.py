
# This module is to download data from loop3d server
# and save it into the loopstructural_output_data 
import os,subprocess

def download_3d_data(docker_executable,source_path, destination_path):
	'''
	docker_executable : docker exe file path
	source_path       : the source path of the output_data within the container
	destination_path  : the destination file path including its name
	'''
	try:
		res = subprocess.run([str(docker_executable), 'cp', source_path, destination_path],
					   capture_output=True,
					   text=True,
					   shell=True)

		if res.returncode != 0:
			print("Error:", res.stderr)
		else:
			print(f'Copying data from container {source_path}: Success')
			return res.returncode
	except:
		print('Cant run the subprocess.run (docker cp , ..)')
	return 
