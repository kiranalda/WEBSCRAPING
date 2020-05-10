from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.gyanlakshmi.net/projects').text

soup = BeautifulSoup(source,'lxml')

div_main = soup.find('div' ,id='cm8ainlineContent-gridContainer')
#divs = soup.find_all('div' ,data-packed_='true')
#divs = soup.find('div' ,class_='txtNew')
#print(divs.prettify)
#div1 = soup.find('div' ,class_='txtNew')

divs = div_main.find_all('div' , {'class' : ['s_BIwzIGroupSkin','style-k9mxj942']})

for div in divs:
	#print(div.prettify)
	#print('-----------')
	title=div.find('div',class_='txtNew')
	if title not in [None]:
		print('Title :' +  title.h6.text)
	
	video=div.find_all('a')
	for a in video:
		if a.get('href') not in [None]:
			print('Video Link ::' + a.get('href'))
	#print(title)
	#print(video)
	
	#attr = div.find(attrs={'class':'s_BIwzIGroupSkin'})
	#print(attr)
	#if attr not in [None]:
	#	header = attr.find('h6',style_='font-size:12px')
		#print(header)
		#if header not in [None]:
			#print(header.text)
	#print(attr)
		

#title_div = div_main.find_all('div',class_='s_BIwzIGroupSkin')
#print(title_div.prettify)

		
	
	#div_1 = soup.find_all('div' ,data-packed_='true')
	#print(div.prettify)
	#header = div.find('h6',style_='font-size:12px')
	#if( div.h6.text != 'None'):
		#print(div.h6.text)
	#print('------------------------')
	#print(div.h6)
		
		#span=header.find('span' , style_='color:#000000;')
		#print(span)
		#print('Article::' + div.h6.text)
	#header=div.find('h6')
	#print(header)
	#print('------------')
	

