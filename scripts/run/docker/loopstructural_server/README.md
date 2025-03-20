# Map2loop server

## Running as docker

- The server can be run using docker by running `docker compose up --build` in the root directory of this repository. By default the server is mapped to the local port 8000, this can be changed in the docker compose file by editing the port mapping.

- To run the server in the background `docker compose up -d --build`

## Running the client in QGIS
- The following features or function are embedded into the qgis client function:
  - push the data to docker
  - execute map2loop inside the cdocker container
  - extract the result of map2loop.
A single push will toggle a prompt in which the user is required to input few data:
  
  username: your name or company name (not compusory for now)
  hostname: your remote machine IP ADRESSS (something like 123.45.678.90)
  portname: 8000 (the default port if you are using CET docker container)

## Running the client on your terminal.
- Run it and debug the error which mainly is caused by qt features. 



