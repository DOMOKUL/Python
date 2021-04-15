lenght = int(input()) #длина
width = int(input()) #ширина
list_ = []
for i in range(lenght):
    list_.append(input())
list2=[]
for i in list_[::2]:
    list2.append(i[::2])
lenght = lenght // 2
width = width // 2
print(lenght, width)
for i in list2:
    print(i)