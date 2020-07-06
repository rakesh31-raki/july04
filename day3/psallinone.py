def demo(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)


demo(1, 2, lang='perl', author='wall', version=2)
