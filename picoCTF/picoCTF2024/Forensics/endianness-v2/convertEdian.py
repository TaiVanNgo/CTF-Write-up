# This program convert the the file from little edian to big edian
import struct

def little_to_big_endian(input_file_path, output_file_path):
    # Define the size of each chunk (4 bytes for 32-bit integers)
    chunk_size = 4

    with open(input_file_path, 'rb') as input_file, open(output_file_path, 'wb') as output_file:
        while True:
            # Read a chunk of data
            chunk = input_file.read(chunk_size)
            
            # Break the loop if the end of the file is reached
            if not chunk:
                break

            # If the chunk is smaller than the chunk_size, pad it with zeros (for incomplete last chunk)
            if len(chunk) < chunk_size:
                chunk = chunk.ljust(chunk_size, b'\0')

            # Unpack the data from little-endian and repack it to big-endian
            little_endian_data = struct.unpack('<I', chunk)
            big_endian_data = struct.pack('>I', *little_endian_data)

            # Write the converted data to the output file
            output_file.write(big_endian_data)

# Example usage
input_file_path = 'challengefile'
output_file_path = 'big_edian'
little_to_big_endian(input_file_path, output_file_path)
