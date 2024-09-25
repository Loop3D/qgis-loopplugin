# Use the Miniconda base image
FROM continuumio/miniconda3

# Set the maintainer label
LABEL maintainer="michel.nzikoumamboukou@uwa.edu.au"

# Update and install system dependencies
RUN apt-get update -qq && \
    DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends \
    gcc \
    g++ \
    libc-dev \
    make 

# Run loop3d and map2loop
RUN conda install -c conda-forge -c loop3d map2loop -y

# Install additional Python packages
RUN pip install websockets\
    matplotlib 

# Copy the server directory into the container
COPY server ./server

# make new directory into your container
#RUN mkdir ./server/source_data
#RUN mkdir ./output_data

