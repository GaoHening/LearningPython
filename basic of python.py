#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("I'm ok")
print("I\'m \"ok\"")
print("\\\n\\")

# r默认不进行转义
print("\\\t\\")
print(r"\\\t\\")

# '''多行显示
print('''line1
line2
line3''')

print(3 > 2)

a = "ABC"
b = a
a = "DEF"
print(b)

# 练习
n = 123
f = 456.789

s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
print(s4)

print(ord("a"))
print(chr(25991))
r = b"\xe4\xb8\xad\xe6\x96\x87".decode('utf-8')
print(r)

print("%s growth rate:%d%%" % ("The", 50))

s1 = 72
s2 = 85
r = (s2-s1)/s1*100
print("%.1f%%" % r)

classmate = ['A', 'B', 'C']
print(classmate[len(classmate) - 1])
classmate.append('D')
print(classmate)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])
