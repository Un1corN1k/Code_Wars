# https://www.codewars.com/kata/583a8bde28019d615a000035/solutions/python


def len(list_name):
    dict_name = []
    for name in list_name:
        sum_name = sum(ord(i) for i in name['firstName'])
        if sum_name % 2:
            dict_name.append(name)
    return dict_name


list1 = [
    { 'firstName': 'Daniel', 'lastName': 'J.', 'country': 'Aruba', 'continent': 'Americas', 'age': 42, 'language': 'Python' },
    { 'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 22, 'language': 'Ruby' },
    { 'firstName': 'Sou', 'lastName': 'B.', 'country': 'Japan', 'continent': 'Asia', 'age': 43, 'language': 'Ruby' },
    { 'firstName': 'Hanna', 'lastName': 'L.', 'country': 'Hungary', 'continent': 'Europe', 'age': 95, 'language': 'JavaScript' },
    { 'firstName': 'Jayden', 'lastName': 'P.', 'country': 'Jamaica', 'continent': 'Americas', 'age': 18, 'language': 'JavaScript' },
    { 'firstName': 'Joao', 'lastName': 'D.', 'country': 'Portugal', 'continent': 'Europe', 'age': 25, 'language': 'JavaScript' }
    ]

# a = "A"
# print (ord(a))

print(len(list1))