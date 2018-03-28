#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""
Takes Aardvark json data and prints out a list of users who have expired (user-defined) or unused credentials.
Projct: https://github.com/Netflix-Skunkworks/aardvark
Input: Aardvark json data, run on cron
Output: Non-compliant accounts
Author: Jerry Pirkle
Date Created: 3/27/18
Python Version: 2.7.13s

Planned Improvements:
* Write results to DB
"""

from __future__ import print_function
import time
import json

# Constant: Seconds in a day
seconds = 86400

# Variable: Notify if an account has not been used in x days
days = 30

# Get today's date in Unix epoch format
# Time is returned in ms, so multiply by 1000 to get seconds
epoch_time = int(time.time()) * 1000

# Any number under the defined limit will be reported
limit = epoch_time - seconds * days

# Load json data into a variable
data = json.load(open('export.json'))

# Get list of users
users = []
for i in data:
    if 'user' in i:
        users.append(str(i))

# Number of user roles
print("".ljust(100,":"))
print(("Users, Number of Roles Assigned").ljust(100,":"))
print("".ljust(100,":") + '\n')
for i in users:
    print("* " + i.split("/")[1], end=': ')
    print(len(data[i]))

# Permissions that have been used, but are expired
print('\n' + "".ljust(100,":"))
print(("Expired Permissions (have not ben used in %s days):" % days).ljust(100,":"))
print("".ljust(100,":"))
print("These accounts may currently have too much access and should be audited")
for i in users:
    print('\n' + (i.split("/")[1]).ljust(100,"-") + '\n')
    for j in range(len(data[i]) - 1):
        if data[i][j]["lastAuthenticated"] > 0 and data[i][j]["lastAuthenticated"] < limit:
            print('* ' + data[i][j]["serviceNamespace"], "Last Used:", time.strftime("%a %d %b %Y %H:%M:%S GMT", time.gmtime(data[i][j]["lastAuthenticated"]  / 1000.0)))

# Permissions that have never been used
print('\n' + "".ljust(100,":"))
print(("Permissions that have Never been Used:").ljust(100,":"))
print("".ljust(100,":"))
print("These accounts may have been originially provisioned with too much access.")
for i in users:
    print('\n' + (i.split("/")[1]).ljust(100,"-"))
    for j in range(len(data[i]) - 1):
        if data[i][j]["lastAuthenticated"] == 0:
            print('* ' + data[i][j]["serviceNamespace"])#!/usr/bin/env python
