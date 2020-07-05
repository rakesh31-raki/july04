"""demo for the IO"""

import math


def compute(radius):
    """function definition"""
    return math.pi * radius ** 2


try:
    user_radius = float(input('enter the radius :'))  # reading a line from the stdin
    area = compute(user_radius)  # function calling
    print('area :', area)
except ValueError as error:
    print(error)
