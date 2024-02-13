""" given character is a vowel or consonant """

a = input("enter the character:")
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

# consonant = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z",
#              "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

if a in vowels:
    print(f"character {a} is vowel")
else:
    print(f"character {a} is consonant")
