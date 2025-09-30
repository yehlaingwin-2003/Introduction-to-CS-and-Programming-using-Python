# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 12:10:17 2025

@author: zkkkkk
"""

# x = 0.375
# p = 0

# while (2**p * x)%1 != 0:
#     p += 1 
    
# num = int(2**p * x)
# result = ''
# if num == 0:
#     result = '0'
# while num > 0: 
#     result = str(num%2) + result
#     num = num//2
    
# if p-len(result) > 0:
#     for i in range(p - len(result)):
#         result = '0'+result
# print(result[0:-p])
# print(result[-1:-p])
# result = result[0:-p] + '.' + result[-1:-p-1:-1]
    
# print (result)


##########################################
## Approximation Algorithim Method 
##########################################
number = 54321

epsilon = 0.001

increment = 0.00001

number_of_guesses = 0

guess = 0 

while abs(guess**2 - number) > epsilon and guess**2 <= number:
    guess += increment
    number_of_guesses += 1
    
if guess**2 > number: 
    print("Failed on find the suqare root of "+str(number))
else:
    print(guess)
    print(f"The nearest square root of {number} is {guess} becuase guess square is {guess**2}")
    print(f"number of guesses is {number_of_guesses}")
    
