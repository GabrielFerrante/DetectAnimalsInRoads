import os

def move():


    pastaTrain = f"./YoloV7-Model/BRA-Dataset/images/train/"
    pastaValid = f'./YoloV7-Model/BRA-Dataset/images/val/'
    pastaLabelTrain = f'./YoloV7-Model/BRA-Dataset/labels/train/'
    pastaLabelVal = f'./YoloV7-Model/BRA-Dataset/labels/val/'
    for diretorio, subpastas, arquivos in os.walk(pastaTrain):
        for arquivo in arquivos:
            if arquivo.endswith(".txt"):
                os.popen(f"cp {pastaTrain}/{arquivo} {pastaLabelTrain}/{arquivo}")
    
    for diretorio, subpastas, arquivos in os.walk(pastaValid):
        for arquivo in arquivos:
            if arquivo.endswith(".txt"):
                os.popen(f"cp {pastaValid}/{arquivo} {pastaLabelVal}/{arquivo}") 


move()