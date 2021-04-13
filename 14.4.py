n = list(map(int, input("Введите числа: ").split()))

xMax = len(n)
yMax = max(n)

print('*' * (xMax + 2))
print('*' + ' ' * xMax + '*')
for y in range(1, yMax + 1):
    print(end='*')
    for nk in n:
        if nk >= yMax - y + 1:
            print(end='*')
        else:
            print(end=' ')
    print('*')


