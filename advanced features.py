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
