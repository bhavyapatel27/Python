n = int(input("Enter the value:"))

count = 0
for i in range(1,n):
    for j in range(i):
        count += 1
        print(count,end=" ")
    print()