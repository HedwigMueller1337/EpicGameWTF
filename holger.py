# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 14:08:05 2017

@author: schulung
"""
# general test file for game objects
import numpy as np
from holgerObjects import *
from townevents import *
from fileReader import *
from dice import *

if __name__ == '__main__':
    
    exampleTown = town()
    # check resources
    print(exampleTown.resources)
    # add resources 
    exampleTown.addResources({'wood':20, 'tool':5, 'rope':5, 'clay':5})
    print(exampleTown.resources)
    # warning
    exampleTown.addResources({'wood':-20})
    print(exampleTown.resources)
    # check workers
    # to do: read as text file, weights, more (inspiration: http://www.ckiiwiki.com/Traits, http://dwarffortresswiki.org/index.php/DF2014:Personality_trait, http://dwarffortresswiki.org/index.php/DF2014:Attribute)
    educationDefault = dice(['language', 'combat', 'scholar', 'medicine', 'craftsman', 'supervisor'])
    physicalDefault = dice(['strength', 'endurance', 'speed', 'athletic', 'weakness'])
    mentalDefault  = dice(['creativity', 'aestetics', 'logic', 'charisma', 'paranoid'])
    characterDefault = dice(['anger', 'courage', 'intrigue', 'lazyness', 'curiosity'])
    fateDefault= dice([None, None, None, None, 'luck', 'mutiny', 'discovery', 'breakdown'])
    
    # add two peasants with random default dice
    helmut = peasant('helmut', educationDefault, physicalDefault, mentalDefault, characterDefault, fateDefault)
    emil = peasant('emil', educationDefault, physicalDefault, mentalDefault, characterDefault, fateDefault)
    peter = peasant('peter', educationDefault, physicalDefault, mentalDefault, characterDefault, fateDefault)
    günther = peasant('günther', educationDefault, physicalDefault, mentalDefault, characterDefault, fateDefault)

    # add buildings to town
    print('before building', exampleTown.resources)
    exampleTown.build('masons shop')
    exampleTown.build('masons shop')
    exampleTown.build('masons shop')
    print('after building', exampleTown.resources)
    # add workers to buildings
    exampleTown.buildings[0].addWorker(helmut)
    exampleTown.buildings[0].addWorker(emil)
    exampleTown.buildings[0].addWorker(peter)
    exampleTown.buildings[1].addWorker(peter)
    exampleTown.buildings[1].addWorker(günther)    
    # roll dice with worker/shop configuration
    diceRollExample = exampleTown.rollDice()
    print(diceRollExample)
    
    # check events-
    Events = events()
    # check None handling
    noneExample = [None, 'technology', None, 'exhaustion']
    Events.checkEvents(noneExample)
    
    # eventList = Events.checkEvents(diceRollExample)
    
    # check events for fixed example
    eventExample = ['stone', 'luck', 'discovery', 'stone', 'stone']
    eventList = Events.checkEvents(eventExample)
    
    for eventIter in eventList:
        eventDict[eventIter](exampleTown)
    print(exampleTown.resources)
    
    # read file with one level
    actions = fileReader('actions')
    
    # roll example action dice
    print(actions['Explore'].roll())
    
    # read file with tow levels
    items = fileReader('items')



    
    
    