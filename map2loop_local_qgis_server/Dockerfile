
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

RUN conda install -c conda-forge gdal numpy scipy python=3.9 -y
RUN conda install -c conda-forge -c loop3d map2loop -y
RUN pip install websockets\
                matplotlib 

COPY server ./server



