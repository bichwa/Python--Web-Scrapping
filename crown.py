#Web Scrapping using Python 3.5 
#Credits goes to chris reeves: https://github.com/creeveshft
#Author:  @rickarani: https://github.com/bichwa/

import urllib.request

urls = ["http://google.com","http://cnn.com","http://bean.co.ke"]

i =0
while i < len(urls):
	htmlfile = urllib.request.urlopen(urls[i])
	htmltext = htmlfile.read()

	print (htmltext)
	i+=1


