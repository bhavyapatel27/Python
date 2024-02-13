n = 5
for i in range(0, n+1):
    count = i
    for j in range(0, i):
        print(count, end = " ")
        count += n - (j+1)
    print()