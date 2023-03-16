#https://www.codewars.com/kata/582746fa14b3892727000c4f/solutions/python

def count_developers(lst):
    numd = 0
    for developers in lst:
        region = developers.get("continent")
        lang_program = developers.get("language")
        if region == 'Europe' and lang_program == 'JavaScript':
            numd += 1
    return numd


lst1 = [
  { 'firstName': 'Maia', 'lastName': 'S.', 'country': 'Tahiti', 'continent': 'Oceania', 'age': 28, 'language': 'JavaScript' },
  { 'firstName': 'Shufen', 'lastName': 'L.', 'country': 'Taiwan', 'continent': 'Asia', 'age': 35, 'language': 'HTML' },
  { 'firstName': 'Sumayah', 'lastName': 'M.', 'country': 'Tajikistan', 'continent': 'Asia', 'age': 30, 'language': 'CSS' },
]

print(count_developers(lst1))