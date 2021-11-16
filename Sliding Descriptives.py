#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
input: 1D or 2D array which gets computed in series of window sizes
output: depending on parameter stated, a new output array will be returned
"""

import numpy as np

A = np.array([[1,2,3,4,5],[6,7,8,9,10]])

B = np.array([1,2,3,4,5,6,7,8,9,10])

inputArray = np.copy(B)

print('input array:', inputArray)

def sliding_descriptives(inputArray, param_calc, window_size):
        
    num_windows = int(np.ceil(len(inputArray)/window_size))

    #initialize outuput array
    placeholder = []
    
    for i in range(num_windows*2):
        start = i
        end = i + window_size
            
        window = inputArray[start:end]
        print(window)
        
        if end > len(inputArray):
            end = len(inputArray)
        
        if param_calc == "mean" :
            
            window_mean = np.mean(window)
            placeholder.append(window_mean)
            
            #print(window_mean)
            print('output array:', placeholder)

            #return placeholder
        
        elif param_calc == "sd" :
            
            window_sd = np.std(window, axis=0)
            placeholder.append(window_sd)
            
            #print(window_sd)
            print('output array:', placeholder)
                
            #return placeholder
        
        
    if param_calc == "corr" :
        for i in range(num_windows):
            start = i
            end = i + window_size
            
            window_1 = inputArray[0][start:end]
            window_2 = inputArray[1][start:end]
            
            if end>len(inputArray[0]):
                end = len(inputArray[0])
        
            window_corr = np.corrcoef(window_1, window_2)
            placeholder.append(window_corr)
            
            print('output array:', placeholder)
            
            
            #return placeholder
        
        
sliding_descriptives(inputArray, 'mean', 3)
        