"""
Alphabet Pattern
    A
    AB
    ABC
    ABCD
    ABCDE
"""

n = int(input("Enter the value:"))

for i in range(0,n):
    for j in range(i+1):
        print(chr(ord('A')+j),end=" ")

    print(" ")