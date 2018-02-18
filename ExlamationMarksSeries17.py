#! /usr/bin/env

"""Codewards Challenge - Exlamation marks series #17: Put the exlamation marks
and question marks to the balace. Are they balanced?

This function will take two strings as input, each with a number of exlamation
points and question marks. Exlamations count as 2 and questions as 3. This
'weighs' each side and returns which side has more weight or if they're
balanced."""

def balance(left, right):
    left_weight = left.count('!')*2 + left.count('?')*3
    right_weight = right.count('!')*2 + right.count('?')*3
    if left_weight > right_weight:
        return 'Left'
    elif right_weight > left_weight:
        return 'Right'
    else:
        return 'Balance'
