actually_dmy = input().split()
expected_dmy = input().split()

# day late
if (int(actually_dmy[0]) > int(expected_dmy[0])) and (int(actually_dmy[1]) == int(expected_dmy[1])):
    day_late = int(actually_dmy[0]) - int(expected_dmy[0])

else: day_late = 0

# month late
if int(actually_dmy[1]) > int(expected_dmy[1]) and int(actually_dmy[2]) == int(expected_dmy[2]):
    month_late = int(actually_dmy[1]) - int(expected_dmy[1])
else: month_late = 0
# year late
if int(actually_dmy[2]) > int(expected_dmy[2]):
    year_late = 1
else: year_late = 0

fine = year_late * 10000 + month_late * 500 + day_late * 15
print(actually_dmy)
print(expected_dmy)
print(fine)
f'fkfjkjf\n'
