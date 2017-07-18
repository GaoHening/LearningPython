import math
print(abs(-100))
n1 = 255
n2 = 1000
print(hex(n1), hex(n2))


def move(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x1, y1 = move(100, 100, 60, math.pi/6)
print(x1, y1)


def quadratic(a, b, c):
    r1 = (b*(-1)+math.sqrt(b*b-4*a*c))/(2*a)
    r2 = (b*(-1)-math.sqrt(b*b-4*a*c))/(2*a)
    return r1, r2
print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))


def add_end(l=None):
    if l is None:
        l = []
    l.append("End")
    return l
print(add_end())
print(add_end(["haha"]))


def calc(*number):
    sum1 = 0
    for n in number:
        sum1 = sum1+n*n
    return sum1

print(calc(1, 2, 3))
text = [1, 2, 3]
print(calc(*text))


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
    return

person('Bob', 35, city='Beijing')
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)

#*args是可变参数，args接收的是一个tuple；

#**kw是关键字参数，kw接收的是一个dict。

#以及调用函数时如何传入可变参数和关键字参数的语法：

#可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

#关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

#使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

#命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

#定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。