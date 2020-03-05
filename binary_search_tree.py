import re

if __name__ == '__main__':
    s = input()


    if re.search('[A-Za-z0-9]', s): print('True')
    else: print('False')

    if re.search('[A-Za-z]', s): print('True')
    else: print('False')

    if re.search('[0-9]', s): print('True')
    else: print('False')

    if re.search('[a-z]', s): print('True')
    else: print('False')

    if re.search('[A-Z]', s): print('True')
    else: print('False')




'''
In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
In the second line, print True if  has any alphabetical characters. Otherwise, print False.
In the third line, print True if  has any digits. Otherwise, print False.
In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
'''
