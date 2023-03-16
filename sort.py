# https://www.codewars.com/kata/583ea278c68d96a5fd000abd/train/python
import pandas as pd

arr = [
  {"first_name": "Nikau", "last_name": "R.", "country": "New Zealand", "continent": "Oceania", "age": 39,
   "language": "Ruby" },
  {"first_name": "Maria", "last_name": "S.", "country": "Peru", "continent": "Americas", "age": 30,
   "language": "C" },
  {"first_name": "Agustin", "last_name": "V.", "country": "Uruguay", "continent": "Americas", "age": 19,
   "language": "JavaScript" },
  {"first_name": "Agustin", "last_name": "V.", "country": "Uruguay", "continent": "Americas", "age": 19,
     "language": "JavaScript"},
{"first_name": "Maria", "last_name": "S.", "country": "Peru", "continent": "Americas", "age": 30,
     "language": "C"},
]

# df = pd.DataFrame(arr)
# print(df.sort_values("language"))
def sort_arr(arr):
    result = sorted(arr, key=lambda item: (item["language"], item["first_name"]))
    return result
print(sort_arr(arr))