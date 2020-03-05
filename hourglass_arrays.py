'''
Task
Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.

Input Forarr

There are  lines of input, where each line contains  space-separated integers describing 2D Array ; every value in  will be in the inclusive range of  to .

Constraints

Output Forarr

Print the largest (maximum) hourglass sum found in .

Sample Input

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
Sample Output

19
Explanation

 contains the following hourglasses:

(0,0) (0,1) (0,2)   1 1 0   1 0 0   0 0 0
      (1,1)           0       0       0
(2,0) (2,1) (2,2)   1 1 0   1 0 0   0 0 0

0 1 0   1 0 0   0 0 0   0 0 0
  1       1       0       0
0 0 2   0 2 4   2 4 4   4 4 0

1 1 1   1 1 0   1 0 0   0 0 0
  0       2       4       4
0 0 0   0 0 2   0 2 0   2 0 0

0 0 2   0 2 4   2 4 4   4 4 0
  0       0       2       0
0 0 1   0 1 2   1 2 4   2 4 0
The hourglass with the maximum sum () is:

2 4 4
  2
1 2 4
'''

arr = [
    (1, 1, 1, 0, 0, 0),
    (0, 1, 0, 0, 0, 0),
    (1, 1, 1, 0, 0, 0),
    (0, 0, 2, 4, 4, 0),
    (0, 0, 0, 2, 0, 0),
    (0, 0, 1, 2, 4, 0),
]
rows = cols = 6
max_sum = -63
arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

for i in range(rows-2):
    for j in range(cols-2):
        current_sum = (arr[i][j]+arr[i][j+1]+arr[i][j+2])+\
                (arr[i+1][j+1])+\
                (arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
        # print(arr[i][j], 'Summ = ', current_sum, end=' ')
        # print(f'max_sum = {max_sum}, current_sum ={current_sum}')
        max_sum = max(current_sum, max_sum)
print(max_sum)
