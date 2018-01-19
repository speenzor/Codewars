#Codewars Challenge: String average
#Takes a string og number between 0-9 and returns the average of these
#numbers in the largest integer less than the average written out as
#a string.
def average_string(s):
    numbers = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,
               'seven':7,'eight':8,'nine':9}
    numbers2 = {0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',
                6:'six',7:'seven',8:'eight',9:'nine'}
    inputs = s.split()
    summation = 0
    for i in inputs:
        if i not in numbers:
            return 'n/a'
        elif inputs == []:
            return 'n/a'
        else:
            summation += numbers[i]
    if len(inputs) == 0:
        return 'n/a'
    else:
        average = summation/len(inputs)
        return numbers2[int(average)]
