import os

def move():


    pastaTrain = f'./yolov5/data/images/train'
    pastaValid = f'./yolov5/data/images/val'
    pastaLabel = f'./yolov5/data/labels'
    for diretorio, subpastas, arquivos in os.walk(pastaTrain):
        for arquivo in arquivos:
            if arquivo.endswith(".txt"):
                os.popen(f"cp {pastaTrain}/{arquivo} {pastaLabel}/{arquivo}")
    
    for diretorio, subpastas, arquivos in os.walk(pastaValid):
        for arquivo in arquivos:
            if arquivo.endswith(".txt"):
                os.popen(f"cp {pastaValid}/{arquivo} {pastaLabel}/{arquivo}") 


move()