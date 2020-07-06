"""demo for the scope"""

n = 123  # global scope


def demo():
    """update a global variable from a function"""

    global n   # to refer the global variable from a function
    n = [n, 'pip']
    print(n)


demo()
print(n)

# static