# Program to check availability of product on shopping sites 

import requests
from bs4 import BeautifulSoup
import time
import webbrowser
import winsound

def checkavailability(website_name , url):

	headers= { "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
	page = requests.get (url, headers=headers)
	soup = BeautifulSoup(page.content, 'html.parser')

	if website_name=='amazon':
		avail = soup.find(id="priceblock_ourprice")
		if avail != None :
			print ("product is available")

			webbrowser.open(url)

		else :
			print ("product is not available")

	elif website_name=='flipkart':
		avail = soup.find(id="pincodeInputId")
		if avail != None :

			print ("product is available")
			
			webbrowser.open(url)
			duration = 10000  # milliseconds
			freq = 440  # Hz
			winsound.Beep(freq, duration) #Beep to alert when product is available
	
		else :
			print ("product is not available")
'''
 to call checkavailability function pass two argument first with 
 website name (like 'amazon'and 'filpkart') and second with the url of the product 
'''
while True :
	checkavailability('(flipkart/amazon)','[[LINK]]')
	time.sleep(10)  
