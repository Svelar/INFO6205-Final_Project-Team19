import math


def dis(point1, point2):
    d = math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)
    return d
