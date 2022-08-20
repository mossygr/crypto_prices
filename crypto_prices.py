from re import X
import requests
from bs4 import BeautifulSoup

crypto_list = ["bitcoin","solana","cardano"]
crypto_urls = []
crypto_prices = []
final = {}

for x in crypto_list:
    url = "https://www.coindesk.com/price/%s" % (x)
    crypto_urls.append(url)

def get_prices():
    for i in crypto_urls:
        req = requests.get(i)
        soup = BeautifulSoup(req.content, 'html.parser')
        temp = soup.find('div', {"class" : "jwYVXk"}).text
        crypto_prices.append(temp)

get_prices()
final = dict(zip(crypto_list, crypto_prices))

print (final)