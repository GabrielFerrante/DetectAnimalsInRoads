import os
from re import L
from shutil import move




def createTrainAndValid():
    # o que o codigo abaixo faz: adiciona o nome e caminho de todos as fotos (.jpg) em um txt
    
        
    pasta = f'./yolov5/data/images/train'
        
    for diretorio, subpastas, arquivos in os.walk(pasta):
        if len(arquivos) == 0:
            print("N tem imagens no train")
        else:
            for arquivo in arquivos[int(0.8 * len(arquivos)):]:
                if arquivo.endswith(".jpg"):
                    os.replace(f"{pasta}/{arquivo}", f"./yolov5/data/images/val/{arquivo}") 
                if arquivo.endswith(".txt"):
                    os.replace(f"{pasta}/{arquivo}", f"./yolov5/data/images/val/{arquivo}") 
    

createTrainAndValid()