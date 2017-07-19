from functools import reduce
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
