list_1 = [1, 2, 2, 2300, 1200, 11, 200, 1200, 32, 98]
max_1 = -99999
max_2 = None
for i in list_1:
    if i > max_1:
        max_1 = i
        continue
        print (max_1)
    if max_2 is None or i > max_2:
        max_2 = i
print(max_2)
