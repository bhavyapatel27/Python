def lcm(n1,n2):
    if n1>n2:
        high_num = n1
    else:
        high_num = n2
    val = high_num

    while(True):
        if high_num%n1 == 0 and high_num%n2 == 0:
            print(f"LCm of {n1} and {n2} is {high_num}")
            break
        else:
            high_num = high_num + val

lcm(int(input("Enter the 1st number:")),int(input("Enter the 2nd number:")))