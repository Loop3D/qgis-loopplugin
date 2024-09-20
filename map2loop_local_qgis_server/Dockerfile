
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
###
RUN conda install -c conda-forge gdal numpy scipy python=3.9 -y

#RUN conda install -c conda-forge -c loop3d map2loop -y
RUN git clone https://github.com/Loop3D/map2loop.git && cd map2loop && conda install -c loop3d --file dependencies.txt && pip install -e .
#RUN conda install -c conda-forge -c loop3d map2loop=3.1.12 loopprojectfile=0.1.3 -y
# RUN conda install --override-channels -c loop3d -c conda-forge map2loop=3.1.12 -y

# RUN conda install -c conda-forge -c loop3d map2loop=3.1.12 -y
# RUN pip install loopprojectfile==0.1.3


RUN pip install websockets\
    matplotlib 

# copy server into the container
COPY server ./server

# make new directory into your container
#RUN mkdir ./server/source_data
#RUN mkdir ./output_data

