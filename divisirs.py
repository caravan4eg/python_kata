n = int(input('Number: '))
div = n
sum = 0

while div > 0:
    if n % div == 0:
        sum += div
    div -= 1

print(sum)
