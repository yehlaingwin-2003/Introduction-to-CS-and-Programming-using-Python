# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 11:01:12 2025

@author: zkkkkk
"""

###############################################################################
## YOU TRY IT!
###############################################################################

## (1) Write a function that meets these specs:
    
vowels = "aeiou"
def char_counts(s):
    """ s is a string of lowercase chars
    Return a tuple where the first element is the
    number of vowels in s and the second element
    is the number of consonants in s """
    (num_of_vowels, num_of_consonants) = (0, 0)
    for char in s:
        if char in vowels:
            num_of_vowels += 1
        else: 
            num_of_consonants += 1
    
    return (num_of_vowels, num_of_consonants)

print(char_counts('aeiou'))



## (2) Write a function that meets these specs in docstring

def sum_and_prod(L):
    """ L is a list of numbers
    Return a tuple where the first value is the
    sum of all elements in L and the second value
    is the product of all elements in L """
    
    (total_sum, total_product) = (0, 1)
    
    for i in L:
        total_sum += i
        total_product *= i
        
    return (total_sum, total_product)

print(sum_and_prod([1,2,3,4]))



###############################################################################
## FINGER EXERCISE 
###############################################################################

def dot_product(tA, tB):
    """
    tA: a tuple of numbers
    tB: a tuple of numbers of the same length as tA
    Assumes tA and tB are the same length.
    Returns a tuple where the:
    * first element is the length of one of the tuples
    * second element is the sum of the pairwise products of tA and tB
    """
    # Your code here
    first_element = len(tA)
    second_element = 0
    for i in range(len(tA)):
        second_element += tA[i] * tB[i]
        
    return (first_element, second_element)

# Examples:
tA = (1, 2, 3)
tB = (4, 5, 6)   
print(dot_product(tA, tB)) # prints (3,32)

