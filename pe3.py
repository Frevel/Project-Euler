#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 16:16:10 2018

@author Frevel
"""
 
def get_primes(limit = 1000):
    """
    Computes all primes up to limit. Uses the sieve of Erastothenes.
    
    limit (int) : Upper limit for value of prime number
    Returns list
    """
    numbers = list(range(2, limit + 1))
    for prime in numbers:
        multiple = 2
        while prime * multiple <= limit:
            try:
                numbers.remove(prime * multiple)
            except Exception:
                pass  # Ignore already deleted values
            multiple += 1
    return numbers
        
    
def prime_factors(n, primes):
    """
    Computes the prime factors of n, if all prime factors appear in primes.
    
    n (int) : Number to get prime factors of
    primes (list) : prime numbers
    Returns list
    """
    prime_factors = []
    for factor in primes:
        while n % factor == 0:
            prime_factors.append(factor)
            n = n / factor
    if n > primes[-1]:
        print("Warning: Not enough primes provided!")
        return []
    return prime_factors
    
#print(prime_factors(600851475143, get_primes(10000)))
print(prime_factors(int(input("Compute prime factors for number: ")),
                    get_primes(int(input("Generate primes up to: ")))))