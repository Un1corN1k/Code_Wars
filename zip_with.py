
a_1 = ["a","b","c","d","e","f"]
b_2 = [6,5,4,3,2,1]
fn_1 = "mul"

def zip_arr(fn,a1,a2):
    result_zip = []
    answ = []
    if fn == "add":
        result_zip += zip(a1,a2)
        for el in result_zip:
            el = sum(el)
            answ.append(el)
    elif fn == "max":
        result_zip += zip(a1,a2)
        for el in result_zip:
            el = max(el)
            answ.append(el)
    elif fn == "pow":
        result_zip += zip(a1, a2)
        for el in result_zip:
                elem_1 = el[0]
                elem_2 = el[1]
                element = pow(elem_1,elem_2)
                answ.append(element)
    elif fn == "mul":
        result_zip += zip(a1, a2)
        for el in result_zip:
                elem_1 = el[0]
                elem_2 = el[1]
                element = elem_1 * elem_2
                answ.append(element)
    return answ

print(zip_arr(fn_1,a_1,b_2))