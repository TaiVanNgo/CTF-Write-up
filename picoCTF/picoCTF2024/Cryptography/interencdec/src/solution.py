import base64

base64_string = ''
base64_bytes = base64_string.encode('ascii')

string_bytes = base64.b64decode(base64_bytes)
string = string_bytes.decode('ascii')

print(f'Decoded string: {string}')
