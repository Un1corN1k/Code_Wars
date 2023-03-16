def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True


def minimum_number(numbers):
  suma = sum(numbers)
  while is_prime(suma) != True:
    suma = suma + 1
  print(suma)
  return suma - sum(numbers)


print(minimum_number([2,12,8,4,6]))