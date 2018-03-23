#!/usr/bin/env python
# # -*- coding: utf-8 -*-
"""
Function that implements the Luhn Algorithm, which is used to help validate credit card numbers.
Author: Jerry Pirkle
Date Created: 3/25/18
Python Version: 3.6.4
"""
def validate(n):
	"""
	Inputs: cc number, integers only
	Returns: Valid/Invalid in Boolean 
	"""
    digits = [int(x) for x in str(n)]
    for x in xrange(len(digits)-2, -1, -2):
        digits[x] = sum(map(int, str(digits[x] * 2)))
    return sum(digits) % 10 == 0
