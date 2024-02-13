def fibonacciint(n):
    a = 0
    b = 1
    count = 0
    if n <= 0:
        print("Please, Enter the positive numbers")
    elif n == 1:
        return 0
    while count < n:
        c = a + b
        print(a)
        a = b
        b = c
        count = count + 1
fibonacciint(int(input("Enter the Int Value:")))