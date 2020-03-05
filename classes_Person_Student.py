'''
Heraldo Memelli 8135627
2
100 80
'''

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self,firstName,lastName,idNum,scores):
        self.firstName=firstName
        self.lastName=lastName
        self.idNumber=idNum
        self.scores=scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #   Write your function here
    def calculate(self):
        average_grade = sum(self.scores)/len(self.scores)
        if average_grade >= 90: return 'O'
        elif average_grade >= 80: return 'E'
        elif average_grade >= 70: return 'A'
        elif average_grade >= 55: return 'P'
        elif average_grade >= 40: return 'D'
        return 'T'



line = input().split()

firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list(map(int, input().split()))

s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
