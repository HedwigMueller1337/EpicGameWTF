# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 21:22:29 2017

@author: kram
"""
import random
class dice():
    # sides: list of sides
    def __init__(self, sides = [], weights = []):
        self.sides = sides
        self.weights = weights
    # add sides to dice
    def extend(self, newSides):
        self.sides.extend(newSides)
    # remove dice sides
    def remove(self, remSides):
        self.sides.remove(remSides)
    # roll dice
    def roll(self):
         if self.weights == []:
             return random.choice(self.sides)
         else:
             return random.choices(self.sides, self.weights)