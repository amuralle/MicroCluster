#Alex Muralles & Ruhani Mumick
#02-512 Final Project
#randomizeSelection.py

#Short algorithm used to select X random sequences from our gene ontology file


import random as rand


def pick(numberOfRandoms, textFile):
    newFile = open("random" + str(numberOfRandoms) + ".txt","w")
    aFile = open(textFile)
    fileLines = aFile.readlines()
    newFile.write(fileLines[0])

    data = range(1,len(fileLines))
    rand.shuffle(data)
    for i in range(len(data[:numberOfRandoms])):
        newFile.write(fileLines[data[i]])
    return
