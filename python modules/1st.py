# there are 2 types of module in python 
# 1. built in Module 
# 2. external module 







import math
import os
import mymodule
import requests
print(math.sqrt(121))

mymodule.hello()

r= requests.get("https://www.google.com")

print(r.text)