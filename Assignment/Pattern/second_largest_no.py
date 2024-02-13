a = [11,9,12,96,96,96]
# for i,l in enumerate(a):
#     print(i)
a.sort()
print(a)
print(a.count(96))
for i in a:
    if a.count(i) >1:
        a.remove(i)
print(a[-2])

# a.sort()
# print(a[-2])
# max(a)
# print(a[2])

# def second_l(arr):
#     largest = s_largest = float('-inf')
#
#     for num in arr:
#         if num > largest:
#             s_largest = largest
#             largest = num
#         elif num > s_largest and num != largest:
#             s_largest = num
#     else:
#         return s_largest
#
# # Example usage:
# my_list = [3,5,-7,-7,8]
# result = second_l(my_list)
# print("Second largest element:", result)

