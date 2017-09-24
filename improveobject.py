class Student(object):
    __slots__ = ('name', 'age')
    pass


def set_age(self, age):
    self.age = age


Student.setage = set_age
a = Student()
a.setage(25)
print(a.age)
a.name = 'hehe'

