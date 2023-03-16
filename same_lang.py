# https://www.codewars.com/kata/58287977ef8d4451f90001a0/solutions/python


list1 = [
  { 'firstName': 'Daniel', 'lastName': 'J.', 'country': 'Aruba', 'continent': 'Americas', 'age': 42, 'language': 'JavaScript' },
  { 'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 22, 'language': 'JavaScript' },
  { 'firstName': 'Hanna', 'lastName': 'L.', 'country': 'Hungary', 'continent': 'Europe', 'age': 65, 'language': 'Java' },
]


def same_lang(list_lang):
    true = 0
    language = [dev["language"] for dev in list_lang]
    for dev in range(len(language)):
        if language[dev] == language[dev - 1]:
            true += 1
    if true == len(language):
        return True
    else:
        return False

print(same_lang(list1))