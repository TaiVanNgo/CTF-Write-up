def bxor(message, key):
    cipher_text = bytearray() # define a bytearray
    for i in range(len(message)):
        cipher_text.append(message[i] ^ key[i]) # append to the array

    print(bytes(cipher_text)) # convert to byte again and print
# -----------------------------------------------------------------------------


#origin hex string
hex_string = b'hi there!'

# convert to 

key = b'\x77'
key_stream = key * len(hex_string) #Repeat the key so it has the same length with the message

bxor(hex_string, key_stream)

