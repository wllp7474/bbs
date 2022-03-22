from django.test import TestCase

# Create your tests here.



import datetime

now=datetime.datetime.now().strftime("%Y-%m-%d")

print(now)
print(type(now))


import json

json.dumps(now)