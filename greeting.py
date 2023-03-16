# https://www.codewars.com/kata/58279e13c983ca4a2a00002a

list1 = [
  { 'firstName': 'Sofia', 'lastName': 'I.', 'country': 'Argentina', 'continent': 'Americas', 'age': 35, 'language': 'Java' },
  { 'firstName': 'Lukas', 'lastName': 'X.', 'country': 'Croatia', 'continent': 'Europe', 'age': 35, 'language': 'Python' },
  { 'firstName': 'Madison', 'lastName': 'U.', 'country': 'United States', 'continent': 'Americas', 'age': 32, 'language': 'Ruby' }
]


def greet_developers(lst):
    for dev in lst:
      dev["greeting"] = f'Hi {dev["firstName"]}, what do you likethe most about {dev["language"]}'
    return lst


print(greet_developers(list1))