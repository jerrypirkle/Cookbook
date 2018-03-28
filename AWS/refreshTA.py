#!/usr/bin/env python
# # -*- coding: utf-8 -*-
"""
Refreshes Trusted Advisor on a single account
Author: Jerry Pirkle
Date Created: 3/6/18
Python Version: 3.6.4
Requirements: Boto3 configured with saved crednetials
Account Permissions: "trustedadvisor:*", "support:*"
"""

from __future__ import print_function
import boto3
from botocore.exceptions import ClientError

taChecks = support_client.describe_trusted_advisor_checks(language='en')
for checks in taChecks['checks']:
    try:
        support_client.refresh_trusted_advisor_check(checkId=checks['id'])
        print('Refreshing check: ' + checks['name'])
    except ClientError:
        print('Cannot refresh check: ' + checks['name'])
        continue
