def show_bits(n):
    if n < 0:
        n = 2**32 + n  # Convert negative integer to its two's complement representation

    binary_representation = [int(bit) for bit in format(n, '032b')]
    return binary_representation
