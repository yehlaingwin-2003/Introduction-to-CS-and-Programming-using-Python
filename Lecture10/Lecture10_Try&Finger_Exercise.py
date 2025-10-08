# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 08:49:23 2025

@author: zkkkkk
"""

###############################################################################
## YOU TRY IT!
###############################################################################


# (1) Write a function that meets the following speciicaion:
    
def make_ordered_list(n):
    """ n is a positive int
    Returns a list containing all ints in order from 0 to n (inclusive).
    """
    
    ordered_list = []
    
    for i in range (n+1):
        ordered_list.append(i)
        
    return ordered_list

print(make_ordered_list(6))
        

###############################################################################


## (2) Write a function that meets the specification

def remove_elem(L, e):
    """
    L is a list
    Returns a new list with elements in the same order as L 
    but without any elements equal to e.
    """
    new_list = []
    for item in L:
        if item != e:
            new_list.append(item)
        
    return new_list;

  
L = [1,2,2,2]
print(remove_elem(L, 2))    # prints [1]
# L = [1,2,2,2]
# print(remove_elem(L, 1))    # prints [2,2,2]
# L = [1,2,2,2]
# print(remove_elem(L, 0))    # prints [1,2,2,2]


###############################################################################



## (3) Write a function that meets this specification

def count_words(sen):
    """ sen is a string representing a sentence 
    Returns how many words are in sen (i.e. a word is a 
    a sequence of characters between spaces. """
    # your code here+
    
    words_list = sen.split(" ")
    return len(words_list)

s = "Hello it's me"
print(count_words(s))   # prints 3

# s = "I just took a DNA test turns out I'm 100% splitting strings"
# print(count_words(s))   # prints 12


###############################################################################



## (4) Write a function that meets these specs:
    
def sort_words(sen):
    """ sen is a string representing a sentence 
    Returns a list containing all the words in sen but
    sorted in alphabetical order. """
    
    new_list = sen.split(" ")
    new_list.sort()
    return new_list
    

s = "look at this photograph"
print(sort_words(s))    # prints ['at', 'look', 'photograph', 'this']

# s = "now this is a story all about how my life got flipped turned upside down"
# print(sort_words(s))



###############################################################################


## (5) Iteration

##  Option 1: Make a new variable representing the index, initialized to 0
## before the loop and incremented by 1 in the loop.

def square_list(L):
    i = 0
    for elem in L:
        L[i] = elem**2
        i += 1
    return L



# Option 2: Loop over the index not the element, and use L[index] to get
# the element

def square_list(L):
    for i in range(len(L)):
        L[i] = L[i]**2
    return L




# Option 3: Use enumerate in the for loop (I leave this option to you to
# look up). i.e. for i,e in enumerate(L)

def square_list(L):
    for index, item in enumerate(L):
        L[index] = item**2
    return L


L = [1,2,3]
print(square_list(L)) 
       
        
    
## Option 2 and 3 are recommended and the best
## Never use option 1 for iteration over a list if we want to mutate the list


###############################################################################
## Finger Exercise
###############################################################################

def all_true(n, Lf):
    """ n is an int
        Lf is a list of functions that take in an int and return a Boolean
    Returns True if each and every function in Lf returns True when called 
    with n as a parameter. Otherwise returns False. 
    """
    # Your code here
    new_list = []
    for i in range(len(Lf)):
        new_list.append(Lf[i](n))
        
    if False in new_list:
        return False
    else: 
        return True
        
        
    

def is_even(n):
    if (n % 2) == 0:
        return True
    else:
        return False
    
def is_greater_than_one(n):
    if n > 1:
        return True
    else: 
        return False
    
def is_an_integer(n):
    if type(n) == "Number":
        return True
    else: 
        return False
    

# Examples:    
print(all_true(6, [is_even, is_greater_than_one])) # prints 6
    
    
    
    
    
    
    
    
    
    