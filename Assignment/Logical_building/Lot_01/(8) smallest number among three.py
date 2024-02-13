a = int(input("Enter the 1st number:"))
b = int(input("Enter the 2nd number:"))
c = int(input("Enter the 3rd number:"))

if a<b and a<c:
    print(f"{a} is smaller")
elif b<a and b<c:
    print(f"{b} is smaller")
else:
    print(f"{c} is smaller")

