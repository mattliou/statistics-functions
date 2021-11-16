#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
input: a 1D Array
output: a 2D Array returning the unique values as well as their frequencies in ascending value
"""

import numpy as np

A = np.array([1,2,1,2,1])

B = np.array([7,7,7,7.5,7.3])

inputArray = np.copy(A)

def catcounter(inputArray):
    
    (unique, counts) = np.unique(inputArray, return_counts=True)
    frequencies = np.asarray((unique,counts)).T

    print(frequencies)    
        
catcounter(inputArray)