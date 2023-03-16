def no_space(x):
    result = ""
    for word in x:
        if word == " ":
            continue
        else:
            result += result.join(word)
    return result


def no_space_1(s):
    return s.replace(' ', '')


str_1 = "8 j 8   mBliB8g  imjB8B8  jl  B"
print(no_space(str_1))