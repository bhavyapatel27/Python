""" Python program to count vowels and consonants in the string """

a = input("Enter the string:")

vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
vowels_list = []
consonant_list = []

for i in a:
    if i in vowels:
        vowels_list.append(i)
    else:
        consonant_list.append(i)


print(f"there are {len(set(vowels_list))} vowels in given string:{a}")
print(f"there are {len(set(consonant_list))} consonant in given string:{a}")
print(set(vowels_list))