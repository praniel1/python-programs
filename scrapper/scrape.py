import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings()
url = "https://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=Los+Angeles%2C+CA"
r = requests.get(url, verify=False)
soup = BeautifulSoup(r.content,'html.parser')
g_data = soup.find_all("div", {"class":"info"})

for item in g_data:
    print item.contents[0].find_all("a",{"class":"business-name"})[0].text
    print item.contents[1].find_all("p",{"class":"adr"})[0].text
    try:
        print item.contents[1].find_all("div",{"class":"primary"})[0].text
    except:
        pass
    print ("")