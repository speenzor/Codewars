#Codewars Challenge: Who likes it?
#Given a list of names it will display who is in the list.
def likes(names):
    #If no names
    if len(names) == 0:
        return ('no one likes this')
    #If one name
    elif len(names) == 1:
        return (names[0]+ ' likes this')
    #If 2 names
    elif len(names) == 2:
        return (names[0]+' and '+names[1]+' like this')
    #If 3 names
    elif len(names) == 3:
        return(names[0]+', '+names[1]+' and '+names[2]+' like this')
    #If 4 or more names
    elif len(names) > 3:
        return(names[0]+', '+names[1]+' and '+str(len(names)-2)+' others like this')
