#Web Scrapping using Python 3.5 
#Credits goes to chris reeves: https://github.com/creeveshft
#Author:  @rickarani: https://github.com/bichwa/

import urllib.request

urls = ["http://google.com","cnn.com","bean.co.ke"]

htmltext = urllib.request.urlopen("http://google.com").read()

print (htmltext)
