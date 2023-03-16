# https://www.codewars.com/kata/5829ca646d02cd1a65000284/solutions/python

list1 = [
  { 'firstName': 'Harry', 'lastName': 'K.', 'country': 'Brazil', 'continent': 'Americas', 'age': 19, 'language': 'Python' },
  { 'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 29, 'language': 'JavaScript' },
  { 'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia', 'age': 39, 'language': 'Ruby' },
  { 'firstName': 'Noa', 'lastName': 'A.', 'country': 'Israel', 'continent': 'Asia', 'age': 40, 'language': 'Ruby' },
  { 'firstName': 'Andrei', 'lastName': 'E.', 'country': 'Romania', 'continent': 'Europe', 'age': 59, 'language': 'C' },
  { 'firstName': 'Maria', 'lastName': 'S.', 'country': 'Peru', 'continent': 'Americas', 'age': 60, 'language': 'C' },
  { 'firstName': 'Lukas', 'lastName': 'X.', 'country': 'Croatia', 'continent': 'Europe', 'age': 75, 'language': 'Python' },
  { 'firstName': 'Chloe', 'lastName': 'K.', 'country': 'Guernsey', 'continent': 'Europe', 'age': 88, 'language': 'Ruby' },
  { 'firstName': 'Viktoria', 'lastName': 'W.', 'country': 'Bulgaria', 'continent': 'Europe', 'age': 98, 'language': 'PHP' },
  { 'firstName': 'Piotr', 'lastName': 'B.', 'country': 'Poland', 'continent': 'Europe', 'age': 128, 'language': 'JavaScript' }
]


def age_group(list_guests):
    teens = 0
    twenties = 0
    thirties = 0
    forties = 0
    fifties = 0
    sixties = 0
    seventies = 0
    eighties = 0
    nineties = 0
    centenarian = 0
    for guest in list_guests:
        teens1 = guest.get("age")
        if teens1 <= 19:
            teens += 1
    for guest in list_guests:
        twenties1 = guest.get("age")
        if 20 <= twenties1 <= 29:
            twenties += 1
    for guest in list_guests:
        thirties1 = guest.get("age")
        if 30 <= thirties1 <= 39:
            thirties += 1
    for guest in list_guests:
        forties1 = guest.get("age")
        if 40 <= forties1 <= 49:
            forties += 1
    for guest in list_guests:
        fifties1 = guest.get("age")
        if 50 <= fifties1 <= 59:
            fifties += 1
    for guest in list_guests:
        sixties1 = guest.get("age")
        if 60 <= sixties1 <= 69:
            sixties += 1
    for guest in list_guests:
        seventies1 = guest.get("age")
        if 70 <= seventies1 <= 79:
            seventies += 1
    for guest in list_guests:
        eighties1 = guest.get("age")
        if 80 <= eighties1 <= 89:
            eighties += 1
    for guest in list_guests:
        nineties1 = guest.get("age")
        if 90 <= nineties1 <= 99:
            nineties += 1
    for guest in list_guests:
        centenarian1 = guest.get("age")
        if 100 <= centenarian1 <= 199:
            centenarian += 1
    if teens >= 1 and twenties >=1 and thirties >=1 and forties >=1 and fifties >=1 and sixties >=1 and seventies >=1 and eighties >=1 and nineties >=1 and centenarian >=1:
        return True
    else:
        return False




print(age_group(list1))