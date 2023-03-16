# https://www.codewars.com/kata/5827bc50f524dd029d0005f2/solutions/python

list1 = [
  { "first_name": "Mark", "last_name": "G.", "country": "Scotland", "continent": "Europe", "age": 22, "language": "JavaScript" },
  { "first_name": "Victoria", "last_name": "T.", "country": "Puerto Rico", "continent": "Americas", "age": 30, "language": "Python" },
  { "first_name": "Emma", "last_name": "B.", "country": "Norway", "continent": "Europe", "age": 19, "language": "Clojure" },
{ "first_name": "Victoria", "last_name": "T.", "country": "Puerto Rico", "continent": "Americas", "age": 30, "language": "Python" },
]


def get_first_python(list_users):
    result = ''
    for user in list_users:
        lang_pr = user.get("language")
        if lang_pr == "Python":
            result += user.get("first_name")
            result += ", "
            result += user.get("country")
            break
    if result == "":
        result += "There will be no Python developers"
    return result

print(get_first_python(list1))
