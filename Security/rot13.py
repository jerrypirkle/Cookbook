#!/usr/bin/env python
# # -*- coding: utf-8 -*-
"""
Function that implements ROT13, a simple letter substitution cipher that replaces a 
letter with the 13th letter after it WITHOUT using built-in encode/decode from string module. 
This is a special case of the Caesar cipher which was developed in ancient Rome.
Author: Jerry Pirkle
Date Created: 3/25/18
Python Version: 3.6.4
"""
def rot13(message):
    """
    Input: String in ROT13 format
    Return: plaintext string
    :param message:
    :return:
    """
    def decode(c):
        if 'a' <= c <= 'z':
            base = 'a'
        elif 'A' <= c <= 'Z':
            base = 'A'
        else:
            return c
        return chr((ord(c) - ord(base) + 13) % 26 + ord(base))
    return "".join(decode(c) for c in message)
