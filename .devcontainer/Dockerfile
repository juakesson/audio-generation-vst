FROM mcr.microsoft.com/devcontainers/python:0-3.11
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \ 
&& apt-get -y install git
RUN apt-get install -y python3-pip
RUN pip install numpy
RUN pip install torch
