from selenium import webdriver
import matplotlib.pyplot as plt
import pandas as pds
import numpy as np
import csv
import  json

url = "https://www.daraz.com.bd/catalog/?spm=a2a0e.home.search.1.735212f7rB5wpJ&q=laptop&_keyori=ss&clickTrackInfo=textId--8604400042594750176__abId--300705__pvid--6285551b-8ea9-406c-8050-6dc7a7520391__matchType--1__srcQuery--laptop__spellQuery--laptop&from=suggest_normal&sugg=laptop_0_1"
driver = webdriver.Chrome(executable_path=r'C:\Users\coder\Downloads\chromedriver_win32 (1)\chromedriver.exe')
driver.get(url)
p_name = []
p_price =[]
p_dict = {}
for i in range(1,11):
    pName=driver.find_element("xpath",'//*[@id="root"]/div/div[2]/div/div/div[1]/div[2]/div['+str(i)+']/div/div/div[2]/div[2]/a').text
    p_name.append(pName)
    pPrice = driver.find_element("xpath",'//*[@id="root"]/div/div[2]/div/div/div[1]/div[2]/div['+str(i)+']/div/div/div[2]/div[3]/span').text
    p_price.append(pPrice)

for name in p_name:
    name=name.split()[:2]
    name=' '.join(name)
    for price in p_price:
        price=price.replace(',','')
        price=price.replace('৳','')
        price=float(price)
        p_dict[name] = price

twoWrdPname = []
for i in p_name:
    i=((i.split())[:2])
    i = ' '.join(i)
    twoWrdPname.append(i)


#
for i in range(len(p_price)):
    p_price[i] = p_price[i].replace('৳','')
    p_price[i] = p_price[i].replace(',','')
    p_price[i] = float(p_price[i])

p_dict = json.dumps(p_dict,indent=2)
print(p_dict)

dataset = {
    "product":twoWrdPname,
    "price":p_price
}
df = pds.DataFrame(dataset)
x= np.array(twoWrdPname)
y = np.array(p_price)
plt.bar(x,y)
plt.show()

# for save to cvs format
df.to_csv('product.csv')
print("saved your CSV file!")
