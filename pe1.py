#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 16:16:10 2018

@author: Frevel
"""

def sum_multiples(limit):
    '''
    Computes the multiples of 3 and 5 up to limit and returns the sum of these
    multiples.
    
    x (int) : upper limit
    Returns int
    '''
    sum = 0
    for i in range(0, limit, 3):
        if i % 5 != 0: sum += i
    for i in range(0, limit, 5):
        sum += i
    return sum


print(sum_multiples(int(input("Get the sum of multiples of 3 and 5 up to: "))))
