# def find_it(seq):
#     a = 0
#     res = dict((i, seq.count(i)) for i in seq)
#     for value in res.values():
#         if not value % 2 == 0:
#             a += value
#     reverseMap = dict(zip(res.values(), res.keys()))
#     return reverseMap.get(a)


def find_it(seq):
    item = {}

    for x in seq:
        if x in item:
            item[x] += 1
        else:
            item[x] = 1
    for x in item:
        if (item[x] % 2) != 0:
            return x

        
list_1 = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
print(find_it(list_1))