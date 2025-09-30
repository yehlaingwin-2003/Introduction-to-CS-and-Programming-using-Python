# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 22:42:13 2025

@author: zkkkkk
"""

# combining strings / concatenating strings
# b = ":" 
# c= ")"
# s1 = b + 2*c
# print(s1)


# f = "a"
# g = "b" 
# h = "3"
# s2 = (f+g) * int(h)
# print (s2)
# print(len(s2))


# s = "ABC d3f ghi"
# print(s[2]) # c
# print(s[2:9]) # abc
# print(s[-3:-8]) # g f3d c
# print(s[8:1:-1]) # g f3d c

# a = input("Type a number: ")
# print(2 * a)


# YOU TRY IT 

# a = input("Please type a verb: ")
# print("I can "+a+" better than you")
# print((a+" ")*5) # there is extra space at the end of last verb
# print(" ".join([a]*5))



# secret_num = 13
# guess_num = int(input("Guess a number: "))
# print(secret_num == guess_num)


# branching 
# x = int(input("Enter a number for x: "))
# y = int(input("Enter a different number for y: "))
# if x == y:
#     print(x,"is the same as",y)
#     print("These are equal!")


# y = 11
# answer = ''
# x = 11
# if x == y:
#     answer = answer + 'M'
# if x >= y:
#     answer = answer + 'i'
# else:
#     answer = answer + 'T'
# print(answer)


secrect_num = 11
guess_num = int(input("Type a number: "))
if guess_num == secrect_num: 
    print("The same as the secrect")
elif guess_num > secrect_num: 
    print("Too high")
else:
    print("Too Low")
