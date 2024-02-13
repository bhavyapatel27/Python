n = 5
for i in range(0, n):
    for j in range(i+1):
        count = 0
        for k in range(j):
            count += n-k
        if j%2 == 0:
            print(count + i-j+1, end=" ")
        else:
            print(count + n - i,end=" ")
    print() 