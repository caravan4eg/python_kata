#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
total_swaps = 0
for i in range(n):
    # Track number of elements swapped during a single array traversal
    numberOfSwaps = 0

    for j in range(n-1):
        # Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]):
            a[j], a[j + 1] = a[j + 1], a[j]
            numberOfSwaps += 1
            total_swaps += 1
            print(total_swaps)


    # If no elements were swapped during a traversal, array is sorted
    if numberOfSwaps == 0:
        break
print('Array is sorted in ' + str(total_swaps) + ' swaps.')
print('First Element: ', a[0])
print('Last Element: ', a[-1])
