import requests
from bs4 import BeautifulSoup

print("\n*************************************")
print("\tProduct Price Checker")
print("*************************************\n")

url = input("Enter the Link of the Product : \n")
raw = requests.get(url)
data = raw.content

soup = BeautifulSoup(data, 'html.parser')

item = soup.find(class_='B_NuCI').text
cost = soup.find(class_='_3I9_wc _2p6lqe').text
price = soup.find(class_='_30jeq3 _16Jk6d').text
rating = soup.find(class_='_3LWZlK').text

print(f"\nName of Product : {item}")
print(f"Ratings : {rating}")
print(f"Cost Price of Product : {cost}")
print(f"Selling Price of Product : {price}")
# discount = (((int(cost)-int(price))/int(cost))*100)
cp = cost.replace('₹','').replace(',','')
sp = price.replace('₹','').replace(',','')
discount = (((int(cp)-int(sp))/int(cp))*100)
discount = round(discount)
print(f"Discount Percetage : {discount}%")
