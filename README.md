# DetectorAnimalsInRoads

Instalar o CUDA para WSL2
https://ubuntu.com/tutorials/enabling-gpu-acceleration-on-ubuntu-on-wsl2-with-the-nvidia-cuda-platform#1-overview

Instalar o CUDNN
https://developer.nvidia.com/rdp/cudnn-download


Baseado em https://github.com/tensorflow/tensorflow/issues/41041 
Extrair o .tz e copiar as libs:

tar -xzvf cudnn-x.x-linux-x64-v8.x.x.x.tgz

sudo cp cuda/include/cudnn*.h /usr/local/cuda/include
sudo cp cuda/lib64/libcudnn* /usr/local/cuda/lib64
sudo chmod a+r /usr/local/cuda/include/cudnn*.h /usr/local/cuda/lib64/libcudnn*

No ~./bashrc do usuário linux, acrescentar:

export PATH=/usr/local/cuda-11.0/bin:${PATH}
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=/usr/local/cuda-11.0/lib64:${LD_LIBRARY_PATH}
export CUDA_HOME=/usr/local/cuda


INSTALAR O OPENCV4

sudo apt-get install cmake
sudo apt-get install gcc g++

sudo apt-get install python3-dev python3-numpy

sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev
sudo apt-get install libgstreamer-plugins-base1.0-dev libgstreamer1.0-dev


sudo apt-get install libgtk-3-dev

sudo apt-get install libpng-dev
sudo apt-get install libjpeg-dev
sudo apt-get install libopenexr-dev
sudo apt-get install libtiff-dev
sudo apt-get install libwebp-dev


sudo apt-get install git
git clone https://github.com/opencv/opencv.git


mkdir build
cd build

cmake -DPYTHON_DEFAULT_EXECUTABLE=/usr/bin/python3 -DOPENCV_GENERATE_PKGCONFIG=ON ../

make -j16

sudo make install

Ou, pode optar pelo pacote de instalação para WSL2:

https://github.com/Christophe-Foyer/darknet_wsl_cuda_install_scripts
