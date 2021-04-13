countMen=int(input())
menWorks1 = set()
menWorks2 = set()
for i in range(countMen):
    men=input()
    if men in menWorks1:
        menWorks2.add(men)
    else:
        menWorks1.add(men)
result=menWorks1-menWorks2
res= countMen - len(result)
print(res)
