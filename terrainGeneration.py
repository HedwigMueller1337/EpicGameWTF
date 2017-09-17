# -*- coding: utf-8 -*-
"""

"""

from holgerObjects import *
import numpy as np
from scipy.ndimage.filters import gaussian_filter
# for evaluation only
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# create hills by random noise and convolution with gaussian blur
class altitudeMap:
    # initialize random altitude map
    # size           list of [sizeX, sizeY]
    # maxAltitude    max Altitude     
    # sigma          list of [sigmaX, sigmaY]
    def __init__(self, size, altitude, sigma):
        # create random map and blur it to create terrain-like structure
        self.M = gaussian_filter(altitude * np.random.rand(size[0], size[1]), sigma)

    
    