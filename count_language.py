# https://www.codewars.com/kata/5828713ed04efde70e000346/solutions/python


list1 = [
    { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'C' },
    { 'firstName': 'Anna', 'lastName': 'R.', 'country': 'Liechtenstein', 'continent': 'Europe', 'age': 52, 'language': 'JavaScript' },
    { 'firstName': 'Ramon', 'lastName': 'R.', 'country': 'Paraguay', 'continent': 'Americas', 'age': 29, 'language': 'Ruby' },
    { 'firstName': 'George', 'lastName': 'B.', 'country': 'England', 'continent': 'Europe', 'age': 81, 'language': 'C' },
    ]


def count_languages(list_language):
    language = {}
    for language_p in list_language:
        if language_p["language"] not in language.keys():
            language[language_p["language"]] = 1
        else:
            language[language_p["language"]] += 1
    return language


print(count_languages(list1))