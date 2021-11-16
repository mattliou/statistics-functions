#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
input: A 1D numpy array of user-defined number of columns
output: A new 1D numpy array where elements have the median subtracted
        and made absolute. Finally returning the median of this new array
"""

import numpy as np

numRows = 1
numColumns = np.random.randint(10,size=20)

B = [1,2,3,4,5,6,7]

B = np.array([numColumns, numColumns])

print(B)

np.random.randint(20)

median = np.median(B)

inputArray = np.copy(B)


def median_abs_dev(inputArray):
    
    #Calculate the median values of inputArray
    median_value = np.median(inputArray)
    
    #initialize 2 arrays
    subtracted_median_array = []
    abs_subtracted_median_array = []
    
    #iterate over each index
    for i in range(len(inputArray)):
        
        #subtract median value from each i
        subtracted_median = inputArray[i] - median_value
        subtracted_median_array.append(subtracted_median)
        
        #make absolute each i
        abs_subtracted_median = np.abs(subtracted_median_array[i])
        abs_subtracted_median_array.append(abs_subtracted_median)
        
    #return final median
    median_final = np.median(abs_subtracted_median_array)
    
    return median_final

median_abs_dev(inputArray)