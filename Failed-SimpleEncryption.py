#! /usr/bin/env python3

#I failed this kata. Below is how far I got before giving up and looking up the answer.

"""Codewars Challenge - Simple Encryption #1 - Alternating Split
by Spencer on 02/11/2018
This script builds an encrypted string by taking every 2nd character from
the string, then the other characters that are not every 2nd character, and
concatenates them as a new string. It does this n times."""

def encrypt(text, n):
    new_list = []
    t = 0
    while t != n:
        for i in range(1,len(text),2):
            new_list.append(text[i])
        for i in range(0,len(text),2):
            new_list.append(text[i])
        new_string = ''.join(new_list)
        print(new_string)
        t += 1


text = 'This is a test!'
n = 1
encrypt(text, 2)
