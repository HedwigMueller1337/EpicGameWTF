# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 15:30:25 2017

@author: schulung
"""
from dice import *
import itertools
from townevents import *
#from numpy.random import choice
# TO DO: 
# IMPORT CHARACTER DICE, EVENTS, BUILDINGS, RESOURCES ... from .txt files
# DEFINE PROPER IDENTIFIER FOR WORKERS


class building():
    # initialize the building
    # typename: building type description (e.g. mason's shop)
    # minWorkers: minimum workers for the buildig to be usable
    # maxWorkers: maximum workers the building can supply
    # cost: dict of resourceType:number 
    def __init__(self, typeName):
        self.possibleBuildings = {
                'masons shop': {'minWorkers':1, 'maxWorkers':2, 'cost':{'wood':-2, 'tool':-2}, 'dicePool':[ dice(['stone', 'stone', 'stone','stone', 'stone', 'accident']), dice(['stone','stone monument' ,'stone', 'exhaustion','stone brick', 'technology'])]}
                }
        self.cost = self.possibleBuildings[typeName]['cost']
        self.typeName = typeName
        self.minWorkers = self.possibleBuildings[typeName]['minWorkers']
        self.maxWorkers = self.possibleBuildings[typeName]['maxWorkers']
        self.dicePool = self.possibleBuildings[typeName]['dicePool']
        # list of workers
        self.workers = []
    def rollDice(self):
        result = []
        for i in range(len(self.workers)):
            result.append(self.dicePool[i].roll())
        return(result)
    # Add worker to building
    def addWorker(self, worker):
        # check if still available places
        if len(self.workers) == self.maxWorkers:
            print(self.typeName,' can only employ ', self.maxWorkers, ' workers')
        else:
            # the worker contributes his dice sides to the building
            workerIndex = len(self.workers)
            self.workers.append(worker)
            self.dicePool[workerIndex].extend(worker.dicePool)
    # remove worker from job
    # TO DO: ADD ERROR HANDLING
    def removeWorker(self, worker):
        self.workers.remove(worker)
        
class peasant():
    # initialize peasant by rolling dice for attributes
    def __init__ (self,
                 name,
                 physicalDice, 
                 educationDice, 
                 characterDice,
                 mentalDice,
                 specialDice):
        # initialize dice pool
        self.dicePool = [physicalDice.roll(), educationDice.roll(), characterDice.roll(), mentalDice.roll(), specialDice.roll()]
class town():
    def __init__(self):
        # dict for resources: typeString:number
        self.resources = dict()
        # list of buildings
        self.buildings = []
        # dict of peasants
        self.peasants = dict()

    def addResources(self, resourceChange):
        # resources: dict of resourceType:number
        # check if enough resources are available (if negative change values)
        for resourceType in resourceChange:
            if resourceType not in self.resources.keys():
                # resource not known yet
                self.resources[resourceType]  = 0 
            if self.resources[resourceType] < -resourceChange[resourceType]:
                print('not enough resources')
                return 0
        # add/ subtract resources
        for resourceType in resourceChange:
            self.resources[resourceType] +=  resourceChange[resourceType]
        return 1
    # add a building
    # buildingType: string describing building type
    def build(self, buildingType):
        newBuilding = building(buildingType)
        if self.addResources(newBuilding.cost):
            self.buildings.append(newBuilding)
    # roll the dice, specified by peasants, shops and items
    def rollDice(self):
        # this function rolls the dice of all buildings
        result = []
        for buildingIter in self.buildings:
            result.extend(buildingIter.rollDice())
        return result
