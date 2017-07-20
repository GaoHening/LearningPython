from functools import reduce
import functools
# reduce()函数已经被从全局名字空间里移除了，它现在被放置在fucntools模块里
# 用的话要 先引入from functools import reduce


def add(x, y, f):
    return f(x) + f(y)
print(add(-5, -4, abs))

L = [1, 2, 3, 4, 5, 6]
print(list(map(int, '12345')))


def f(x):
    return x*x
print(list(map(f, L)))


def fn(x, y):
    return x*10 + y
print(reduce(fn, L))


def str2int(s):
    def fn1(x, y):
        return x * 10 + y
# 将字符串中的一个字符作为索引条件，转换成对应的数字

    def char2num(s1):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s1]
    return reduce(fn1, map(char2num, s))
print(str2int('12345'))


def normalize(name):
    return name.title()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def mul(x, y):
    return x*y


def prod(mulgroup):
    return reduce(mul, mulgroup)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

flag = 0


def str2float(s):

    def fn1(x, y):
        global flag
        if flag == 0:
            if y < 10:
                return x * 10 + y
            elif y == 10:
                flag = flag + 1
                return x
        else:
            print(10 ** flag)
            x = x + (y / (10 ** flag))
            flag = flag + 1
            return x

    def char2num(s1):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': 10}[s1]
    return reduce(fn1, map(char2num, s))
print(str2float('123.45'))


def is_odd(x):
    return x % 2 == 1
print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

now = 2


def main():

    for n in primes():
        if n < 100:
            print(n)
        else:
            break


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(x):
    global now
    return x % now > 0


def primes():
    global now
    yield 2
    it = _odd_iter()
    while True:
        now = next(it)
        yield now
        it = filter(_not_divisible, it)

if __name__ == '__main__':
    main()

print(list(filter((lambda n: str(n) == str(n)[::-1]), range(1, 1000))))
print(L[::-1])

print(sorted([36, 5, -12, 9, -21]))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.upper))
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(x):
    return x[0]


def by_score(x):
    return x[1]

print(sorted(L, key=by_name))
print(sorted(L, key=by_score, reverse=True))


def lazy_sum(args):

    def sum1():
        ax = 0
        for a in args:
            ax = ax + a
        return ax
    return sum1

f = lazy_sum([1, 2, 3, 4])
print(f())
# 函数的闭包

print(list(map(lambda x: x*x, [1, 2, 3, 4])))


def build(x, y):
    return lambda: x*x+y*y
f = build(1, 2)
print(f())


def log(func):
    def wrapper(*args, **kw):
        print('begin call %s():' % func.__name__)
        func(*args, **kw)
        print('end call %s():' % func.__name__)
        return
    return wrapper


@log
def now():
    print('2015-3-25')
now()


newmax = functools.partial(max, 10)
print(newmax(1, 2, 3))

int2 = functools.partial(int, base=2)
print(int2('101'))

