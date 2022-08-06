from collections import OrderedDict

def ordered_count(inp):
    return [(c, inp.count(c)) for c in ''.join(OrderedDict.fromkeys(inp).keys())]
