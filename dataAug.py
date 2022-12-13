#HS = Horizontal Shift
#VS = Vertical Shift
#BG = Brightness
#HF = Horizontal Flip
#VF = Vertical Flip
#RT = Rotation
#NS = Random Noise

#Librarys
import cv2
import random
import os
import numpy as np
from skimage.util import random_noise
from skimage import io, img_as_ubyte



def fill(img, h, w):
    img = cv2.resize(img, (h, w), cv2.INTER_CUBIC)
    return img
        
def horizontal_shift(img, nome, ratio=0.0):
    print(type(img))
    if ratio > 1 or ratio < 0:
        print('Value should be less than 1 and greater than 0')
        return img
    ratio = random.uniform(-ratio, ratio)
    h, w = img.shape[:2]
    to_shift = w*ratio
    if ratio > 0:
        img = img[:, :int(w-to_shift), :]
    if ratio < 0:
        img = img[:, int(-1*to_shift):, :]
    img = fill(img, h, w)
    cv2.imwrite("HS-"+nome, img)

def vertical_shift(img, nome, ratio=0.0):
    if ratio > 1 or ratio < 0:
        print('Value should be less than 1 and greater than 0')
        return img
    ratio = random.uniform(-ratio, ratio)
    h, w = img.shape[:2]
    to_shift = h*ratio
    if ratio > 0:
        img = img[:int(h-to_shift), :, :]
    if ratio < 0:
        img = img[int(-1*to_shift):, :, :]
    img = fill(img, h, w)
    cv2.imwrite("VS-"+nome, img)

def brightness(img, low, high, nome):
    value = random.uniform(low, high)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hsv = np.array(hsv, dtype = np.float64)
    hsv[:,:,1] = hsv[:,:,1]*value
    hsv[:,:,1][hsv[:,:,1]>255]  = 255
    hsv[:,:,2] = hsv[:,:,2]*value 
    hsv[:,:,2][hsv[:,:,2]>255]  = 255
    hsv = np.array(hsv, dtype = np.uint8)
    img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    cv2.imwrite("BG-"+nome, img)

def horizontal_flip(img, flag, nome):
    if flag:
        img = cv2.flip(img, 1)
        cv2.imwrite("HF-"+nome, img)
    else:
        return img

def vertical_flip(img, flag, nome):
    if flag:
        img = cv2.flip(img, 0)
        cv2.imwrite("VF-"+nome, img)
    else:
        return img

def rotation(img, angle, nome):
    angle = int(random.uniform(-angle, angle))
    h, w = img.shape[:2]
    M = cv2.getRotationMatrix2D((int(w/2), int(h/2)), angle, 1)
    img = cv2.warpAffine(img, M, (w, h))
    cv2.imwrite("RT-"+nome, img)

def noise(img, nome):
    img = random_noise(img)
    img = img_as_ubyte(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.imwrite('NS-'+nome, img)
    

#./BRA-Dataset/images/train/

#Lendo as imagens de treino
pasta = f'./BRA-Dataset/images/train'
for diretorio, subpastas, arquivos in os.walk(pasta):
    if len(arquivos) == 0:
        print("N tem imagens no images")
    else:
        for arquivo in arquivos:
            if arquivo.endswith(".jpg") and arquivo=='anta00000000.jpg':
                img = cv2.imread('./BRA-Dataset/images/train/'+arquivo)
                horizontal_shift(img, arquivo,0.7)
                vertical_shift(img, arquivo, 0.6)
                brightness(img, 0.5, 4, arquivo)
                horizontal_flip(img, True, arquivo)
                vertical_flip(img, True, arquivo)
                rotation(img, 30, arquivo)
                noise(img, arquivo)
