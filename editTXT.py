import os

search = "../Dataset/images/val/"

troca = "../Dataset/images/"


with open(r'val.txt', 'r') as file:
    data = file.read()

    data = data.replace(search, troca)


with open(r'val.txt', 'w') as file:
  
    # Writing the replaced data in our
    # text file
    file.write(data)
  
# Printing Text replaced
print("Text replaced")