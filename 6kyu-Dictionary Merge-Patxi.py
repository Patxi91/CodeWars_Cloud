def merge(*dicts):
    result = {}

    for d in dicts:
        for key, value in d.items():
            if key in result:
                # If the key already exists in the result, append the value to the existing list
                result[key].append(value)
            else:
                # If the key is not in the result, create a new list with the value
                result[key] = [value]

    return result
