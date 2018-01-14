#Codewars Challenge: Beginner Series #3 Sum of Numbers
#Sums all the numbers between a and b, including a and b. They can be negative
#integers as well and do not have to be ordered.
def get_sum(a,b):
    if a == b:
        return (a)
    elif a < b:
        z = a
        while a < b:
            a += 1
            z += a
        return (z)
    elif b < a:
        z = b
        while b != a:
            b += 1
            z += b
        return (z)
