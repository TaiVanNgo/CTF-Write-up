# This code is based on Mr. John Hammond's code.
# Source: https://www.youtube.com/watch?v=nIB1IxK1FmY
import string

flag = []

with open("message.txt") as filp:  # file pointer
    contents = filp.read()
    # contents.split will convert the whole string -> an array of characters
    numbers = [int(val) for val in contents.split()]  # convert to integer
    print(numbers)

    for number in numbers:
        modulus = number % 37
        if modulus in range(26):  # 0 -> 25
            flag.append(string.ascii_uppercase[modulus])
        elif modulus in range(26, 36):
            flag.append(string.digits[modulus - 26])
        else:
            flag.append('_')

print('Flag: ')
print(f"picoCTF{{{"".join(flag)}}}")
