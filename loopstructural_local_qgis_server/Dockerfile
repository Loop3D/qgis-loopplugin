
FROM continuumio/miniconda3
LABEL maintainer="michel.nzikoumamboukou@uwa.edu.au"
#This docker image has been adapted from the lavavu dockerfile
# install things
RUN apt-get update -qq && \
        DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends \
        gcc \
        g++ \
        libc-dev \
        make 

RUN apt-get update && apt-get install -y --no-install-recommends \
        libgl1 \
        libglib2.0-0 

#RUN conda install -c conda-forge gdal numpy scipy python=3.9 -y
RUN conda install -c conda-forge -c loop3d map2loop -y

RUN pip install websockets \
        LoopStructural \
        loopstructuralvisualisation





# copy the server folder into the container home directory 
COPY server ./server
