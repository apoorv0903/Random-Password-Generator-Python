import random

ucase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lcase_letters = ucase_letters.lower()
specialChar = "!@#$%^&*()_+=-}{][;:,"
digits = "0123456789"

include_upper, include_lower, include_numeric, include_symbol = True, True, True, True

all = ""

if include_upper: 
    all += ucase_letters

if include_lower:
    all += lcase_letters

if include_numeric:
    all += digits

if include_symbol:
    all += specialChar

lengthOfPassword = 10
totalNumberOfPassword = 5

for x in range(totalNumberOfPassword):
    password = "".join(random.sample(all, lengthOfPassword))
    print(password)
    
