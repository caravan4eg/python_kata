"""Sample Input

10
161 182 161 154 176 170 167 171 170 174
Sample Output

169.375"""

def average(array):
    return sum(set(array)) / len(set(array))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
