#Codewars challenge: Find the unique number
#Finds the unique number in a list. This assumes that there is only one
#unique number in the list.
def find_uniq(arr):
    a, b = set(arr)
    if arr.count(a) == 1:
        return a
    else:
        return b
