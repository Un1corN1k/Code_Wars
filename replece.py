
def correct(s):
    error_list = ['5', '0', '1']
    correct_list = ['S', 'O', 'I']
    for s in range(len(s)):
        s = s.replece(str(error_list[s]),correct_list[s])
    return s

s = 'L0ND0N'
print(correct(s))