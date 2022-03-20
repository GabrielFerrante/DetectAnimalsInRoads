from zipfile import ZipFile

z = ZipFile('zipWithObjs.zip', 'r')
z.extractall(path='darknet/data/imagens/')
z.close()