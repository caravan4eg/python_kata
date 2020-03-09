"""Task
Consider a database table, Emails, which has the attributes First Name and Email ID. Given  N rows of data simulating the Emails table, print an alphabetically-ordered list of people whose email address ends in @gmail.com.

Sample Input
6
riya riya@gmail.com
julia julia@julia.me
julia sjulia@gmail.com
julia julia@gmail.com
samantha samantha@gmail.com
tanya tanya@gmail.com

Sample Output
julia
julia
riya
samantha
tanya
"""
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    pattern = '@gmail.com'
    gmail_users = []
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        if re.search(pattern, emailID):
            gmail_users.append(firstName)
    print(gmail_users)
    for user in sorted(gmail_users):
        print(user)
