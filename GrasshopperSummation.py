#Codewars Challenge: Grasshopper- Summation
#This sums every number between 1 and the number num.
def summation(num):
    total = 0
    for i in range(1,num+1):
        total = total + i
    return (total)
