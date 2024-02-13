# Upward Triangle
# a = int(input("Enter the Length of the Pyramid:"))
# for i in range(0,a):
#     for j in range(a-i):
#         print(" ",end = " ")
#     for k in range(i):
#         print("*",end=" ")
#     for l in range(i+1):
#         print("*",end=" ")
#     print(" ")

# a = int(input("Enter the length of the pyramid:"))
# RHS Pattern
# a = 5
# for i in range(0,a):
#     for j in range(i+1):
#         print("*",end = " ")
#     print(" ")
#
# hollow RHS Triangle
# a = 5
# for i in range(0,a):
#     for j in range(i+1):
#         if i in range(1,a) and j in range(0,i): #i = 0 row and j = i+1 = 1 star print because at 0 no star print so, j in j it self i-1
#             print(" ",end=" ")
#         else:
#             print("*",end = " ")
#     print(" ")

# Space triangle

# a = 5
# for i in range(0,a):
#     for j in range(a-i):
#         print("*",end = " ")
#     print(" ")

# Downword triangle
# a = 5
# for i in range(0,a+1):
#     for j in range(i):
#         print(" ",end = " ")
#     for k in range(a-i):
#         print("*",end=" ")
#     for l in range(a-(i+1)):
#         print("*",end=" ")
#     print(" ")

# #Upward Triangle
# a = int(input("Enter the Length of the Pyramid:"))
# for i in range(0,a):
#     if i ==
#     for j in range(a-i):
#         print(" ",end = " ")
#     for k in range(i):
#         print("*",end=" ")
#     for l in range(i+1):
#         print("*",end=" ")
#     print(" ")

# Diamond Pattern
# a = 5
# for i in range(0, a):
#     for j in range(a - i):
#         print(" ", end=" ")
#     for k in range(i):
#         if i in range(1, a) and k in range(1, a):
#             print(" ", end=" ")
#         else:
#             print("*", end=" ")
#         # print("*",end=" ")
#     for l in range(i + 1):
#         # print("*",end=" ")
#         if i in range(1, a) and l in range(0, i):
#             print(" ", end=" ")
#         else:
#             print("*", end=" ")
#     for q in range(a - i):
#         print(" ", end=" ")
#     print()
# for p in range(1, a):
#     for m in range(p + 1):
#         print(" ", end=" ")
#     for n in range(a - p):
#         # print("*",end=" ")
#         if p in range(1, a) and n in range(1, a):
#             print(" ", end=" ")
#         else:
#             print("*", end=" ")
#     for o in range(a - (p + 1)):
#         print("*", end=" ")
#         if p in range(1, a) and o in range(a,2):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     for r in range(p + 1):
#         print(" ", end=" ")
#     print()

# Hollow Triangle

# a = 7
# for i in range(0, a):
#     for j in range(a - i):
#         print(" ", end=" ")
#     for k in range(i):
#         if i in range(1, a) and k in range(1, a):
#             print(" ", end=" ")
#         else:
#             print("*", end=" ")
#     for l in range(i + 1):
#         if i in range(1, a) and l in range(0, i):
#             print(" ", end=" ")
#         else:
#             print("*", end=" ")
#         # print("*",end=" ")
#     print()
# for p in range(1, a):
#     for m in range(p + 1):
#         print(" ", end=" ")
#     for n in range(a - p):
#         if p in range(1, a) and n in range(1, a):
#             print(" ", end=" ")
#         else:
#             print("*", end=" ")
#     for o in range(a - (p + 1)):
#         if p in range(1, a) and o in range(0,p):
#             print(" ", end=" ")
#         else:
#             print("*", end=" ")
#         # print("*",end=" ")
#     print()

# a = 10
# for i in range(1,a):
#     for j in range(1,a):
#         print(j,end=" ")
#     print()

# Except Diamond Pattern
# a = 5
# for i in range(0,a):
#     for j in range(a-i):
#         print("*",end = " ")
#     for k in range(i):
#         print(" ",end=" ")
#     for l in range(i+1):
#         print(" ",end=" ")
#     for j in range(a-i):
#         print("*",end = " ")
#     print()
# for p in range(1,a):
#     for m in range(p+1):
#         print("*",end = " ")
#     for m in range(a-p):
#         print(" ",end=" ")
#     for n in range(a-(p+1)):
#         print(" ",end=" ")
#     for m in range(p+1):
#         print("*",end = " ")
#     print()

a = 15
for i in range(5):
    for j in range(5):
        if i+j == 2:
            print("*",end=" ")
        else:
            print(" ",end="")
    print("")