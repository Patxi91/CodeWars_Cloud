def mean(lst):

    # Extract integers from the list and calculate the mean
    integers = [int(x) for x in lst if x.isdigit()]
    mean_value = sum(integers) / 10
    
    # Extract characters from the list and concatenate them into a string
    characters = ''.join(x for x in lst if not x.isdigit())
    
    return [round(mean_value, 1), characters]
