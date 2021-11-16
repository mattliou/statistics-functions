#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
input: Take in four inputs as arguments, in this order: a: The prior probability of A, b: The prior probability of B, c: The likelihood
(the probability of B given A) and d: A flag (the number 1 or 2) whether this function will implement 1) the simple or 2) the
explicit version of Bayes theorem. If the flag is set to 2 (the explicit version), input argument b should be interpreted as “the
probability of B given not A”, instead of the prior probability of B. 
output:  posterior probability of A given B from the information given in the input arguments.
"""

def bayes_calc(PA,PB,L,flag):

    if flag == 1:

        posterior_simple = (PA*L)/(PB)

    return posterior_simple

    if flag == 2:

        posterior_explicit = (PA*L)/(L*PA+PB*(1-PA))

    return posterior_explicit