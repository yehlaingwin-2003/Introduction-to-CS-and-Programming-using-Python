# -*- coding: utf-8 -*-
"""
Created on Sat Oct  4 16:00:47 2025

@author: zkkkkk
"""

###############################################################################
## YOU TRY IT!
###############################################################################

## (1) What is printed if you run this code as a file?

def add(x,y):
    return x+y

def mul(x,y):
    print(x*y)
    
add(1,2)  # Nothing will be printed 
print(add(2,3))  # 5 will be printed
mul(3, 4)  # 12 will be printed 
print(mul(4, 5))  # 20 and None will be printed



## (2) Fix the code that tries to write this function

def is_triangular(n): 
    """ n is an int > 0
    Returns True if n is triangular, i.e. equals a continued
    summation of natural numbers (1+2+3+...+k), False otherwise """
       
    total = 0
    for i in range(n+1):
        total += i
        if total == n:
            return True  # change print to return
        
    return False  # change print to return
         
print(is_triangular(3))


## (3) Write a function that satisfies the following specs
## def count_nums_with_sqrt_close_to (n, epsilon):
##       """ n is an int > 2
##      epsilon is a positive number < 1
##      Returns how many integers have a square root within epsilon of n """
## Use bisection_root we already wrote to get an approximation
## for the sqrt of an integer.
## For example: print(count_nums_with_sqrt_close_to(10, 0.1))
## prints 4 because all these integers have a sqrt within 0.1
##  sqrt of 99 is 9.949699401855469
##  sqrt of 100 is 9.999847412109375
##  sqrt of 101 is 10.049758911132812
##  sqrt of 102 is 10.099456787109375

def bisection_root(x):
    """
    x is an integer and the function will find the square root of x"""
    epsilon = 0.01
    low = 0
    high = x
    ans = (high + low)/2.0
    while abs(ans**2 - x) >= epsilon:
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
    return ans


def count_nums_with_sqrt_close_to (n, epsilon):
    """ n is an int > 2
    epsilon is a positive number < 1
    Returns how many integers have a square root within epsilon of n """
    count = 0
    for i in range(n**3):
        square_root = bisection_root(i)
        if abs(square_root-n) < epsilon:
            count += 1
            print(i, square_root)
    return count
    
print(count_nums_with_sqrt_close_to(10, 0.1))
    

## (4) Do a similar trace with the function call

def calc (op, x, y):
    return op(x,y)

def div(a, b):
    if b != 0:
        return a/b
    print("Denon was 0.")
    
res = calc(div, 2, 0)
print(res)



## (5) Write a function that meets these specs in doc stings

def apply(criteria,n):
    """
    * criteria is a func that takes in a number and returns a bool
    * n is an int
    Returns how many ints from 0 to n (inclusive) match
    the criteria (i.e. return True when run with criteria)
    """
    num_of_int = 0
    for i in range(n+1):
        if criteria(i):
            num_of_int += 1
    return num_of_int


def is_odd (x):
    if x%2 != 0:
        return True
    return False

print(apply(is_odd, 5))

###############################################################################
## FINGER EXERCISE
###############################################################################

def same_chars(s1, s2):
    """
    s1 and s2 are strings
    Returns boolean True is a character in s1 is also in s2, and vice 
    versa. If a character only exists in one of s1 or s2, returns False.
    """
    # Your code here
    combined_s = s1+s2
    for char in combined_s:
        if not (char in s1 and char in s2):
            return False
    return True 


# Examples:
print(same_chars("abc", "cab"))     # prints True
print(same_chars("abccc", "caaab")) # prints True
print(same_chars("abcd", "cabaa"))  # prints False
print(same_chars("abcabc", "cabz")) # prints False