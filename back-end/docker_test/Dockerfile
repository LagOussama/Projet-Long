FROM ubuntu

# add a non-root user
#RUN useradd -ms /bin/bash shark

# tell environment we're not able to respond to quesitons
ENV DEBIAN_FRONTEND noninteractive

# install python and curl packages
RUN apt-get update && \
    apt-get install -y python3.6 && \
    apt-get install -y python3-distutils && \
    apt-get install -y curl

COPY ./requirement.txt .
# fix pip
RUN curl -O https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python3 get-pip.py && \
    rm get-pip.py

# install pyshark and wireshark
RUN apt-get install -y  tshark && \
    apt install -y iproute2 && \
    pip install -r requirement.txt

# add group wireshark, add shark user and give right permissions


#RUN dpkg-reconfigure wireshark-common

# Copy the current directory contents into the container at /app
COPY ./src/ /app

# Set the working directory to /app
WORKDIR /app

# switch to user shark
#USER shark
USER root
#CMD bash ./websnif.sh
