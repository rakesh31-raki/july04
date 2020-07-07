"""demo for the simple inheirtance"""


class Person:
    """base class"""
    def __init__(self, fn, ln):
        self.fn = fn
        self.ln = ln

    def get_info(self):
        print('first name :', self.fn)
        print('last name :', self.ln)


if __name__ == '__main__':   # namespace validation
    p = Person('larry', 'wall')
    p.get_info()
    print(__name__)