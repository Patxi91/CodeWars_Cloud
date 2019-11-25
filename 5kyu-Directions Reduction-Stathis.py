def dirReduc(arr):
    mapping = {'NORTH': 1, 'SOUTH': -1, 'EAST': 2, 'WEST': -2}
    inv_mapping = {v: k for k, v in mapping.items()}
    num_arr = [mapping[cardinal] for cardinal in arr]
    
    changed = True
    while changed:
        changed = False
        for i in range(len(num_arr)-1):
            if sum(num_arr[i:i+2]) == 0:
                num_arr[i] = 0
                num_arr[i+1] = 0
                changed = True
        num_arr = [val for val in num_arr if val != 0]
        
    return [inv_mapping[num] for num in num_arr]
