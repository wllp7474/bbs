# from django.test import TestCase
#
# # Create your tests here.
#
#
#
# import datetime
#
# now=datetime.datetime.now().strftime("%Y-%m-%d")
#
# print(now)
# print(type(now))
#
#
# import json
#
# json.dumps(now)



stored_results = {1:"dasdas",2:"dasaffg"}
def sum_to_n(n):
    result = 0
    for i in reversed(range(n)):
        if i + 1 in stored_results:
            print('Stopping sum at % s because we have previously computed it' % str(i + 1))
            result += stored_results[i + 1]
            break
        else:
            result += i + 1
            stored_results[n] = result
            return result

# sum_to_n(1)