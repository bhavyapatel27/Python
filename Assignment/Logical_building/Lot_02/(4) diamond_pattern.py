n = int(input("Enter the value:"))


for i in range(0,n):
    for j in range(n-i):
        print(" ",end= " ")
    for k in range(i-1):
        print("*",end=" ")
    for l in range(i):
        print("*", end=" ")
    print()
for m in range(0,n):
    for o in range(m):
        print(" ",end=" ")
    for p in range(n-m):
        print("*",end=" ")
    for q in range(n-(m+1)):
        print("*",end=" ")
    print()

