from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Title', 'Price', 'Stock Availability'])

source = requests.get('http://books.toscrape.com/').text

soup = BeautifulSoup(source,'lxml')

section = soup.find('div',class_='col-sm-8 col-md-9').find('section')

#print(section.prettify)

articles=section.find_all('article')

for article in articles:
    #print(article.prettify)
    print('----------------------------')
    print('TITLE::' + article.h3.text)
    title = article.h3.text
    try:
        product = article.find('div' , class_='product_price')
        price = product.find('p' , class_='price_color')
        stock = product.find('p' , class_='instock availability')
        try:
            prc = price.text
            stck = stock.text.strip()
            print('PRICE::' + price.text)
            print('STOCK AVAILABILITY:: ' + stock.text.strip())
        except:
            price=None
            stock = None
    except:
        product = None
		
    csv_writer.writerow([title,prc,stck])
    
        
	