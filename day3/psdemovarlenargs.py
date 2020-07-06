"""variable length arguments """


def demo(*args):
    print(args)


# demo()
# demo(1000)
# demo(1, 2, 3, 4, 5)

items = [11, 22, 33]
demo(items)
demo(*items)   # to pass content of the object as the arguments
print()

items = (11, 22, 33)
demo(items)
demo(*items)
print()

param = {'brightness': 0.77, 'constrast': 0.66, 'hue': 0.88}
demo(*param)
# demo('python')
# demo(*'python')