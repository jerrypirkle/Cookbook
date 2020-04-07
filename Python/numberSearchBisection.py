#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 22:41:56 2018

@author: jpirkle

The program works as follows: you (the user) thinks of an integer between 
0 (inclusive) and 100 (not inclusive). The computer makes guesses, and you 
give it input - is its guess too high or too low? Using bisection search, the 
computer will guess the user's secret number!



Is your secret number 91?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess 
is too low. Enter 'c' to indicate I guessed correctly. y
Sorry, I did not understand your input.
Is your secret number 91?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess 
is too low. Enter 'c' to indicate I guessed correctly. c
"""

x = input("Please think of a number between 0 and 100!")
low = 0       
high = 99
#ans = (high + low)//2
indicate = ''

if x < 0 or x > 99:
    print("That's not between 0 and 100!")
    guess = input("Please think of a number between 0 and 100!")

ans = (high + low)//2
print("Is your secret number " + str(ans) +'?')
while indicate != 'c':
    indicate = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if indicate not in 'hcl':
        print('Sorry, I did not understand your input.')
    
    if indicate == 'l':
        low = ans
    elif indicate == 'h':    
        high = ans
    ans = (high + low)//2
    print("Is your secret number " + str(ans) +'?')

print('Game over. Your secret number was:', end=' ' + str(ans))

def somefunc(x):
    """
    Input: Something
    Output: Something Else:
    """
    return True




