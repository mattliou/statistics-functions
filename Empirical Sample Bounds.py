#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
input: 1D array along with sample bounds: 5,90,95
output: 2 variables of upper and lower percentile
"""

from numpy import genfromtxt

my_data = genfromtxt('sampleInput1.csv', delimiter=',')

def empirical_sample_bounds(my_data, bound):
    
    sorted_data = sorted(my_data)
    length = len(sorted_data)
    one_percentile = length/100
    
    mass_prob = (100-bound)/2
    upper_bound = 100-mass_prob
    lower_bound = 0+mass_prob

    lower_index = int(lower_bound * one_percentile) - 1
    upper_index = int(upper_bound * one_percentile) - 1

    print('lower: ', sorted_data[lower_index], 'upper: ', sorted_data[upper_index])

empirical_sample_bounds(my_data, 95)