# https://www.codewars.com/kata/582ba36cc1901399a70005fc/solutions/python


list1 = [
  { 'firstName': 'Maria', 'lastName': 'Y.', 'country': 'Cyprus', 'continent': 'Europe', 'age': 33, 'language': 'Java' },
  { 'firstName': 'Victoria', 'lastName': 'T.', 'country': 'Puerto Rico', 'continent': 'Americas', 'age': 70, 'language': 'Python' },
]


def get_average(list_age):
    age = []
    for ages in list_age:
        ages = ages.get("age")
        age.append(ages)
    return round(sum(age) / len(list_age), 0)


print(get_average(list1))