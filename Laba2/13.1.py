name=input()
count= int(input())
lol = [input() for _ in range(int(input()))]
for _ in range(int(input())):
    tmp = [lol[int(input())-1] for _ in range(int(input()))]
    lol = tmp
print('\n'.join(lol))