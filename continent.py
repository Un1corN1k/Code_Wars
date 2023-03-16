
list1 =  [
  { 'firstName': 'Fatima', 'lastName': 'A.', 'country': 'Algeria', 'continent': 'Africa', 'age': 25, 'language': 'JavaScript' },
  { 'firstName': 'Agustín', 'lastName': 'M.', 'country': 'Chile', 'continent': 'Americas', 'age': 37, 'language': 'C' },
  { 'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia', 'age': 39, 'language': 'Ruby' },
  { 'firstName': 'Laia', 'lastName': 'P.', 'country': 'Andorra', 'continent': 'Europe', 'age': 55, 'language': 'Ruby' },
  { 'firstName': 'Oliver', 'lastName': 'Q.', 'country': 'Australia', 'continent': 'Oceania', 'age': 65, 'language': 'PHP' }
  ]

list2 = [
        { 'firstName': 'Fatima', 'lastName': 'A.', 'country': 'Algeria', 'continent': 'Africa', 'age': 25, 'language': 'JavaScript' }
        ]


def all_continents(lst):
    Africa = 0
    Americas = 0
    Asia = 0
    Europe = 0
    Oceania = 0
    for cont in lst:
        if cont.get("continent") == "Africa":
            Africa += 1
        if cont.get("continent") == "Americas":
            Americas += 1
        if cont.get("continent") == "Asia":
            Asia += 1
        if cont.get("continent") == "Europe":
            Europe += 1
        if cont.get("continent") == "Oceania":
            Oceania += 1
    if Africa >=1 and Americas >=1 and Asia >=1 and Europe >=1 and Oceania >=1:
        return True
    else:
        return False


#def all_continents(lst):
#   return set(['Africa', 'Americas', 'Asia', 'Europe', 'Oceania']) == set([el['continent'] for el in lst])


print(all_continents(list2))