import os
from re import L



def createTrain():
    # o que o codigo abaixo faz: adiciona o nome e caminho de todos as fotos (.jpg) em um txt
    imagensTrain = []
    imagensValid = []

    
        
    pastaTrain = f'./BRA-Dataset/images/train/'
    pastaValid = f'./BRA-Dataset/images/valid/'
    for diretorio, subpastas, arquivos in os.walk(pastaTrain):
        for arquivo in arquivos:
            if arquivo.endswith(".jpg"):
                print(arquivo)
                imagensTrain.append(f"images/train/" + arquivo)
            
    for diretorio, subpastas, arquivos in os.walk(pastaValid):
        contador = 0
        for arquivo in arquivos:
            if arquivo.endswith(".jpg"):
                contador = contador + 1
                print(contador)
                imagensValid.append(f"images/valid/" + arquivo)

    with open("train.txt", "w") as outfile:
        for img in imagensTrain:
            outfile.write(img)
            outfile.write("\n")            
        outfile.close()
    
    with open("valid.txt", "w") as outfile:
        for img in imagensValid:
            outfile.write(img)
            outfile.write("\n")            
        outfile.close()
createTrain()