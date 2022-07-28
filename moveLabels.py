import os

def move():


    pastaTrain = f'./YoloX-Model/Dataset/images/train/'
    pastaValid = f'./YoloX-Model/Dataset/images/val/'
    pastaLabelTrain = f'./YoloX-Model/Dataset/labels/train/'
    pastaLabelVal = f'./YoloX-Model/Dataset/labels/val/'
    for diretorio, subpastas, arquivos in os.walk(pastaTrain):
        for arquivo in arquivos:
            if arquivo.endswith(".txt"):
                os.popen(f"cp {pastaTrain}/{arquivo} {pastaLabelTrain}/{arquivo}")
    
    for diretorio, subpastas, arquivos in os.walk(pastaValid):
        for arquivo in arquivos:
            if arquivo.endswith(".txt"):
                os.popen(f"cp {pastaValid}/{arquivo} {pastaLabelVal}/{arquivo}") 


move()