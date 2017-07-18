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
