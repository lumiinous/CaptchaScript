from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
import cv2
import numpy as np
import pytesseract
import time
import base64
import io
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

def data_uri_to_cv2_img(uri):
    encoded_data = uri.split(',')[1]
    nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img

def getCaptcha():
    #get cropped image of Captcha
    driver.get('http://challenge01.root-me.org/programmation/ch8/')
    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")
    final = soup.find("img")
    image = data_uri_to_cv2_img(final['src'])


    #Noise removal
    image[np.where ((image==[0,0,0]).all(axis=2))]=[255,255,255]
    image[np.where ((image!=[255,255,255]).all(axis=2))]=[0,0,0]
    blur = cv2.GaussianBlur(image,(3,3),0)


    #OCR
    text=pytesseract.image_to_string(blur)

    #insert text
    input_text = driver.find_element(By.NAME,"cametu")
    input_text.send_keys(text)


def testHitRate():
    i=0
    success=0
    while i<100:
        getCaptcha()
        content = driver.page_source
        soup = BeautifulSoup(content, features="html.parser")
        para=soup.find('p')
        if str(para)=="<p>Failed, Try again.<br/></p>":
            #print("failed")
            pass
        else:
            success=success+1
        i=i+1
        print(i)

    print("Success rate: "+str(success/i*100) +"%")
    driver.quit()

def main():
    while True:
        getCaptcha()
        content = driver.page_source
        soup = BeautifulSoup(content, features="html.parser")
        para=soup.find('p')
        if str(para)=="<p>Failed, Try again.<br/></p>":
            pass
        else:
            break

main()

#testHitRate()

