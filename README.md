# devalore_project
#the prod environments

import requests

response = requests.get("http://api.exchangeratesapi.io/v1/latest?access_key=fa3b5e2d4e682ef6ba7a7b2bbf528bdb")
currency_name = response.json()["rates"]

sorted_values = sorted(currency_name.values()) # Sort the values
sorted_dict = {}

for i in sorted_values:
    for k in currency_name.keys():
        if currency_name[k] < 10:
            sorted_dict[k] = currency_name[k]

print(sorted_dict)

#test unit

import requests

response = requests.get("http://api.exchangeratesapi.io/v1/latest?access_key=fa3b5e2d4e682ef6ba7a7b2bbf528bdb")
currency_name = response.json()["rates"]

sorted_values = sorted(currency_name.values()) # Sort the values
sorted_dict = {}

for i in sorted_values:
    for k in currency_name.keys():
        if currency_name[k] < 10:
            sorted_dict[k] = currency_name[k]
#I took one key and check if its upper then 10 and one key lower then 10.            
    def test_prod():
        assert currency_name['AZN'] < 10

    def test_prod_1():
        assert currency_name['BAM'] > 10

print(sorted_dict)

#install docker and download jenkins image:

docker pull jenkins/jenkins
docker image inspect [image.ID] #in this info. we look for the exposed port to the jenkis service which is port 8080
docker run -d -p 80:8080 jenkins/jenkins #in this command the jenkins will run while it expose port 80.



