def binary_to_string(binary):
    binary_values = binary.split('0b')[1:]
    result = ''
    for binary_value in binary_values:
        decimal_value = int(binary_value, 2)
        result += chr(decimal_value)
    return result
