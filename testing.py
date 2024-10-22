# on cloud9 run pip install requests to fetch the library

import requests
import time

url = 'https://x9zx73tiy4.execute-api.us-east-1.amazonaws.com/prod/unicorns'

obj1 = '{"Name": "JohnDoe","Weight": 100}'
obj2 = '{"Name": "Bucefalos","Weight": 65}'
obj3 = '{"Name": "Goldilax","Weight": 45}'
obj4 = '{"Name": "Redmalicious","Weight": 55}'
obj5 = '{"Name": "Pegasina","Weight": 30}'


x = requests.post(url, data=obj1)
print(x, x.elapsed.total_seconds())
# x = requests.post(url, data = obj2)
# print(x, x.elapsed.total_seconds())
# x = requests.post(url, data = obj3)
# print(x)
# x = requests.post(url, data = obj4)
# print(x)
# x = requests.post(url, data = obj5)
# print(x)
