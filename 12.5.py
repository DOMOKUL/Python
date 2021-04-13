n = int(input())
r = 1
rr = []
dd = []
while r not in rr:
    rr.append(r)
    dd.append(10*r//n)
    r = 10*r%n
print("".join(map(str, dd[rr.index(r):])))

