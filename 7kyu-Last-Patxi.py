def last(*args):
    if len(args)!=1:
        return args[-1]
    else:
        if isinstance(args[-1], int):
            return args[-1]
        else:
            return args[-1][-1]
