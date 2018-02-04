#Codewars Challange - Longest Palindrome
#This script finds the longest palindrome in a given string and returns its length
def longest_palindrome (s):
    if len(s) == 0:
        return (0)
    elif len(s) == 1:
        return (1)
    elif len(s) == 2:
        return (2)
    else:
        all_palindromes = []
        longest_length = int()
        for x in range(len(s)+1):
            for i in range(len(s)):
                string = s[i:i+x]
                #Check if it is a palindrome
                if string == string[::-1]:
                    all_palindromes.append(string)
    #Return the length of the longest palindrome in all_palindromes
    for i in range(len(all_palindromes)):
        if len(all_palindromes[i]) > len(all_palindromes[i-1]):
            longest_length = len(all_palindromes[i])
    return (longest_length)
