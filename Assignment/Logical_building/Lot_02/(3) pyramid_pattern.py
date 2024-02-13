"""Print a pyramid pattern of asterisks. The user inputs the number of rows.
    Enter number of rows: 4
       *
      ***
     *****
    *******"""

n = int(input("Enter the value:"))

for i in range(0,n):
    for j in range(n-i):
        print(" ",end= " ")
    for k in range(i-1):
        print("*",end=" ")
    for l in range(i):
        print("*", end=" ")
    print(" ")
