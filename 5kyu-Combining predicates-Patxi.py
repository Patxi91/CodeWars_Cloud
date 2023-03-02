class predicate:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __and__(self, other):
        def new_func(*args, **kwargs):
            return self.func(*args, **kwargs) and other(*args, **kwargs)
        return predicate(new_func)

    def __or__(self, other):
        def new_func(*args, **kwargs):
            return self.func(*args, **kwargs) or other(*args, **kwargs)
        return predicate(new_func)

    def __invert__(self):
        def new_func(*args, **kwargs):
            return not self.func(*args, **kwargs)
        return predicate(new_func)
