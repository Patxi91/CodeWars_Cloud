def to_bytes(n):
    if n == 0:
        return ['00000000']  # Special case for 0

    # Convert the integer to binary and remove the '0b' prefix
    binary_str = bin(n)[2:]

    # Pad the binary string with leading zeros to ensure it's a multiple of 8
    padding = (8 - len(binary_str) % 8) % 8
    binary_str = '0' * padding + binary_str

    # Split the binary string into 8-bit chunks
    byte_chunks = [binary_str[i:i + 8] for i in range(0, len(binary_str), 8)]

    return byte_chunks
