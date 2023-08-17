
#for location

import requests
from tkinter.messagebox import * 
data=None
location=None
temp=None
city=None
try:
	wa="https://ipinfo.io/"
	res=requests.get(wa)
	#print(res)
	data=res.json()
	

except  ConnectionError: 
	location='Not Available'
except requests.exceptions.RequestException as e:
	location='Not Available'
except Exception as e:
	print("Some issue1",e)
else:
	location=data['city']+','+data['region']
	#print(location)


#for Temperature

try:
	city=data['city']
	a1='http://api.openweathermap.org/data/2.5/weather?units=metric'
	a2="&q= "+data['city']
	a3="&appid="+"b3410e614690b8f541c5419fe82d8646"

	web=a1+a2+a3
	res1=requests.get(web)
	#print(res1)
	#data1=res1.json()
	#print(data1)
	
	#temp=data1['main']['temp']
except ConnectionError:
	temp='N/A'
except TypeError:
	temp='N/A'
except requests.exceptions.RequestException as e:
	temp='N/A'
except Exception as e:
	print("Some issue2",e)

else:
	data1=res1.json()
	#print(data1)
	temp1=data1['main']['temp']
	temp=temp1
#for quotes

import bs4


try:
	w="https://www.brainyquote.com/quote_of_the_day"
	res=requests.get(w)	
	#print(res)
	data=bs4.BeautifulSoup(res.text,'html.parser')
	info=data.find('img',{'class' :'p-qotd'})
	msg=info['alt']
	#print(msg)
except ConnectionError:
	msg='World is a Beautiful Place'
except requests.exceptions.RequestException as e:
	msg='World is a beautiful Place'
except Exception as e:
	print(e)

