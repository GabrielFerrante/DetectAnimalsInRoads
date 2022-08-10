import os
from re import L
from shutil import move


#EXECUTAR 2 VEZES O SCRIPT

def createValid():
    # o que o codigo abaixo faz: adiciona o nome e caminho de todos as fotos (.jpg) em um txt
    
        
    pasta = f'./YoloV7-Model/BRA-Dataset/images/train'
    animals = ["anta", "jaguarundi", "loboGuara", "oncaParda", "tamanduaBandeira"]
    

    for diretorio, subpastas, arquivos in os.walk(pasta):
        if len(arquivos) == 0:
            print("N tem imagens no train")
        if len(getValidImages()) > 0:
            print("ja tem no valid as imagens")
        else:
            
            for animal in animals:
                aux = []
                for arquivo in arquivos:
                    if arquivo.count(animal) > 0:
                        aux.append(arquivo)
                for arquivo in aux[int(0.8 * len(aux)):]:
                    if arquivo.endswith(".jpg"):
                        os.replace(f"{pasta}/{arquivo}", f"./YoloV7-Model/BRA-Dataset/images/val/{arquivo}")
                   
               
    

def getValidImages():
    pastaVal = f"./YoloV7-Model/BRA-Dataset/images/val/"
    imagesValida = []
    for diretorio, subpastas, arquivos in os.walk(pastaVal):
        for arquivo in arquivos:
            imagesValida.append(arquivo)    
    return imagesValida

def getValidLabels(imagens):

    print(len(imagens))
    pasta = f"./YoloV7-Model/BRA-Dataset/images/train"
        
    for diretorio, subpastas, arquivos in os.walk(pasta):
        if len(arquivos) == 0:
            print("N tem imagens no train")
        else:
            for arquivo in imagens:
                arquivo1 = arquivo.replace(".jpg",".txt")
                os.replace(f"{pasta}/{arquivo1}", f"./YoloV7-Model/BRA-Dataset/images/val/{arquivo1}") 
                


createValid()
getValidLabels(getValidImages())