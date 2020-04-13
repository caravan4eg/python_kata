# capitalize

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.


def solve(s):
    for x in s.split():
       s = s.replace(x, x.capitalize())
    return s


print(solve('alex  piter 4ivanov'))
print('132 456 Wq  M E' == '132 456 Wq  M E')
