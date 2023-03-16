def create_box(m, n):
    result = []
    for numb in range(n):
        result.append([min(numb, j, n - numb - 1, m - j - 1) + 1 for j in range(m)])
    return result


m_1 = 6
n_1 = 5
print(create_box(m_1,n_1))