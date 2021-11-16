#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
input: dataset that gets its normalization error calculcated, specificed
output: single-value output calcuation of the RMSE
"""

import numpy as np

B = np.array([[1,2],[2,4],[3,1],[4,6],[5,2]])

inputArray = np.copy(B)

def norm_error(inputArray, flag):
    
    counter1 = 0 #counter1 is the index loc of predictions array
    counter2 = 1 #counter2 is the index loc of measurements array
    
    templist = [] #empty list to append items from 2D inputArray
    templist2 = [] #empty list to append difference btw pred and measure
    predictions = [] #empty list to append prediction values
    measurements = [] #empty list to append measurement values
    
    for row in inputArray: 
        for item in row:
            templist.append(item)
            
    #iterate over templist to append new values to predictions and measurements        
    for item in range(len(templist)):
            
            if counter1 < 10:
                predictions.append(templist[counter1])
                counter1 += 2
                
            if counter2 < 10:
                measurements.append(templist[counter2])
                counter2 += 2       
    
    for i in range(len(predictions)):
        diff = predictions[i] - measurements[i]
        templist2.append(diff)
        
    overall_diff = np.abs(templist2)
    overall_diff_flagged = pow(overall_diff, flag)
    divided_by_n = (np.sum(overall_diff_flagged) / len(predictions))
    ne = pow(divided_by_n, 1/flag)
    
    print("normalization error is: ", ne)
        
norm_error(inputArray, 2)