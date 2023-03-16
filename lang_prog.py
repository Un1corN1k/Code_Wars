# https://www.codewars.com/kata/58381907f8ac48ae070000de/solutions/python


from collections import Counter


list1 = [
    { 'firstName': 'Daniel', 'lastName': 'J.', 'country': 'Aruba', 'continent': 'Americas', 'age': 42, 'language': 'Python' },
    { 'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 22, 'language': 'Ruby' },
    { 'firstName': 'Sou', 'lastName': 'B.', 'country': 'Japan', 'continent': 'Asia', 'age': 43, 'language': 'Ruby' },
    { 'firstName': 'Hanna', 'lastName': 'L.', 'country': 'Hungary', 'continent': 'Europe', 'age': 95, 'language': 'JavaScript' },
    { 'firstName': 'Jayden', 'lastName': 'P.', 'country': 'Jamaica', 'continent': 'Americas', 'age': 18, 'language': 'JavaScript' },
    { 'firstName': 'Joao', 'lastName': 'D.', 'country': 'Portugal', 'continent': 'Europe', 'age': 25, 'language': 'JavaScript' }
    ]

list3 = [
          { 'firstName': 'Daniel', 'lastName': 'J.', 'country': 'Aruba', 'continent': 'Americas', 'age': 42, 'language': 'Python' },
          { 'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 22, 'language': 'Ruby' },
          { 'firstName': 'Jayden', 'lastName': 'P.', 'country': 'Jamaica', 'continent': 'Americas', 'age': 18, 'language': 'JavaScript' },
          { 'firstName': 'Joao', 'lastName': 'D.', 'country': 'Portugal', 'continent': 'Europe', 'age': 25, 'language': 'JavaScript' }
        ]

list4 = [
    {'firstName': 'Daniel', 'lastName': 'J.', 'country': 'Aruba', 'continent': 'Americas', 'age': 42,
     'language': 'Python'},
    {'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 22,
     'language': 'Ruby'},
    {'firstName': 'Joao', 'lastName': 'D.', 'country': 'Portugal', 'continent': 'Europe', 'age': 25,
     'language': 'JavaScript'}
]


def lang_prog(list_prog):
    lang = Counter(lang["language"] for lang in list_prog)
    tuple_sort = sorted(((k, variable) for k, variable in lang.items()), key=lambda x: x[1])
    max_tuple = tuple_sort[-1][1]
    min_tuple = tuple_sort[0][1]
    if max_tuple / min_tuple > 2:
        return False
    else:
        return True


def is_language(list_lang):
    j_s = 0
    py = 0
    ruby = 0
    for lang in list_lang:
        if lang['language'] == 'JavaScript':
            j_s += 1
        elif lang['language'] == 'Ruby':
            ruby += 1
        else:
            py += 1
    if py/j_s > 2 or py/ruby > 2:
        return False
    if j_s/py > 2 or j_s/ruby > 2:
        return False
    if ruby/py > 2 or ruby/j_s > 2:
        return False
    return True

print(is_language(list3))
