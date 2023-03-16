# https://www.codewars.com/kata/580dda86c40fa6c45f00028a/train/python

arr = [1, 2, 3, 4]
arr_1 = [-3,-2,2,3]
arr_2 = ["a",12,9,"z",42]

def cube_odd(arr):
    result = []
    sum = 0
    if any(type(x) is not int for x in arr):
        return None
    for i in arr:
        i = i ** 3
        result.append(i)
    for x in result:
        if x % 2:
            sum += x
    return sum


print(cube_odd(arr))
