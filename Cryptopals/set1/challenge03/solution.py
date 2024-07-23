def bxor(message, key):
    cipher_text = bytearray() # define a bytearray
    for i in range(len(message)):
        cipher_text.append(message[i] ^ key[i]) # append to the array

    # convert to byte again and print
    return bytes(cipher_text)
# -----------------------------------------------------------------------------


#origin hex string
hex_string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
# convert to bytes
hex_bytes = bytes.fromhex(hex_string)

possible_key = bytes([1])
print(possible_key)
key_stream = possible_key * len(hex_bytes) #Repeat the key so it has the same length with the message

bxor(hex_bytes, key_stream)
