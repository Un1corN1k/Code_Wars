# https://www.codewars.com/kata/586909e4c66d18dd1800009b/solutions/python
# def addition(n):
#     return n + n
#
#
# numbers = list(map(int,input().split()))
# result = map(addition, numbers)
# print(list(result))


def multyply_all(arr):
    def inside(n):
        return [i*n for i in arr]
    return inside()

