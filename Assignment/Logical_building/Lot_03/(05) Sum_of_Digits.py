n = 123
a = 0

while (n > 0):
    last_digit = n % 10
    n = n // 10
    a += last_digit
print(a)
