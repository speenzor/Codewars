#Codewars Challange - Find the smallest

#I could not solve this Codewars challenge but this is below is how far I got before giving up.

#This function will take a single integer as input. Then the function will
#find the smallest number it can make by taking a single digit in the input and
#putting it at a new index location. Then it will return a list of three
#things: the smallest number it got, the index of the digit it took, and
#the index where it inserted the digit.

def smallest(n):
    num = str(n)
    new_num = str()
    for i in range(1,len(num)):
        #Find the smallest digit in the string and put it in front
        if num[i] == min(num[1:]):
            for j in range(len(num)):
                if num[i] < num[j]:
                    new_num = num[:j] + num[i] + num[j:i] + num[i+1:]
                    print([int(new_num), i, j])


n = 209917
smallest(n)

#[029917, 0, 1]
#my answer [029917, 1, 0]
