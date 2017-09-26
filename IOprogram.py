with open('text.txt', 'r') as f:
    # print(f.read())
    for line in f.readlines():
        # print(line)
        print(line.strip())

with open('text.txt', 'w') as f:
    f.write('This is another text!\n')
    f.write('try to add another line!')

