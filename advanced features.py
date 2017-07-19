import os
L = list(range(100))
print(L[:10])
print(L[:10:2])
# print(L)
print("ABCDE"[:2])

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
for value in d.values():
    print(value)
for key, value in d.items():
    print(key, ",", value)

la = [x*x for x in range(10)]
lb = [x*x for x in range(10) if x%2 == 0]
print(la)
print(lb)

lc = [d for d in os.listdir('.')]
print(lc)

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)


def fib(max1):
    n, a, b = 0, 0, 1
    while n < max1:
        yield b
        a, b, n = b, a+b, n+1
    return

for n in fib(6):
    print(n)


def triangles():
    lst = [1]
    while True:
        yield lst
        if lst == [1]:
            lst = [1, 1]
        else:
            time = len(lst) - 1
            lst_new = [1]
            number = 1
            while number <= time:
                lst_new.append(lst[number-1]+lst[number])
                number = number + 1
            lst = lst_new
            lst.append(1)

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break


it = iter([1, 2, 3, 4])
while True:
    try:
        print(next(it))
    except StopIteration:
        break
