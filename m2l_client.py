import asyncio
import websockets
import json
import base64
import glob, os
import time
from PyQt5.QtGui import QFont

##


def run_progressbar(self, i, N, flag, name):
    """
    This function is used to generate a progress bar
    # i   : file number i
    # N   : the total number of iteration or the total number of files
    # flag: the tyoe of the ongoing action
    # name: transferring files, can be None or a name.
    """
    # if flag=='PC ------> Server':
    self.map2loop_progressBar.setVisible(True)
    self.map2loop_progressBar.setGeometry(170, 100, 750, 25)
    self.map2loop_progressBar.setValue(int((i / N) * 100))
    self.map2loop_log_TextEdit.setGeometry(170, 150, 750, 300)
    self.map2loop_log_TextEdit.append(
        str(name) + " is transferring ..............." + "\n"
    )

    if i == N:
        if flag == "PC ------> Server":
            self.map2loop_log_TextEdit.append(
                "............END MODE: " + str(flag) + ".............. " + "\n"
            )
            self.map2loop_progressBar.setVisible(False)

        elif flag == "Server ------> PC":
            self.map2loop_log_TextEdit.append(
                "ALL RESULT DATA HAVE SUCCESSFULLY BEEN TRANSFERRED TO YOUR LOCAL PC"
                + "\n"
            )
            self.map2loop_log_TextEdit.append(
                "............END MODE: " + str(flag) + ".............. " + "\n"
            )
            self.map2loop_progressBar.setVisible(False)

        else:
            for i in range(5):
                self.map2loop_log_TextEdit.setFontWeight(QFont.Bold)
                self.map2loop_log_TextEdit.append("EXECUTING MAP2LOOP" + "\n")
    else:
        pass


async def data_uploader(
    filename, filepath, idx, how_many_file_need_to_be_sent, ip_adress, port_number
):
    """This function is used to transfert data (UPLOAD packet with binary data)
    into the server/docker container.
    UPLOAD your shape and dtm data to the server source_data folder
    # filename   : name of the file being transfered to the server
    # filepath   : source of the data filepath
    # idx        : file index used in counting the nbre of data so that we can break when we reach N
    # how_many_file_need_to_be_sent: (N=the total nbre of file to be transferred )
    # ip_adress  : host ip address
    # port_number: server ip address
    """
    uri = "ws://" + str(ip_adress) + ":" + str(port_number)
    async with websockets.connect(uri) as socket:
        end_upload_msg = []
        try:
            data = None
            with open(filepath, mode="rb") as file:
                data = file.read()
            encoded_data = base64.b64encode(data).decode("utf-8")
            package = {
                "client_id": 1,
                "project_id": 1,
                "function": "UPLOAD",
                "params": encoded_data,
                "filename": str(filename),
                "Length": how_many_file_need_to_be_sent,
            }
            await socket.send(json.dumps(package))
            resp = await socket.recv()
            resp = json.loads(resp)
            # Check whether all data are uploaded into the server
            if idx == how_many_file_need_to_be_sent:
                end_upload_msg.append(resp["response"])
            else:
                print(resp["error_msg"])
        except Exception as e:
            print(e)
    return end_upload_msg


async def map2loop_executor(conf_param, ip_adress, port_number):
    """This function is used to execute map2loop within the container
    # conf_param : configuration parameters need to execute map2loop
    # ip_adress  : host ip address
    # port_number: server ip address
    """
    uri = "ws://" + str(ip_adress) + ":" + str(port_number)
    async with websockets.connect(uri, ping_interval=None) as socket:
        map2loop_execution_msg = []
        map2loop_output = []
        try:
            package = {
                "client_id": 1,
                "project_id": 1,
                "function": "EXECUTE",
                "params": conf_param,
                "filename": "",
                "Length": "",
            }
            await socket.send(json.dumps(package))
            resp = await socket.recv()
            resp = json.loads(resp)
            if resp["success"]:
                map2loop_execution_msg.append(resp["response"])
                map2loop_output.append(resp["output_data"])
            else:
                print(resp["error_msg"])
        except Exception as e:
            print(e)
    return map2loop_output, map2loop_execution_msg


async def ping(self, ip_adress, port_number):
    """Simple ping test"""
    try:
        uri = "ws://" + str(ip_adress) + ":" + str(port_number)
        async with websockets.connect(uri, ping_interval=None) as socket:
            self.ping_message = []
            try:
                package = {
                    "client_id": 1,
                    "project_id": 1,
                    "function": "TEST",
                    "params": "Hello",
                    "filename": "",
                }
                await socket.send(json.dumps(package))
                resp = await socket.recv()
                resp = json.loads(resp)
                self.ping_message.append(resp["success"])
            except Exception as e:
                print(e)
                self.ping_message.append(e)
    except:
        self.ping_message.append("False")


async def map2loop_result_extractor(
    your_local_dir, list_server_data, server_filename, ip_adress, port_number
):
    """This function download data (DOWNLOAD packet to get binary data) from the docker container to your host machine
    # data_path       : results output data path within the docker container/server
    # server_filename : filename of the result output
    # ip_adress       : host ip address
    # port_number     : server ip address
    """
    uri = "ws://" + str(ip_adress) + ":" + str(port_number)
    async with websockets.connect(uri) as socket:
        try:
            package = {
                "client_id": 1,
                "project_id": 1,
                "function": "DOWNLOAD",
                "params": "",
                "filename": "",
                "serv_data": str(list_server_data),
            }

            await socket.send(json.dumps(package))
            resp = await socket.recv()
            resp = json.loads(resp)
            data = base64.b64decode(resp["response"].encode("UTF-8"))
            dir = str(your_local_dir) + str(server_filename)
            with open(str(dir), mode="wb") as file:
                file.write(data)
        except Exception as e:
            print("server filename: ", server_filename, e)


def m2l_client_main(
    self, userID, ip_adress, port_number, config_param, local_data_path
):
    """
    This is the main client connect and data transferring pipeline.

    # local_data_path  : local directory where the result data will be saved
    # ip_adress        : ip address of the remote server
    # userID           : the user name or company/ department
    # port_number      : the default port is 8000
    # config_param     : the configuration parameters extracted from data processing
    """
    try:
        asyncio.get_event_loop().run_until_complete(ping(self, ip_adress, port_number))
        if self.ping_message[0] == 1:
            self.map2loop_log_TextEdit.setVisible(True)
            self.map2loop_log_TextEdit.setGeometry(170, 150, 750, 300)
            self.map2loop_log_TextEdit.append(
                "Successfully connected to the host:: " + str(ip_adress) + "\n"
            )
            time.sleep(0.05)
            self.map2loop_log_TextEdit.append(
                "Let the magic happen!! " + str(ip_adress) + "\n"
            )
            # self.processed_data = (
            #     local_data_path + "/process_source_data_" + str(self.dt_string)
            # )
            time.sleep(0.05)
            list_of_data = glob.glob(
                local_data_path + "/process_source_data_" + str(self.dt_string) + "/*"
            )
            local_output_data_path = (
                str(local_data_path) + "/output_data_" + str(self.dt_string) + "/"
            )
            nbre_pc_data_to_server = len(list_of_data)
            filename = []
            for a in list_of_data:
                name_file = os.path.basename(os.path.normpath(a))
                filename.append(name_file)

            idx = 1  # Index for file counts
            outgoing_flag = (
                "PC ------> Server"  # action to tranfert data from pc to docker
            )
            self.map2loop_log_TextEdit.append(
                ".............. MODE: " + str(outgoing_flag) + ".............. " + "\n"
            )

            for file, filepath in zip(filename, list_of_data):
                print(
                    f"STATUS: Moving <<{file}>> to map2loop server source data - JOB: completed"
                )
                run_progressbar(self, idx, nbre_pc_data_to_server, outgoing_flag, file)
                all_data_uploaded_msg = asyncio.get_event_loop().run_until_complete(
                    data_uploader(
                        file,
                        filepath,
                        idx,
                        nbre_pc_data_to_server,
                        ip_adress,
                        port_number,
                    )
                )
                if idx == nbre_pc_data_to_server:
                    self.map2loop_log_TextEdit.append(
                        str(all_data_uploaded_msg[0]) + "\n"
                    )
                idx += 1

            (
                map2loop_output,
                map2loop_execution_msg,
            ) = asyncio.new_event_loop().run_until_complete(
                map2loop_executor(str(config_param), ip_adress, port_number)
            )
            self.map2loop_log_TextEdit.append(str(map2loop_execution_msg[0]) + "\n")

            data_str = map2loop_output[0].replace(" ", "")
            output_list = data_str.replace("{", "").replace("}", "").split(",")
            # Create a dictionary of server output data and filepath
            dictionary = {}
            for i in output_list:
                dictionary[i.split(":")[0].strip("'").replace('"', "")] = i.split(":")[
                    1
                ].strip("\"'")
            # Download data from the server/docker container
            index = 1  # Index for file counts
            nbre_server_data_to_pc = len(dictionary)  #  Nbre of result output
            incoming_flag = (
                "Server ------> PC"  #  action to tranfert data from docker to your pc
            )

            self.map2loop_log_TextEdit.append(
                ".............. MODE: " + str(incoming_flag) + ".............. " + "\n"
            )
            # print("filepath::::", filepath)
            for filename, filepath in dictionary.items():
                run_progressbar(
                    self, index, nbre_server_data_to_pc, incoming_flag, filename
                )
                asyncio.new_event_loop().run_until_complete(
                    map2loop_result_extractor(
                        local_output_data_path,
                        str(filepath),
                        str(filename),
                        ip_adress,
                        port_number,
                    )
                )
                index += 1
            self.Reload_btnPush.setVisible(True)

    except:
        self.map2loop_log_TextEdit.setVisible(True)
        network_message = [
            "OOOPS! OOOPS! OOOPS! Server is down",
            "Please email Michel Nzikou : ",
            " michel.nzikoumamboukou@uwa.edu.au ",
            "or Mark Jessel : ",
            "mark.jessell@uwa.edu.au",
        ]
        for msg in network_message:
            self.map2loop_log_TextEdit.setGeometry(170, 150, 750, 300)
            self.map2loop_log_TextEdit.append(str(msg) + "\n")


if __name__ == "__main__":
    m2l_client_main()
