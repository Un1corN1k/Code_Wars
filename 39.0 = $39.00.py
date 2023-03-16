# https://www.codewars.com/kata/55902c5eaa8069a5b4000083/solutions/python
def format_money(amount):
    return '$' + f'{"%.2f" % amount}'

print(format_money(39.0))
