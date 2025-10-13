# -*- coding: utf-8 -*-
"""
Created on Sat Oct 11 09:55:06 2025

@author: zkkkkk
"""

###############################################################################
## YOU TRY IT!
###############################################################################

## (1) Write a function that meets the specification.
##      Hint. Make a copy to save the elements. The use L.clear() to
##     empty out the list and repopulate it with the ones you’re
##     keeping.
def remove_all(L, e):
    """
    L is a list
    Mutates L to remove all elements in L that are equal to e
    Returns None
    """
    Lcopy = L[:]
    L.clear()
    for elem in Lcopy:
        if elem != e:
            L.append(elem)

L = [1,2,2,2]
remove_all(L, 2)
print(L) # prints [1]


def remove_all(L, e):
    """
    L is a list
    Mutates L to remove all elements in L that are equal to e
    Returns None
    """
    Lcopy = L[:]
    for element in Lcopy:
        if element == e:
            L.remove(e)
            
       
L = [1,2,2,2]
remove_all(L, 2)
print(L) # prints [1]




###############################################################################
## FINGER EXERCISE
###############################################################################

## (1) Implement the function that meets the specifications below:

def remove_and_sort(Lin, k):
    """ Lin is a list of ints
        k is an int >= 0
    Mutates Lin to remove the first k elements in Lin and 
    then sorts the remaining elements in ascending order.
    If you run out of items to remove, Lin is mutated to an empty list.
    Does not return anything.
    """
    # Your code here  
    lin_copy = Lin[:]
    for element in lin_copy:
        if element == k:
            Lin.remove(k)
            
    Lin.sort()

# Examples:
L = [1,6,3]
k = 1
remove_and_sort(L, k)
print(L)   # prints the list [3, 6]




