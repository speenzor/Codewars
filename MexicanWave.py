#Codewars Challenge - Mexican Wave
#This function will make the lowercase input string do a 'wave' of campital
#letters int he word. It will return a list of words, the first one with the
#first letter capitalized and then each subsequent letter capitalized in the
#next item in the list.

def wave(string):
    output = []
    for i in range(len(string)):
        if string[i] != ' ':
            output.append(string[:i]+string[i].upper()+string[i+1:])
        else:
            continue
    return(output)
