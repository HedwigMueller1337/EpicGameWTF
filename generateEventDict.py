# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 22:46:51 2017

@author: kram
"""
from townevents import *

def generateEventDict():
    def findGems(city):
        print('a gem cluster was found and mined')
        city.addResources({'gem':random.randrange(3)})
    
    return {('stone', 'luck', 'discovery'):findGems,
            ('stone', 'stone'):findGems} 