def solution(roman):
    get_numb = []
    result_numb = []
    answ = 0
    for numb in roman:
        get_numb += numb.split()
    print(get_numb)
    for numb_1 in get_numb:
        if numb_1 == "I":
            result_numb.append(1)
        if numb_1 == "V":
            result_numb.append(5)
        if numb_1 == "X":
            result_numb.append(10)
        if numb_1 == "L":
            result_numb.append(50)
        if numb_1 == "C":
            result_numb.append(100)
        if numb_1 == "D":
            result_numb.append(500)
        if numb_1 == "M":
            result_numb.append(1000)
    for i, n in enumerate(result_numb[:-1]):
        if n >= result_numb[i + 1]:
            answ += n
        else:
            answ -= n
    return answ + result_numb[-1]


print(solution('IV'))