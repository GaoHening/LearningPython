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
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
print(s4)
