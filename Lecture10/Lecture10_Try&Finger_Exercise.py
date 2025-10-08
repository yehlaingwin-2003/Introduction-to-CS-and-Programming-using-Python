# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 08:49:23 2025

@author: zkkkkk
"""

###############################################################################
## YOU TRY IT!
###############################################################################


## (1) Write a function that meets the following speciicaion:
    
# def make_ordered_list(n):
#     """ n is a positive int
#     Returns a list containing all ints in order from 0 to n (inclusive).
#     """
    
#     ordered_list = []
    
#     for i in range (n+1):
#         ordered_list.append(i)
        
#     return ordered_list

# print(make_ordered_list(6))
        

###############################################################################


## (2) Write a function that meets the specification

# def remove_elem(L, e):
#     """
#     L is a list
#     Returns a new list with elements in the same order as L 
#     but without any elements equal to e.
#     """
#     new_list = []
#     for item in L:
#         if item != e:
#             new_list.append(item)
        
#     return new_list;

  
# L = [1,2,2,2]
# print(remove_elem(L, 2))    # prints [1]
# L = [1,2,2,2]
# print(remove_elem(L, 1))    # prints [2,2,2]
# L = [1,2,2,2]
# print(remove_elem(L, 0))    # prints [1,2,2,2]


###############################################################################



## (3) Write a function that meets this specification

# def count_words(sen):
#     """ sen is a string representing a sentence 
#     Returns how many words are in sen (i.e. a word is a 
#     a sequence of characters between spaces. """
#     # your code here+
    
#     words_list = sen.split(" ")
#     return len(words_list)

# s = "Hello it's me"
# print(count_words(s))   # prints 3

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
    

# s = "look at this photograph"
# print(sort_words(s))    # prints ['at', 'look', 'photograph', 'this']

# s = "now this is a story all about how my life got flipped turned upside down"
# print(sort_words(s))



###############################################################################