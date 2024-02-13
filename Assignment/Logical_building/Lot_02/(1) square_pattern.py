"""Print a square pattern of asterisks. The user inputs the side length.
    Enter side length: 5
    *****
    *****
    *****
    *****
    *****  """
n = int(input("Enter the value:"))
for i in range(0,n):
    for j in range(0,n):
        print("*",end=" ")
    print("")