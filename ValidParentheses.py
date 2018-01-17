#Codewars Challenge- Valid Parentheses
#Takes a string of parentheses and determines if the order of the parentheses is
#valid. Returns True if valid, False if invalid.

def valid_parentheses(string):
    open_count = 0
    close_count = 0
    count = 0
    for i in range(len(string)):
        if string[i]=='(':
            open_count += 1
            count += 1
        elif string[i]==')':
            close_count += 1
            count -= 1
            if count < 0:
                return False
    if open_count == close_count:
        return True
    else:
        return False
