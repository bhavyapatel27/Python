"""
 Number Triangle Pattern
    1
    12
    123
    1234
    12345
"""

n = int(input("Enter the value:"))


for i in range(1,n+1):
    for j in range(i):
        print(j+1,end="")
    print()
