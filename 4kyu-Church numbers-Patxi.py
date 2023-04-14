add = lambda a: lambda b: lambda f: lambda x: a(f)(b(f)(x))

mul = lambda a: lambda b: lambda f: a(b(f))

pow = lambda a: lambda b: b(a)
