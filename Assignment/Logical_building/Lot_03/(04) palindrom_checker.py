n = int(input("Enter the integer"))
b = n
a = 0
while (n > 0):
    last_digit = n % 10
    a = a * 10 + last_digit
    n = n // 10
if b == a:
    print("Number is palindrom")
else:
    print("Number is not palindrom")