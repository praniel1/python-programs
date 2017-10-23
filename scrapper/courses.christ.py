import requests
from bs4 import BeautifulSoup
url = 'http://courses.christuniversity.in/login/index.php'
usrname = input("Enter user name  ")
pswrd = input("ENter password  ")
session = requests.session()
payload = {'username': usrname, 'password': pswrd}
r = session.post(url, data=payload)
rs = session.get('http://courses.christuniversity.in/my/')
soup = BeautifulSoup(rs.content,'html.parser')
for link in soup.find_all('h1'):
    print link.text
session.close()