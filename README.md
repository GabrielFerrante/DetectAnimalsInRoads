# DetectAnimalsInRoads

Single-stage detectors for edge computing with CNN architecture to detect animals that suffer the most accidents on Brazilian highways.
Using the BRA-Dataset, a specific dataset about these animals, the detectors were trained and validated in the laboratory and in controlled locations with real animals.

This project is a master's project in computer science and computational mathematics at the University of São Paulo (PPG-CCMC, ICMC-USP)

<details open>
<summary>Important Links </summary>
  
- [INSTALL CUDA, OPENCV4 and cuDNN]
  
- [YOLOV4 Darknet Model]  
  
- [YOLOV5 Pytorch Model]

- [Scaled-YOLOV4]

- [YOLOR]

- [YOLOX]
  
- [MORE MODELS]

</details>

# PROCESSO DE INSTALAÇÃO: CUDA e OPENCV4 

Instalar o CUDA
https://medium.com/geekculture/install-cuda-and-cudnn-on-windows-linux-52d1501a8805#68ce

sudo apt-get update
sudo apt-get upgrade

sudo apt-get install build-essential cmake unzip pkg-config
sudo apt-get install gcc-6 g++-6 
sudo apt-get install libxmu-dev libxi-dev libglu1-mesa libglu1-mesa-dev
sudo apt-get install libjpeg-dev libpng-dev libtiff-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libxvidcore-dev libx264-dev
sudo apt-get install libopenblas-dev libatlas-base-dev liblapack-dev gfortran
sudo apt-get install libhdf5-serial-dev
sudo apt-get install python3-dev python3-tk python-imaging-tk
sudo apt-get install libgtk-3-dev

sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt update

sudo apt-get install nvidia-driver-470

em ~

wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-wsl-ubuntu.pin

sudo mv cuda-wsl-ubuntu.pin /etc/apt/preferences.d/cuda-repository-pin-600

wget https://developer.download.nvidia.com/compute/cuda/11.4.0/local_installers/cuda-repo-wsl-ubuntu-11-4-local_11.4.0-1_amd64.deb

sudo dpkg -i cuda-repo-wsl-ubuntu-11-4-local_11.4.0-1_amd64.deb

sudo apt-key add /var/cuda-repo-wsl-ubuntu-11-4-local/7fa2af80.pub

sudo apt-get update

sudo apt-get -y install cuda


No ~./bashrc do usuário linux, acrescentar:

export PATH=/usr/local/cuda-11.0/bin:${PATH}
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=/usr/local/cuda-11.0/lib64:${LD_LIBRARY_PATH}
export CUDA_HOME=/usr/local/cuda

Instalar o CUDNN, baixe o arquivo
https://developer.nvidia.com/rdp/cudnn-download


Baseado em https://github.com/tensorflow/tensorflow/issues/41041 
Extrair o .tz e copiar as libs:

tar -xzvf cudnn-x.x-linux-x64-v8.x.x.x.tgz

cd cudnn-x.x-linux-x64-v8.x.x.x.tgz

sudo cp include/cudnn*.h /usr/local/cuda/include
sudo cp lib64/libcudnn* /usr/local/cuda/lib64
sudo chmod a+r /usr/local/cuda/include/cudnn*.h /usr/local/cuda/lib64/libcudnn*


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

MÉTODO COM O OPENCV DO REPOSITÓRIO DO UBUNTU

sudo apt install python-opencv
sudo apt install libopencv-dev

pip3 install opencv-python


MÉTODO COM O SOURCE DO OPENCV

sudo apt-get install git
git clone https://github.com/opencv/opencv.git


mkdir build
cd build

cmake -DPYTHON_DEFAULT_EXECUTABLE=/usr/bin/python3 -DOPENCV_GENERATE_PKGCONFIG=ON ../

make -j16

sudo make install

TESTE A GPU

python3 TestGPU.py




