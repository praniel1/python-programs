from pytesseract import image_to_string
from PIL import Image

i = raw_input("Enter the name:\t")
i = i.strip()
print i
image = Image.open(i)
data = str(image_to_string(image))
print data
file = open('parsing.txt', 'w')
file.write(data)
file.close()