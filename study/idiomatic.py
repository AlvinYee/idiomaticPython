def variablefun(*args, **kwargs):
    print(args, kwargs)


variablefun((1, 2, 3), {'a': 4, 'b': 5, 'c': 6})
