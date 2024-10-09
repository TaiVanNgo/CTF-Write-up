import string

flag = []

with open("message.txt") as filp:  # file pointer
    contents = filp.read()
    # contents.split will convert the whole string -> an array of characters
    numbers = [int(val) for val in contents.split()]  # convert to integer
    print(numbers)

    for number in numbers:
        modulus = pow(number, -1, 41)
        print(modulus)
        if modulus in range(27):  # 0 -> 25
            print(modulus)
            flag.append(string.ascii_uppercase[modulus - 1])
        elif modulus in range(27, 37):
            flag.append(string.digits[modulus - 27])
        else:
            flag.append('_')

print('Flag: ')
print(f"picoCTF{{{"".join(flag)}}}")
