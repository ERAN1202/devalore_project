'''import pytest

def func(x):
    return x + 1


def test_answer():
    assert func(4) == 5

'''

import requests

response = requests.get("http://api.exchangeratesapi.io/v1/latest?access_key=fa3b5e2d4e682ef6ba7a7b2bbf528bdb")
currency_name = response.json()["rates"]

sorted_values = sorted(currency_name.values()) # Sort the values
sorted_dict = {}

for i in sorted_values:
    for k in currency_name.keys():
        if currency_name[k] < 10:
            sorted_dict[k] = currency_name[k]


    def test_prod():
        assert currency_name['AZN'] < 10

    def test_prod_1():
        assert currency_name['BAM'] > 10


print(sorted_dict)












