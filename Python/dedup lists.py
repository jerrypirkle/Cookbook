#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 09:17:05 2018

@author: jpirkle
"""

charset = "redacted"
others = "redacted"
dedup = ""

for i in charset:
    if i not in dedup:
        dedup += i

dedup += dedup.upper() + others
print(dedup)
