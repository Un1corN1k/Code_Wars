# https://www.codewars.com/kata/5a81b78d4a6b344638000183


def change_suffixes(word):
    dict = {'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
             'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
             'ir': ['o', 'es', 'e', 'imos', 'is', 'en']}
    return {word: [word[:-2] + v for v in dict[word[-2:]]]}


word = "comer"


print(change_suffixes(word))