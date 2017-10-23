 import cv2
import numpy as np
import pytesseract
from PIL import Image
import os

# Path of working folder on Disk
src_path = "/Users/praniel1/Desktop/all_files/development/python_programs/Image_Recognition/"

def get_string(img_path):
    # Read image with opencv
    img = cv2.imread(img_path)

    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # Write image after removed noise
    cv2.imwrite("removed_noise.png", img)

    #  Apply threshold to get image with only black and white
    #img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    # Write the image after apply opencv to do some ...
    cv2.imwrite("thres.png", img)

    thres = src_path + "thres.png"
    # Recognize text with tesseract for python
    result = pytesseract.image_to_string (Image.open(img_path))

    # Remove template file
    #os.remove(temp)
    return result

i = raw_input("Enter the name:\t")
i = i.strip()
print i
print "--- Start recognize text from image ---"
data = get_string(i)
print data
file = open('parsing.txt', 'w')
file.write(data)
print "------ Done -------"
