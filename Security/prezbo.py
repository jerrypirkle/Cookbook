#!/usr/bin/env python
# # -*- coding: utf-8 -*-
"""
The Barksdale Code is a simple transposition cipher that was used in the TV show The Wire.
Rules: 'Jump to the other side of the 5 on the keypad, and swap 5's and 0's.'
See: https://www.youtube.com/watch?v=DQBlq45c1T4

Author: Jerry Pirkle
Date Created: 4/17/18
Python Version: 3.6.4
"""

def decode(encodedNum):
    """
    Input: unformatted phone number as a text string
    Return: encoded / decoded plaintext string
    """
    trans = {
    "1":"9", "2":"8", "3":"7",
    "4":"6", "5":"0", "6":"4",
    "7":"3", "8":"2", "9":"1",
    "0":"5"}
    prezbod  = ""
    for i in encodedNum:
        prezbod += trans[i]
    return prezbod
