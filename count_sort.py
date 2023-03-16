# https://www.codewars.com/kata/583952fbc23341c7180002fd/solutions/python

def count_meal(list_meal):
    meals = {}
    for meal in list_meal:
        if meal["meal"] not in meals.keys():
            meals[meal["meal"]] = 1
        else:
            meals[meal["meal"]] += 1
    return meals

list1 = [
    {'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19,
     'language': 'C', 'meal': 'vegetarian' },
    {'firstName': 'Anna', 'lastName': 'R.', 'country': 'Liechtenstein', 'continent': 'Europe', 'age': 52,
     'language': 'JavaScript', 'meal': 'standard' },
    {'firstName': 'Ramona', 'lastName': 'R.', 'country': 'Paraguay', 'continent': 'Americas', 'age': 29,
     'language': 'Ruby', 'meal': 'vegan' },
    {'firstName': 'George', 'lastName': 'B.', 'country': 'England', 'continent': 'Europe', 'age': 81,
     'language': 'C', 'meal': 'vegetarian' },
    {'firstName': 'George', 'lastName': 'B.', 'country': 'England', 'continent': 'Europe', 'age': 81,
     'language': 'C', 'meal': 'vegetarian' },
    {'firstName': 'George', 'lastName': 'B.', 'country': 'England', 'continent': 'Europe', 'age': 81,
     'language': 'C', 'meal': 'vegetarian' },
    {'firstName': 'Anna', 'lastName': 'R.', 'country': 'Liechtenstein', 'continent': 'Europe', 'age': 52,
     'language': 'JavaScript', 'meal': 'standard' },
    {'firstName': 'Anna', 'lastName': 'R.', 'country': 'Liechtenstein', 'continent': 'Europe', 'age': 52,
     'language': 'JavaScript', 'meal': 'standard' },
]

print(count_meal(list1))