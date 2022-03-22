from zipfile import ZipFile

z = ZipFile('zipWithObjs.zip', 'r')
z.extractall(path='darknet/images/')
z.close()