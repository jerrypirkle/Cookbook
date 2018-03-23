#!/usr/bin/env python
# # -*- coding: utf-8 -*-
"""
Function to determine credit card provider.
Author: Jerry Pirkle
Date Created: 3/23/18
Python Version: 3.6.4
"""

def get_cc_issuer(number):
	"""
	Input: CC number, integers only
	Returns: CC issuer
	"""
	if len(str(number)) == 15 and str(number)[0] == '3' and str(number)[1] in '47':
		return 'AMEX'
	elif len(str(number)) == 16 and str(number)[0:4] == '6011':
		return 'Discover'
	elif len(str(number)) == 16 and str(number)[0] == '5' and str(number)[1] in '12345':
		return 'Mastercard'
	elif (len(str(number)) == 13 or len(str(number)) == 16) and str(number)[0] == '4':
		return 'VISA'
	else:
		return 'Unknown'
