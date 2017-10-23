import requests
from pytesseract import image_to_string
from PIL import Image
from bs4 import BeautifulSoup

# image = Image.open('')
# data = str(image_to_string(image))
# username = input("Enter name\t")
# password = input("Enter password\t")
url = 'https://christuniversity.in/StudentLogin.html'

session =requests.session()
# payload = {'userName':username, 'password':password, 'enteredCaptcha':data}
# r = session.post(url,data=payload)
rs = session.get(url)
soup = BeautifulSoup(rs.content,'html.parser')
print soup
# for link in soup.find_all('span'):
#     print link.text
# session.close()