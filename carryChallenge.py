#! /usr/bin/env python3

"""
This is a practice problem I saw in a YouTube video. Create a function that
takes an input array, which represents a real integer, then add one to the
integer and represent it as an array. See examples of input/output below:

[1,3,4] -> [1,3,5]
[1,9,9] -> [2,0,0]
[9,9,9] -> [1,0,0,0]
"""

def add_one(given_array):
    carry = 1
    result = [0]*(len(given_array))
    for i in range(len(given_array)-1,-1,-1):
        total = given_array[i] + carry
        if total == 10:
            carry = 1
        else:
            carry = 0
            result[i] = total % 10
    if carry == 1:
        result = [0]*(len(given_array)+1)
        result[0] = 1
    return (result)
