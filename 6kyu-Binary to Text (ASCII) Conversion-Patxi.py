def binary_to_string(binary):
    # Split the binary string into 8-bit chunks
    chunks = [binary[i:i+8] for i in range(0, len(binary), 8)]

    # Convert each chunk to its ASCII character representation
    chars = [chr(int(chunk, 2)) for chunk in chunks]

    # Join the characters into a string and return it
    return ''.join(chars)
