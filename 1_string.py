def create_message(s):
    def func(x=''):
        if x:
            lst.append(x)
            return func
        return ' '.join(lst)

    lst = [s]
    return func