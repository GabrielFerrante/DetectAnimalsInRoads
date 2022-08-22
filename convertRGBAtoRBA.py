import PIL.Image
import os

pastaTrain = f"./Dataset_COCO_format/images/train2017/"
pastaValid = f'./Dataset_COCO_format/images/val2017/'
for diretorio, subpastas, arquivos in os.walk(pastaTrain):
        for arquivo in arquivos:
            if arquivo.endswith(".jpg"):
                rgba_image = PIL.Image.open(f'{pastaTrain}{arquivo}')
                rgb_image = rgba_image.convert('RGB')
                rgb_image.save(f'{pastaTrain}{arquivo}')

for diretorio, subpastas, arquivos in os.walk(pastaValid):
        for arquivo in arquivos:
            if arquivo.endswith(".jpg"):
                rgba_image = PIL.Image.open(f'{pastaValid}{arquivo}')
                rgb_image = rgba_image.convert('RGB')
                rgb_image.save(f'{pastaValid}{arquivo}')