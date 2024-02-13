""" Python program to remove spaces from a string without an inbuilt function """

a = input("Enter the string:")
b = ''
for i in a:
    if i != ' ':
        b+=i
print(f"string before {a}")
print(f"string after removing space {b}")


