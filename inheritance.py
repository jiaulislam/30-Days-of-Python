class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber

	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)


class Student(Person):
    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self,firstName,lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores
        self.LETTER = ['O', 'E', 'A', 'P', 'D', 'T']
  

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        a = sum(self.scores) // len(self.scores)
        if a >= 90 and a <= 100:
            return self.LETTER[0]
        elif a >= 80 and a < 90:
            return self.LETTER[1]
        elif a >= 70 and a < 80:
            return self.LETTER[2]
        elif a >= 55 and a < 70:
            return self.LETTER[3]
        elif a >= 40 and a < 55:
            return self.LETTER[4]
        else:
            return self.LETTER[5]


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
