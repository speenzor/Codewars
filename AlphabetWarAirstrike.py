#! /usr/bin/env python3

"""
Codewars Challenge - Alphabet War, Airstrike (6 kyu)

This function takes a string of letters and * symbols as inputs. 8 selected
letters (shown below in two dictionaries) have score values for either Left or
Right. Each * character in the string represents a bomb dropped on the letters
in the string and will eliminate the characters adjacent to the bomb character.
The remaining letters with score values for Left or Right then fight. The
function returns the winner if there is one and returns another message if there
was no winner.
"""

def alphabet_war(fight):
    left_side = {'w':4,'p':3,'b':2,'s':1}
    right_side = {'m':4,'q':3,'d':2,'z':1}
    fight_list = list(fight)
    left_score = 0
    right_score = 0
    for i in range(len(fight_list)-1):
        print(fight_list)
        print(i)
        if fight_list[i] == '*':
            if fight_list[i-1] != '*' and i > 0:
                fight_list[i-1] = 0
            if fight_list[i+1] != '*' and i < (len(fight_list)):
                fight_list[i+1] = 0
            fight_list[i] = 0
    for i in fight_list:
        if i in right_side:
            right_score += right_side[i]
        if i in left_side:
            left_score += left_side[i]
    if right_score > left_score:
        print ("Right side wins!")
    elif left_score > right_score:
        print ("Left side wins!")
    else:
        print ("Let's fight again!")


fight = '***m*wzbsd*dz*sd*'
alphabet_war(fight)
