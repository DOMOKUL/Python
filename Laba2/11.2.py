for _ in range(int(input())):
    print(filter_(input()))
    for i, x in enumerate(line):
        if x == '#':
            return ''
        elif x != '%' :
            return line[i:]