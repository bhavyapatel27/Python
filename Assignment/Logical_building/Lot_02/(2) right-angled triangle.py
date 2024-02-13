"""Print a right-angled triangle pattern of asterisks. The user inputs the height.
    Enter height: 4
    *
    **
    ***
    ****"""

n = int(input("Enter the value:"))
for i in range(0,n):
    for j in range(i+1):
        print("*",end="")
    print(" ")