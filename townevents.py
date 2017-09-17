# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 11:10:31 2017

@author: schulung
"""
import random
import itertools
# define event handling functions here. They must always have the town (and only the town) as a parameter
def findGems(town):
    town.addResources({'gems':random.randint(3,6),})
    print('The miners struck a gem mine!')
def stoneMining(town):
    town.addResources({'stone':random.randint(2,10),})
    print('The miners mined some stone!')
def eventDummy(town):
    pass

# define events, defined by a side combination and a handling function
eventDict = {('stone', 'luck', 'discovery'):findGems,
             ('stone', 'stone'):stoneMining}

#[('stone', 'stone'), ('strength', 'stone'), ('luck', 'stone'), ('accident', 'stone'), ('anger', 'luck'), ('supervisor', 'anger'), ('stone', 'stone brick'), ('stone', 'luck', 'discovery')]

# list of possible events
eventList = eventDict.keys()

# this class handles events by assigning function
class events():
    def __init__(self):
        # event list: dict of identifier and tupel of required dice each event requires at least 2 dice
        self.eventList = eventList
        # maximal combinations that have to be calculated (= size of biggest event dice tuple)
        self.maxDice = max([len(t) for t in self.eventList])
        # check what events ocurr based on dice rolls
    def checkEvents(self, rolls):
        # remove blank dice sides
        while None in rolls:
            rolls.remove(None)
        # function for calculation of possible combinations
        def calculatePossibleEvents(sides):
            possibleEvents = []
            for i in range(self.maxDice):
                if i+1 > 1:
                    possibleEvents.extend(list(itertools.combinations(tuple(rolls), i+1)))
            return possibleEvents
        
        # possible events from dice
        possibleEvents = calculatePossibleEvents(rolls)
        # TO DO: Cleaner implementation (this implementation sucks) 
        # find events (events with the most dice are handled first)
        sideCombination = possibleEvents[-1]
        # list of occured events
        occurredEventList = []
        while sideCombination in possibleEvents:
            # Event exists 
            if sideCombination in self.eventList:
                # handle event
                print('event', sideCombination)
                occurredEventList.append(sideCombination)
                # remove used dice
                for i in range(len(sideCombination)):
                    rolls.remove(sideCombination[i])
                possibleEvents = calculatePossibleEvents(rolls)
            else: # event hypothesis not in list
                del possibleEvents[-1]
            # exit function if list has been checked
            if len(possibleEvents) > 0:
            #check next element
                sideCombination = possibleEvents[-1]
            else:
                break
        return occurredEventList
