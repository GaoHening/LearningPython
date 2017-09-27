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


def check_file(name, path='.'):  # 在当前目录和子目录查找包含对应字符串的文件路径
    for tempname in os.listdir(path):
        if os.path.isfile(tempname):
            if name in os.path.split(tempname)[1]:
                yield os.path.join(path,tempname)
        else:
            path_dep = os.path.join(path, tempname)
            check_file(name, path_dep)

print(list(check_file('cti')))
