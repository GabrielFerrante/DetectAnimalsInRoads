import os
from re import L
from shutil import move




def createTrain():
    # o que o codigo abaixo faz: adiciona o nome e caminho de todos as fotos (.jpg) em um txt
    
    #Todas as imagens com labels na pasta images do yolov5
    pasta = f'./BRA-Dataset/images'
    
    for diretorio, subpastas, arquivos in os.walk(pasta):
        if len(arquivos) == 0:
            print("N tem imagens no images")
        else:
            for arquivo in arquivos:
                if arquivo.endswith(".jpg") or arquivo.endswith(".txt"):
                    os.replace(f"{pasta}/{arquivo}", f"{pasta}/train/{arquivo}")  
                
                    
    

createTrain()
