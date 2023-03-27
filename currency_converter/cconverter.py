import requests
import json

currency_code = input().lower()
r = requests.get('http://www.floatrates.com/daily/' + currency_code + '.json').json()
cache = {}

for code in r:
    if code == 'usd' or code == 'eur':
        cache[code] = r[code]

while True:
    currency_trans = input().lower()
    if currency_trans == '':
        break
    num = float(input())
    print("Checking the cache...")
    if currency_trans in cache:
        print("Oh! It is in the cache!")
        print(f"You received {cache[currency_trans]['rate'] * num:.2f} {currency_trans.upper()}.")
    else:
        print("Sorry, but it is not in the cache!")
        cache[currency_trans] = r[currency_trans]
        print(f"You received {cache[currency_trans]['rate'] * num:.2f} {currency_trans.upper()}.")
