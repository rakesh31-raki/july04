"""custom / user defined exception """


class RadiationError(Exception):
    """custom exception"""

    def __str__(self):
        return f'{self.__class__.__name__}: {self.args[0]}'


def check_4_limit(value):
    if not 0.3 <= value <= 0.7:
        raise RadiationError(f'abnormal radiation level : {value}')


if __name__ == '__main__':
    try:
        check_4_limit(.15)
    except RadiationError as error:
        print(error)