# https://www.codewars.com/kata/582dace555a1f4d859000058/solutions/python

list1 = [
  { 'firstName': 'Harry', 'lastName': 'K.', 'country': 'Brazil', 'continent': 'Americas', 'age': 22, 'language': 'JavaScript', 'githubAdmin': 'yes' },
  { 'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 49, 'language': 'Ruby', 'githubAdmin': 'no' },
  { 'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia', 'age': 34, 'language': 'JavaScript', 'githubAdmin': 'yes' },
  { 'firstName': 'Piotr', 'lastName': 'B.', 'country': 'Poland', 'continent': 'Europe', 'age': 128, 'language': 'JavaScript', 'githubAdmin': 'no' }
  ]


def find_admin(list, lang):
    dict_adm = []
    for adm in list:
        adm_lg = adm.get("language")
        adm_gh = adm.get("githubAdmin")
        if adm_lg == lang and adm_gh == "yes":
            dict_adm.append(adm)
    return dict_adm


print(find_admin(list1, 'JavaScript'))