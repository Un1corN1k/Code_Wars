# https://www.codewars.com/kata/563f879ecbb8fcab31000041/train/python


def factory(x):
    def arrs(my_arr):
        result = []
        for el in my_arr:
            elem = el * x
            result.append(elem)
        return result
    return arrs


print(factory(5))


