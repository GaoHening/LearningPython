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

#s = input("birth:")
#if int(s)<2000:
#    print("before 00")
#else:
#    print("after 00")

height = 1.79
weight = 90
bmi = weight/(height*height)
print("your bmi is %.2f" % bmi)
if bmi < 18.5:
    print("过轻")
elif bmi < 25:
    print("正常")
elif bmi < 28:
    print("过重")
elif bmi < 32:
    print("肥胖")
else:
    print("严重肥胖")

re = 0
for x in range(101):
    re = re + x
print(re)

L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print("hello,", name)
