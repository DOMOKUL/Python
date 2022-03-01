n = int(input("Введите размер матрицы: "))
bacteri_array = []
for i in range(n):
    bacteri_array.append([])
    for j in range(n):
        bacteri_array[i].append(int(input("Введите значение: ")))
print(bacteri_array)
