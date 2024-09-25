
FROM continuumio/miniconda3
LABEL maintainer="michel.nzikoumamboukou@uwa.edu.au"
# 
RUN apt-get update -qq && \
    DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends \
    gcc \
    g++ \
    libc-dev \
    make 
#
RUN conda install -c conda-forge gdal numpy scipy python=3.9 -y

RUN git clone https://github.com/Loop3D/map2loop.git && cd map2loop && conda install -c loop3d --file dependencies.txt && pip install -e .

RUN pip install websockets\
    matplotlib 

# copy server into the container
COPY server ./server

# make new directory into your container
#RUN mkdir ./server/source_data
#RUN mkdir ./output_data

