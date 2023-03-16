from math import sqrt


def nearestSq(n):
    return round(sqrt(n)) ** 2


print(nearestSq(111))