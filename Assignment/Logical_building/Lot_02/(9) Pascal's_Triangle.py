n = int(input("Enter the value:"))
lst = []
for i in range(n):
    temp_list = []
    for j in range(i+1):
        if j == 0 or j==i:
            temp_list.append(1)
        else:
            temp_list.append(lst[i-1][j-1] + lst[i-1][j])
    lst.append(temp_list)
print(lst)
for k in range(n):
    for l in range(n-k-1):
        print(" ",end="")
    for m in range(k+1):
        print(lst[k][m],end=" ")
    print()


