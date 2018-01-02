#Codewars challenge: Find the next perfect square!
#Find the next perfect square given the input of the perfect square as "sq"
#Function will return -1 if the input is not a perfect square.
import math

def find_next_square(sq):
    check = math.sqrt(sq)
    if check - int(check) != 0:
        return (-1)
    output = check + 1.1
    while output -int(output) != 0:
        check += 1
        output = int(check)**2
    return (output)
