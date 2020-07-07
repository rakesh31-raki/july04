class Dummy:
    def demo(self):
        print('null arguments')

    def demo(self, a, b):
        print(a + b)


if __name__ == '__main__':
    d = Dummy()
    d.demo()
