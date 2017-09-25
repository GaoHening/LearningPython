from enum import Enum, unique


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


class Animal(object):
    pass


class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class Runable(object):
    def run(self):
        print("runing")


class Dog(Mammal, Runable):
    pass

d = Dog()
d.run()


class NewStudent(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'name is ' + self.name

    def __repr__(self):
        return self.name

print(NewStudent('Gao'))
a = NewStudent('GAO')
print(a)


class Fib(object):
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        temp = self.a + self.b
        self.a = self.b
        self.b = temp
        if self.a > 100:
            raise StopIteration()
        return self.a

    def __getitem__(self, n):
        tmpa, tmpb = 1, 1
        for i in range(n):
            tmpa, tmpb = tmpb, tmpa + tmpa
        return tmpa

fib = Fib()
for num in fib:
    print(num)
print(fib[3])


class Chain(object):
    def __init__(self, path=''):
        self.path = path

    def __getattr__(self, path):
        return Chain(self.path + '/' + path)

    def __str__(self):
        return self.path

    def __call__(self, *args, **kwargs):
        print('text')

print(Chain().staues.da.dsad.dsad.cxfg)
text = Chain()
text()


@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

for name, member in Weekday.__members__.items():
    print(str(name) + '=>' + str(member))
