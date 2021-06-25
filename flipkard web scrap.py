import soupsieve.css_parser
from bs4 import BeautifulSoup
import requests
import pandas as p

product=[]
prices=[]
ratings=[]
req=requests.get("https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&as-pos=1&as-type=RECENT&suggestionId=laptop%7CLaptops&requestId=21a665be-cec5-42b0-841b-4f461d31ffcb&as-backfill=on")
soup=BeautifulSoup(req.content,"html.parser")
# product=soup.find('div',attrs={'class':'_4rR01T'})
# print(product.text)

for a in soup.findAll('a',href=True,attrs={'class':'_1fQZEK'}):
    name=a.find('div',attrs={'class':'_4rR01T'})
    price=a.find('div',attrs={'class':'_30jeq3 _1_WHN1'})
    rating=a.find('div',attrs={'class':'_3LWZlK'})
    product.append(name)
    prices.append(price)
    ratings.append(rating)

df=p.DataFrame({"Product Name":product,"Price":prices,"Rating":ratings})
print(df.to_csv("product.csv"))
