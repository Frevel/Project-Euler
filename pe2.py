#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 16:16:10 2018

@author: thomas
"""

def fib_sum_even(limit):
    '''
    get the sum of all even fibonacci numbers within the
    boarders of limit.
    
    limit (int) - max size of fibonacci numbers to compute
    returns int
    '''
    a = 1
    b = 2
    c = 0
    ans = 2
    while(True):
        c = a+b
        if c > limit: break
        print(c)
        a = b
        b = c
        if c%2 == 0: ans += c
    return ans
fib_sum_even(4000000)