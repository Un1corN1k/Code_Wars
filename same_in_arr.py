# https://www.codewars.com/kata/57ef016a7b45ef647a00002d/train/python

arr = [[1, 5, 4], ['a', 3, 5], ['b'], [], ['1', 2, 3]]

def filter_homogenous(arrays):
    same_el = []
    for same in arrays:
        count = 0
        const = 0
        while count < len(same):
            if type(same[0]) == type(same[count]):
                count += 1
                const = 1
            else:
                const = -1
                break
        if const == 1:
            same_el.append(same)
    return same_el


print(filter_homogenous(arr))