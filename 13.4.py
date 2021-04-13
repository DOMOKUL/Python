num = int(input())
first = [int(input()) for i in range(num)]
second = first[:]
training = int(input())
for i in range(training):
    brother = int(input())
    if brother == 1:
        first[int(input())] += int(input())
    elif brother == 2:
        second[int(input())] += int(input())
print(*first)
print(*second)
first = [13, 10, 10]
second = [13, 10, 17]

count = 0
for x, y in zip(first, second):
    if x == y:
        count += 1
print(count)