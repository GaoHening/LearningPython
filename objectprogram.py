class Student(object):
    def __init__(self, name, grade):
        self.__name = name
        self.__grade = grade

    def printgrade(self):
        print(self.__name + "'s grade is " + str(self.__grade))

    def setgrade(self, grade):
        self.__grade = grade

Gao = Student("Gao", 95)
Gao.printgrade()
Gao.setgrade(80)
Gao.printgrade()