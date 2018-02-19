#! /usr/bin/env python3

"""
Codewars Challenge - Steps in Primes

I failed this challenge. This solution below is too slow, checking each iteration in the list
of primes. The correct solution does the same thing as the nested loop I do below but it uses
another function to check if an interated number is a prime number.

This function takes an input g (integer>=2) which indicates the prime-number
step we are looking for, m (integer>=2) which gives the start of the search
(m inclusive), and n (integer>=m) which gives the end of the search
(n inclusive). Then it returns the first pair between m and n with a step equal
to g.
"""

import math

def step(g, m, n):
    initialList = [True] * n
    initialList[0] = False
    initialList[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        pointer = i*2
        while pointer < n:
            initialList[pointer] = False
            pointer = pointer + i
    #Compile the list of primes
    primes = []
    for i in range(n):
        if initialList[i] == True:
            primes.append(i)

    #Create the start number equal to the first prime in our range
    for i in range(len(primes)):
        if primes[i] >= m:
            startPos = i
            break
    
    #Check consecutive then non-consecutive number in the primes list for
    #the step g
    for i in range(startPos, len(primes)):
        for x in range(1, len(primes)-i):
            if primes[i+x]-primes[i] == g:
                return [primes[i],primes[i+x]]
            elif primes[i+x]-primes[i] > g:
                break   #if it starts checking distances that are greater than g, then move to next start position i
        if i == len(primes)-1:
            return []
