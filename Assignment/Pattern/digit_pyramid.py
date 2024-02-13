a = int(input("Enter the Length of the pyramid:"))
for i in range(a):
    for j in range(i):
        print("", end=" ")
    for k in range(a - i):
        print(k + 1 , end=" ")
    print()
for l in range(a):
    for m in range(a - (l + 1)):
        print("", end=" ")
    for n in range(l + 1):
        print(n + 1, end=" ")
    print()
