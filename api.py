import requests as r
import os

WCI_KEY = os.environ.get('WORLDCOININDEX_KEY')

def getEthPriceInUsd ():
    api_req_str = 'https://www.worldcoinindex.com/apiservice/json?key='+ WCI_KEY
    res = r.get(api_req_str)
    for market in res.json()['Markets']:
        if market['Name'] == 'Ethereum':
            return market['Price_usd']
