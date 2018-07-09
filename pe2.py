#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 16:16:10 2018

@author: Frevel
"""

def fib_sum_even(limit):
    '''
    Returns the sum of all even fibonacci numbers up to limit.
    
    limit (int) : upper limit
    Returns int
    '''
    a = 1  # base case
    b = 2  # base case
    temp_result = 0
    result = 2
    while(a + b <= limit):
        temp_result = a + b
        a = b
        b = temp_result
        if temp_result % 2 == 0:
            result += temp_result
    return result

print(fib_sum_even(int(input("Get the sum of all even fibonacci numbers up to: "))))