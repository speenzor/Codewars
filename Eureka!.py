#This function finds the number in a range (inclusive) whose digits, when raise to their sequential order and summed will equal the number.
#For example 89 = 8^1 + 8^2, 135 = 1^1 + 3^2 + 5^3
def sum_dig_pow(a,b):
    answerlist = []
    for i in range(a,b+1):
        string = str(i)
        digitlist = []
        for x in range(len(string)):
            digitlist.append(int(string[x])**(x+1))
        if sum(digitlist) == i:
            answerlist.append(i)
    return (answerlist)
