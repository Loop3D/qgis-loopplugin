# Use the Miniconda base image
FROM continuumio/miniconda3

# Set the maintainer label
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

# Run loop3d and map2loop
RUN conda install -c conda-forge -c loop3d map2loop -y

# Install additional Python packages
RUN pip install websockets \
        LoopStructural \
        loopstructuralvisualisation


# copy the server folder into the container home directory 
COPY server ./server
