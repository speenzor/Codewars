'''
This is the solution, in Python, to the Codewars Challenge: Memoized Fibonacci
This function takes in the nth Fibonacci number and returns that number in the
Fibonacci sequence. I specifically saught out this challenge in order to learn 
about recursion and memoization.
'''

def fibonacci(n, cache={}):
    if n in cache:
        value = cache[n]
    elif n <= 2:
        value = 1
        cache[n] = value
    else:
        value = fibonacci(n-2) + fibonacci(n-1)
        cache[n] = value
    return value
