n = int(input("Enter the value:"))
for m in range(0,n):
    for o in range(m):
        print(" ",end=" ")
    for p in range(n-m):
        print("*",end=" ")
    for q in range(n-(m+1)):
        print("*",end=" ")
    print()