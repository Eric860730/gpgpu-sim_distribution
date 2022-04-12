FROM ubuntu:20.04
RUN apt-get update
RUN apt-get upgrade -y
RUN DEBIAN_FRONTEDN=noninteractive TZ=Asia/Taipei apt-get -y install tzdata
RUN apt-get install -y openjdk-8-jdk git python3-dev python3-numpy python3-six build-essential python3-pip swig python3-wheel libcurl3-dev libcupti-dev software-properties-common
RUN add-apt-repository ppa:graphics-drivers/ppa
RUN apt update
RUN apt install -y build-essential xutils-dev bison zlib1g-dev flex libglu1-mesa-dev doxygen graphviz libpng-dev libxi-dev libxmu-dev freeglut3-dev wget git git-gui ctags cscope libboost-dev vim
RUN wget -O /tmp/cuda_10.0.130_410.48_linux https://developer.nvidia.com/compute/cuda/10.0/Prod/local_installers/cuda_10.0.130_410.48_linux
RUN chmod +x /tmp/cuda_10.0.130_410.48_linux
RUN /tmp/cuda_10.0.130_410.48_linux --override -silent -toolkit
RUN git clone https://github.com/gpgpu-sim/gpgpu-sim_distribution.git /root/gpgpu-sim_distribution

