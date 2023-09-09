def spacey(array):
    result = []
    current_str = ''

    for word in array:
        current_str += word
        result.append(current_str)

    return result
