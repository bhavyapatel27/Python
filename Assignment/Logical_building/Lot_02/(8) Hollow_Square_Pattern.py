a = int(input("Enter the Length of the Pyramid:"))
for i in range(0,a):
    for j in range(0,a):
        if i in range(1,a-1) and j in range(1,a-1):
            print("  ",end = " ")
        else:
            print("*  ",end= "")
    print(" ")