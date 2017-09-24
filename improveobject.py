class Student(object):
    def __init__(self):
        self.__score = 0

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value


def set_age(self, age):
    self.age = age

Student.setage = set_age
a = Student()
a.setage(25)
print(a.age)
a.score = 99
print(a.score)


class Screen(object):
    def __init__(self):
        self.__width = 0
        self.__height = 0
        self.__resoulution = 0

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def resolution(self):
        self.__resoulution = self.__height * self.__width
        return self.__resoulution

s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
