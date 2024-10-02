import string

cipher_message = [16, 9, 3, 15, 3, 20, 6, 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14]

flag = ''

for i in cipher_message:
    flag += string.ascii_uppercase[i-1]

print(flag)

# flag: PICOCTF{THENUMBERSMASON}