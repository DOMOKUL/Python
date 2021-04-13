s = set()
g = set()
n = int(input())
for i in range(n):
    s.add(input())
n = int(input())
for i in range(n):
    d = int(input())
    for a in range(d):
        g.add(input())
print(*sorted(s-g), sep='\n')