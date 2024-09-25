# Use the Miniconda base image
FROM continuumio/miniconda3

# Set the maintainer label
LABEL maintainer="michel.nzikoumamboukou@uwa.edu.au"

# Set non-interactive mode for apt-get
ARG DEBIAN_FRONTEND=noninteractive

# Update and install system dependencies
RUN apt-get update -qq && \
    apt-get install -yq --no-install-recommends \
    gcc \
    g++ \
    make \
    git \
    && rm -rf /var/lib/apt/lists/*

# Create a conda environment and install necessary packages
RUN conda create -n myenv python=3.9 gdal numpy scipy -c conda-forge -y

# Activate the environment and install additional dependencies
RUN /bin/bash -c "source activate myenv && \
    git clone https://github.com/Loop3D/map2loop.git && \
    cd map2loop && \
    conda install -c loop3d --file dependencies.txt && \
    pip install -e ."

# Install additional Python packages
RUN /bin/bash -c "source activate myenv && \
    pip install websockets matplotlib"

# Set the working directory
WORKDIR /app

# Copy the server directory into the container
COPY server ./server

# make new directory into your container
RUN mkdir ./server/source_data
RUN mkdir ./output_data



# Set the entrypoint (optional, depending on your application)
# If your application has a specific command to run, uncomment the next line
# CMD ["python", "server/app.py"]  # Change app.py to your entry script

# Activate the conda environment when running the container
ENTRYPOINT ["/bin/bash", "-c", "source activate myenv && exec bash"]














