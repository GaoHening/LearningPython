class Student(object):
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def printgrade(self):
        print(self.name + "'s grade is " + str(self.grade))

Gao = Student("Gao", 95)
Gao.printgrade()
