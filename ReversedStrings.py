#Codewars Challenge: Reversed Strings
#Reverses a string
def solution(string):
    newlist = []
    for i in range(len(string)):
        newlist.append(string[len(string)-1-i])
    newstring = ''.join(newlist)
    return (newstring)
