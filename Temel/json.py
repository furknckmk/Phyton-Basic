# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 23:34:35 2021

@author: MMFH V.3
"""
import json

data = '{"firstName":"Furkan","lastName":"Cakmak"}'

y = json.loads(data)

print(y["firstName"])
print(y["lastName"])

customer = {
    "firstName":"Furkan",
    "email":"furkancakmak31@gmail.com"
    }
customerJson = json.dumps(customer)
print(customer)

print(json.dumps("Furkan"))