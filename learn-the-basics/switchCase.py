from typing import *
import math

def areaSwitchCase(ch: int, a: List[float]):
    area = 0.0

    if ch == 1:

        # Calculate the area of a circle.

        r = a[0]

        area = math.pi * r * r

    if ch == 2:

        # Calculate the area of a rectangle.

        l = a[0]

        b = a[1]

        area = l * b

    

    # Print the area formatted to five decimal places

    return "{:.5f}".format(area)