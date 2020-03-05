students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

# for i in range(int(input())):
#         name = input()
#         score = float(input())
#         students.append([name, score])

def by_score(students):
    return students[1]

def by_name(students):
    return students[0]

sorted_students = sorted(students, key=by_score)
first_min_grade = sorted_students[0][1]
second_min_grade_students = []
for student in sorted_students:
    score = student[1]
    if score > first_min_grade:
        if not second_min_grade_students:
            second_min_grade_students.append(student)
        elif score == second_min_grade_students[0][1]:
            second_min_grade_students.append(student)
for student in (sorted(second_min_grade_students, key=by_name)):
    print(student[0])
