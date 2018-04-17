#!/usr/bin/env python
# # -*- coding: utf-8 -*-
"""
Function that counts the character frequency on a website. Used to perform frequency analysis on a target's writing.
Author: Jerry Pirkle
Date Created: 4/17/18
Python Version: 3.6.4
"""

from collections import Counter
from urllib.request import urlopen


target_url = r"https://raw.githubusercontent.com/teropa/nlp/master/resources/corpora/gutenberg/shakespeare-caesar.txt"
data = urlopen(target_url)


def webFreq(input):
    """
    :param input: text from a web page.
    :return: dictionary key=ASCII character (case-sensitive) : value=frequency of character occurrence
    """
    count = Counter()
    for line in data:
        count += Counter(line)
    return count


def percentFreq(input):
    """
    :param input: webFreq dictionary
    :return: dictionary key=ASCII character : value=percentage of frequency occurrence to all other characters
    """
    percentDict = Counter()
    total = sum(input.values())
    #part / total * 100 ... iterate for part
    for key in input:
        percentDict[key] = float('%.3f' % (input[key] / total * 100))
    return percentDict


def askeyCon(input):
    """
    :param input: dictionary with ASCII values as keys
    :return: dictionary with text values as keys
    """
    converted = {}
    try:
        for key in input:
            input[chr(int(key))] = input.pop(key)
    except:
        pass
    return input

'''Testing'''
#output = webFreq(data)
#percentages = percentFreq(output)

#print(output)
#print(percentages)
#print(askeyCon(output))
#print(askeyCon(percentages))
