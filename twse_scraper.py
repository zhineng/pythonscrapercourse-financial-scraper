import requests
import json

response = requests.get(
    'https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=json&date=20220517&selectType=30&_=1652803509494')

print(response.json()['data'])
