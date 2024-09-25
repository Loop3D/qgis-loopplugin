import asyncio
import websockets
import json
import base64
import ast, os
import glob
from pathlib import Path
from L2S_wrapper import LoopStructural_Wrapper




def check_message_format_valid(message):
	"""Simple check to determine if the message dict is in the correct format.

	Args:
			message (dict): _description_

	Returns:
			bool: true if message dict is valid, false if not
	"""
	if type(message) is not dict:
		return False
	if "client_id" not in message:
		return False
	if type(message["client_id"]) is not int:
		return False
	if "project_id" not in message:
		return False
	if type(message["project_id"]) is not int:
		return False
	if "function" not in message:
		return False
	if type(message["function"]) is not str:
		return False
	if "params" not in message:
		return False
	if type(message["params"]) is not str:
		return False
	return True


def clear_folder(folder_path):
	''' This function is used to clear folder after it is received locally'''
	for filename in os.listdir(folder_path):
		file_path = os.path.join(folder_path, filename)
		# Check if it's a file and delete it
		if os.path.isfile(file_path):
			if '__init__.py' in str(file_path):
				pass
			else:
				os.remove(file_path)
				print(f"Deleted file: {file_path}")
	return 

def list_files(directory_path):
	files = []
	for file_name in os.listdir(directory_path):
		file_path = os.path.join(directory_path, file_name)
		if os.path.isfile(file_path):
			files.append(file_path)
		elif os.path.isdir(file_path):
			files.extend(list_files(file_path))
	return files


# connected  =set()
async def handler(socket):
	"""Main packet handler function

	Args:
			socket (WebsocketServerProtocol): the websocket to send and receive from
	"""
	# Receive and unpack packet
	data = await socket.recv()
	package = json.loads(data)
	# print('I ..')

	# Check if packet valid
	if not check_message_format_valid(package):
		await socket.send(f"Invalid server request")
	else:
		# Create response
		response = {
			"client_id": package["client_id"],
			"project_id": package["project_id"],
			"success": 1,
			"error_msg": "",
			"response": "",
			"params": package["params"],
			"filename": package["filename"],
		}

		# flag=str(response["filename"])
		flag = str(package["filename"])

		if flag == "":
			loopprojectfilename = f"server/source_data/server.{package['client_id']}.{package['project_id']}.loop3d"
		elif flag == "server_out":
			pass
		else:
			loopprojectfilename = f"server/source_data/server_" + str(
				response["filename"]
			)

		# Switch for packet type
		if package["function"] == "TEST":
			response["response"] = f"Test message recieved ({package['params']})"

			await socket.send(json.dumps(response))

		elif package["function"] == "UPLOAD":
			## LL is the length of the data to be tranfert
			LL = package["Length"]
			path = Path(loopprojectfilename)
			try:
				if path.is_file() == True:
					response["response"] = (
						f"(client {package['client_id']}) already exist in docker container"
					)
					print(response["response"])
				else:
					# Decode uploaded binary data and save to drive
					data = base64.b64decode(package["params"].encode("utf-8"))
					# with open(loopprojectfilename, mode="wb") as file:
					with open(loopprojectfilename, mode="wb") as file:
						file.write(data)
						response["response"] = (
							f"UPLOAD message recieved (client {package['client_id']})"
						)

			except Exception as e:
				response["success"] = 0
				response["error_msg"] = str(e)

			# Check if the entire set of data are received?
			list_of_data = glob.glob("server/source_data" + "/*")
			if LL == len(list_of_data):
				response["response"] = (
					f"All Data from (client {package['client_id']}) are recieved"
				)
			else:
				pass

			await socket.send(json.dumps(response))

		elif package["function"] == "EXECUTE":
			try:
				data = package["params"]
				config_data = ast.literal_eval(data)
				#bbox_3d = ast.literal_eval(config_data["bounding_box"])
				print('config_data here: ',config_data)
				# # # Create the map2loop project and run rocess
				m2l =LoopStructural_Wrapper(config_data)
				m2l.run_all()

				response["response"] = f"EXECUTED loopstructural Successfully"
				try:
					# list_of_data in server output data
					directory_path = "output_data"
					all_files = list_files(directory_path)
					file_to_transfert = []
					name_to_transfert = []
					# print('all files',all_files)
					for file_path in all_files:
						file_to_transfert.append(file_path)
						name_to_transfert.append(file_path.split("/")[-1])
					filepath_and_its_name = dict(
						zip(name_to_transfert, file_to_transfert)
					)
					response["output_data"] = str(filepath_and_its_name)
					response["response"]    = f"output_data/vtk data is availaible"
				except:
					pass
				await socket.send(json.dumps(response))

			except Exception as e:
				response["success"] = 0
				response["error_msg"] = str(e)
				await socket.send(json.dumps(response))

		elif package["function"] == "DOWNLOAD":
			filepath = str(package["serv_data"])
			filename = str(package["filename"])
			# loopprojectfilename='./'+str(package["filename"])
			loopprojectfilename = "./" + str(package["serv_data"])
			try:
				with open(str(loopprojectfilename), mode="rb") as file:
					data = file.read()
					encoded_data = base64.b64encode(data).decode("utf-8")
					response["response"] = encoded_data
			except Exception as e:
				response["success"] = 0
				response["error_msg"] = str(e)
			await socket.send(json.dumps(response))

		elif package["function"] == "FULL":
			print('The package data file are:',package["function"])
			source_data_path = './server/source_data'
			output_data_path = './output_data/vtk'
			try:
				for folder_path in [source_data_path,output_data_path]:
					clear_folder(folder_path)
			except:
				print(f"Cant delete the file in folders")

			response["response"] = f"FULL message recieved ({package['client_id']})"
			await socket.send(json.dumps(response))


async def main(port, ip, max_size):
	async with websockets.serve(
		handler, ip, port, max_size=max_size, ping_interval=None
	):
		await asyncio.Future()


if __name__ == "__main__":
	import argparse

	parser = argparse.ArgumentParser(description="LoopStructural Server")
	parser.add_argument(
		"-p", "--port", type=int, default=8888, help="Port to listen on"
	)
	parser.add_argument(
		"-ip",
		"--ip",
		type=str,
		default="",
		help="IP address to listen on. 0.0.0.0 for all",
	)
	parser.add_argument(
		"-m",
		"--max_size",
		type=int,
		default=2**20,
		help="Maximum size of packets in bytes",
	)
	args = parser.parse_args()
	port = args.port
	ip = args.ip
	max_size = args.max_size
	##

	# check whether directory 'output_data' already exists
	if not os.path.exists('./output_data'):
	  os.mkdir('./output_data')
	  print("Folder %s created!" % './output_data')
	else:
	  print("Folder %s already exists" % './output_data')
	asyncio.run(main(port, ip, max_size))
