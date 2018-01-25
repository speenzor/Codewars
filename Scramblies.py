#Codewars Challenge: Scramblies
#This function returns true if a portion of s1 characters can be rearranged to match s2,
#otherwise it returns False.

#This way works fast enough for Codewars but was still not as fast as it could be, I suspect:
def scramble(s1, s2):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in alphabet:
        if s2.count(i) <= s1.count(i):
            continue
        else:
            return False
    return True


#This is the super slow way that works but is too slow for Codewars and for very long strings:
def scramble2(s1,s2):
    s1_list = list(s1)
    match_list = []
    for i in s2:
        if i in s1_list:
            match_list.append(i)
            s1_list.remove(i)
    new_match_list = ''.join(match_list)
    if new_match_list == s2:
        return True
    else:
        return False


#This way works and is fast except it doesn't work for double letters
def scramble3(s1,s2):
    s2_list = list(s2)
    filtered_list = filter(lambda x: x in s1, s2_list)
    new_match_string = ''.join(filtered_list)
    if new_match_string == s2:
        print True
    else:
        print False
