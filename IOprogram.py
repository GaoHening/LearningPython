from io import StringIO
import os
with open('text.txt', 'r') as f:
    # print(f.read())
    for line in f.readlines():
        # print(line)
        print(line.strip())

with open('text.txt', 'w') as f:
    f.write('This is another text!\n')
    f.write('try to add another line!')

f = StringIO('hello\nworld\ntext')
for line in f.readlines():
    print(line.strip())

Lib = [x for x in os.listdir('.') if os.path.isdir(x)]
print(Lib)
Lib = [x for x in os.listdir('.') if os.path.isfile(x)]
print(Lib)
Lib = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print(Lib)


