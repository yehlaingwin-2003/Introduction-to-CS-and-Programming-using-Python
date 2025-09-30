# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 19:57:05 2025

@author: zkkkkk
"""

# mysum = 0
# for i in range(5, 11, 2):
#     mysum += i
#     if mysum == 5:
#         break
#         mysum += 1
        
# print(mysum)

# counter = 0
# for i in range(5,6):
#     if(i%2 == 0):
#         counter += 1
        
# print(counter)
    


# s = "demo loops - fruit loops"

# for char in s:
#     if(char == 'i' or char == 'u'):
#         print("There is a i or u")

# for char in s: 
#     if char in 'iu':
#         print("ther is a i or u")


# you try it 1st 

# s = 'abca'
# filtered_word = ''
# count_unique = 0

# for char in s: 
#     if char not in filtered_word:
#         filtered_word += char
#         count_unique += 1
# print(filtered_word)
# print(count_unique)


# guess = 0
# x = int(input("Enter a number and i will guess the perfect square of it: "))

# neg_flag = False
# if x < 0:
#     neg_flag = True

# while guess**2 < x:
#     guess += 1

# if guess**2 == x:
#     print(f"The perfect square of {x} is {guess}.")
# elif guess**2 > x:
#     print(f"There is no perfect square for {x}.")
#     if neg_flag:
#         print(f"Just checking....... did you mean {-x}?")


# you try 2nd 

# num1 =12
# found = False
# for i in range(1, 10):
#     if i == num1:
#         print(f"The secret number is {i} and it is in the range.")
#         found = True
#         break

# if not found: 
#     print(f"it did not find it")


# for a in range(1001):
#     b = max(a - 20,0)
#     c = a * 2
#     if(a+b+c == 1000):
#         print(f"Alyssa sold {a} tickets")
#         print(f"Ben sold {b} tickets")
#         print(f"Cindy sold {c} tickets")

###################################################
# let's calculate the binary of every number

# num = int(input("Enter any number you want to change to binary value: "))
# result = ''
# if num == 0: 
#     result = '0'
# while num > 0:
#     result = str(num%2) + result 
#     num = num//2
    
# print(result)

#######################################################
# if negative value is given

# num = int(input("Enter any number you want to change to binary value: "))
# result = ''
# is_neg = False

# if num < 0: 
#     is_neg = True
#     num = abs(num)

# if num == 0: 
#     result = '0'
    

# while num > 0:
#     result = str(num%2) + result 
#     num = num//2
    
# if is_neg:
#     result = '-'+ result
# print(result)



##########################################################
# Finger Exercise #
# Assume you are given a positive integer variable named N. 
# Write a piece of Python code that finds the cube root of N. 
# The code prints the cube root if N is a perfect cube or it prints error
# if N is not a perfect cube. Hint: use a loop that increments a counter—you decide when the counter should stop.


# N = -27
# x = 0
# is_neg = False
# if N < 0:
#     is_neg = True
#     N = abs(N)

# while x**3 < N:
#     x += 1
# if x**3 == N:
#     if is_neg:
#         print(f"The perfect cube of {N} is {x} but did you mean -{N}")
#     else:    
#         print(f"The perfect cube of N is {x}")
# else:
#     print("Error")