def atomic_number(electrons):
    result = []
    number = 0
    res = 0
    for n in range(1,electrons+1):
        count =  2*(n**2)
        number += count
        if number <= electrons:
            result.append(count)
    for numb in result:
        res += numb
    rest = electrons - res
    if rest != 0:
        result.append(rest)
    return result


print(atomic_number(10))