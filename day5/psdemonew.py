class Demo:
    """borg's singleton pattern"""
    __instance = None

    def __new__(cls, *args, **kwargs):
        """static method"""
        if cls.__instance:
            raise Exception('singleton class can\'t be instantiated twice')
        else:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self):
        """instance method"""


if __name__ == '__main__':
    d1 = Demo()
    print(d1)

    d2 = Demo()
    print(d2)

    # d3 = Demo()
    # print(d3)
    #
    # # sublime singleton pattern
