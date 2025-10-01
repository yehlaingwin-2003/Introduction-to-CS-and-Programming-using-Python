# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 16:58:39 2025

@author: zkkkkk
"""

# def is_even(i): 
#     """
#     """
#     return i%2 == 0


###############################################################################
# YOU TRY IT !! 1st
###############################################################################
# def div_by(n, d):
#     """ n and d are ints > 0 
#         Returns True if d divideds n evenly and False otherwise"""
#     return n%d == 0
# print(div_by(10, 3))
# print(div_by(195, 13))


###############################################################################
# YOU TRY IT !! 2nd
###############################################################################
# def sum_odd(a,b):
#     sum = 0
#     for i in range (a,b+1):
#         if not is_even(i):
#             sum += i
#     return sum
# print(sum_odd(2,5))


###############################################################################
# YOU TRY IT !! 3rd
############################################################################### 
# Method 1
# def is_palindrome(s):
#     """ s is a string
#     Returns True is s is a palindrome and Flase otherwise 
#     """
#     lastindex = len(s)-1
#     midpoint = len(s)//2
#     for i in range (midpoint):
#         if s[i] != s[lastindex-i]:
#             return False
#     return True

# print(is_palindrome("ehello"))


# Method 2
# def is_palindrome(s):
#     return s == s[::-1]

# print(is_palindrome("ererdrere"))


