# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 21:51:01 2017

@author: kram
"""
"""
read txt.file specifying dice
# dicename
side, weight
side, weight
...
# dicename2
side, weight
...
#

"""
from dice import *

def fileReader(fileName):
# open file
    with open(fileName +'.txt') as f:
        # initalise top level dict
        toplevelDict = dict()    

        # read text as list of lines
        lines = f.readlines()
        # strip ws and empty lines
        cleanLines = [l.strip() for l in lines if l.strip()]
        # find elements with # as first symbol and create list of indices        
        hashIndices = [i for i,x in enumerate(cleanLines) if x[0] == '#']
        for i in range(len(hashIndices)):
            # name of dice
            diceName = cleanLines[hashIndices[i]].split()[1]
            # all contents of the dice as assigned in file
            if i != len(hashIndices)-1:
                diceSides = cleanLines[hashIndices[i] +1 : hashIndices[i+1]]
            else:
                diceSides = cleanLines[hashIndices[i]+1 :]
            # split sides and weights
            diceSides = [d.split() for d in diceSides];
            diceWeights = [int(d[1]) for d in diceSides];
            diceSides = [d[0]for d in diceSides];
            # generate dice with name and sides
            #print(toplevelDict)
            toplevelDict[diceName] = dice(diceSides, diceWeights)
            # example roll with created dice
        # return dice dic
        return toplevelDict