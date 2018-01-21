#Codewars Challenge: Scramblies
#This function returns true if a portion of s1 characters can be rearranged to match s2,
#otherwise it returns False.

#This is the slow way that works but is too slow for Codewars:
def scramble2(s1,s2):
    s1_list = list(s1)
    match_list = []
    for i in s2:
        if i in s1_list:
            match_list.append(i)
            s1_list.remove(i)
    new_match_list = ''.join(match_list)
    if new_match_list == s2:
        return (True)
    else:
        return (False)
        
        
        
        
#This is a faster way that Codewars accepts:
