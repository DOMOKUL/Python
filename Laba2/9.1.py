m=int(input())
n=int(input())
mBook = set()
nBook = set()
for i in range(m):
    book1=input()
    mBook.add(book1)
for i in range(n):
    book2=input()
    nBook.add(book2)
    if book2 in mBook:
        print("YES")
    else:
        print("NO")