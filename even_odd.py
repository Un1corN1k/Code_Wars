def drop_while(arr, pred):
    new_arr = []
    if pred == "is even":
        for el in arr:
            if not el % 2:
                new_arr.append(el)
    if pred == "is odd":
        for el in arr:
            if el % 2:
                new_arr.append(el)
    return new_arr


arr_1 = [2,6,4,10,1,5,4,3]
func = "is odd"
print(drop_while(arr_1,func))