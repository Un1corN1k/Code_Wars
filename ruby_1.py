# https://www.codewars.com/kata/5827acd5f524dd029d0005a4

list1 = [
    { 'firstName': 'Sofia', 'lastName': 'I.', 'country': 'Argentina', 'continent': 'Americas', 'age': 35, 'language': 'Java' },
    { 'firstName': 'Lukas', 'lastName': 'X.', 'country': 'Croatia', 'continent': 'Europe', 'age': 35, 'language': 'Python' },
    { 'firstName': 'Madison', 'lastName': 'U.', 'country': 'United States', 'continent': 'Americas', 'age': 32, 'language': 'Ruby' }
    ]


def is_ruby_coming(lst):
    ruby = 0
    for dev in lst:
        developer = dev.get("language")
        if developer == "Ruby":
            ruby += 1
    if ruby >= 1:
        return True
    else:
        return False


print(is_ruby_coming(list1))