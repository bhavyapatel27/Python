def romman_to_int(s):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0

    for i in range(len(s)):
        if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
            result = result - roman[s[i]]
        else:
            result = result + roman[s[i]]
    return result


def int_to_romman(i):
    symbols = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
        (9, 'IX'), (5, 'V'),
        (4, 'IV'), (1, 'I')]
    roman = ''
    for value, symbol in symbols:
        while i >= value:
            roman = roman + symbol
            i = i - value

    return roman


a = int(input("which conversion you want\n str to int = 1\nint to str = 2:\n"))
if a == 1:
    b = input("Enter the String:")
    s = b.upper()
    print(romman_to_int(s))
else:
    i = int(input("Enter the Int value:\n"))
    print(int_to_romman(i))

