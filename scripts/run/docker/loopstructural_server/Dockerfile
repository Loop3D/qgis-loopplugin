FROM continuumio/miniconda3

# Set the maintainer label
LABEL maintainer="michel.nzikoumamboukou@uwa.edu.au"

# Update and install necessary system dependencies in a single RUN command to reduce image layers
RUN apt-get update -qq && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        gcc g++ libc-dev make libgl1 libglib2.0-0 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Configure conda solver and install required conda packages in a single step to improve efficiency
#RUN conda config --set solver classic && \
#    conda install -y -c conda-forge -c loop3d map2loop
RUN conda install -n base conda-libmamba-solver && conda config --set solver libmamba &&\
    conda install -y -c conda-forge -c loop3d map2loop

# Install Python dependencies in a single step
RUN pip install --no-cache-dir \
        websockets \
        LoopStructural \
        loopstructuralvisualisation \
        trame \
        trame-vtk \
        trame-vuetify \
        trame-components

# Copy the server folder into the container home directory
COPY server ./server