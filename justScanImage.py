import time
from telnetlib import EC

import pytesseract as tess
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import asyncio
import requests
import cloudscraper
import re


tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image
import requests
from selenium import webdriver

# driver_path = "C:\seleniumm\chromedriver"
# browser = webdriver.Chrome(executable_path=driver_path)
# browser.maximize_window()


def yaziOku(adres,deger):
    #img = Image.open("z1.jpg")
    url = adres
    #print(url)

    scraper = cloudscraper.create_scraper()
    resim = scraper.get(url).text
    # print (scraper.get("https://prnt.sc/17qiszb").text)
    result = re.search(r'screenshot-image" src="(.+?)\"', resim)
    resimAdresi = result.group(1)
    if resimAdresi.find("prntscr.com") == -1 and resimAdresi.find("imageshack.us") == -1:

        #browser.get(url)
        #browser.get_screenshot_as_file("ekrangoruntusu/screenshot.png")
        #time.sleep(0.5)
        img = Image.open(requests.get(resimAdresi, stream=True).raw)
        #img = Image.open("ekrangoruntusu/screenshot.png")
        text = tess.image_to_string(img)


        #["user","login","pass","sifre","admin","root","mail"]
        if str(text).find("user") != -1:
            print("var 1")
            img.save("resimler/" + str(deger) + ".png")
        elif str(text).find("login") != -1:
            print("var 2")
            img.save("resimler/" + str(deger) + ".png")
        elif str(text).find("pass") != -1:
            print("var3 ")
            img.save("resimler/" + str(deger) + ".png")
        elif str(text).find("sifre") != -1:
            print("var4 ")
            img.save("resimler/" + str(deger) + ".png")
        elif str(text).find("admin") != -1:
            print("var5")
            img.save("resimler/" + str(deger) + ".png")
        elif str(text).find("mail") != -1:
            print("var6")
            img.save("resimler/" + str(deger) + ".png")
        elif str(text).find("root") != -1:
            print("var7")
            img.save("resimler/" + str(deger) + ".png")
        elif str(text).find("key") != -1:
            print("var7")
            img.save("resimler/" + str(deger) + ".png")
        elif str(text).find("secret") != -1:
            print("var7")
            img.save("resimler/" + str(deger) + ".png")
        elif str(text).find("domain") != -1:
            print("var7")
            img.save("resimler/" + str(deger) + ".png")
    return 0

def karakterDon1():
    liste = [ "a","b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","0","1","2","3","4","5","6","7","8","9"]
    deger = 0
    for a in liste:
        print("https://prnt.sc/" + str(a))
        yaziOku("https://prnt.sc/"+str(a),"1Karakter-"+str(deger))
        deger = deger+1

def karakterDon2():
    liste = [ "a","b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","0","1","2","3","4","5","6","7","8","9"]
    deger = 0
    for a in liste:
        for b in liste:
            print("https://prnt.sc/" + str(a)+str(b))
            yaziOku("https://prnt.sc/"+str(a)+str(b),"2Karakter-"+str(deger))
            deger = deger+1

def karakterDon3():
    liste = [ "a","b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","0","1","2","3","4","5","6","7","8","9"]
    deger = 0
    for a in liste:
        for b in liste:
            for c in liste:
                print("https://prnt.sc/" + str(a)+str(b)+str(c))
                yaziOku("https://prnt.sc/"+str(a)+str(b)+str(c),"3Karakter-"+str(deger))
                deger = deger+1

def karakterDon4():
    liste = [ "a","b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","0","1","2","3","4","5","6","7","8","9"]
    deger = 0
    for a in liste:
        for b in liste:
            for c in liste:
                for d in liste:
                    print("https://prnt.sc/" + str(a)+str(b)+str(c)+str(d))
                    yaziOku("https://prnt.sc/"+str(a)+str(b)+str(c)+str(d),"4Karakter-"+str(deger))
                    deger = deger+1

def karakterDon5():
    liste = [ "a","b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","0","1","2","3","4","5","6","7","8","9"]
    deger = 0
    for a in liste:
        for b in liste:
            for c in liste:
                for d in liste:
                    for e in liste:
                        print("https://prnt.sc/" + str(a)+str(b)+str(c)+str(d)+str(e))
                        yaziOku("https://prnt.sc/"+str(a)+str(b)+str(c)+str(d)+str(e),"5Karakter-"+str(deger))
                        deger = deger+1

def karakterDon6():
    liste = [ "a","b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","0","1","2","3","4","5","6","7","8","9"]
    deger = 0
    for a in liste:
        for b in liste:
            for c in liste:
                for d in liste:
                    for e in liste:
                        for f in liste:
                            print("https://prnt.sc/" + str(a)+str(b)+str(c)+str(d)+str(e)+str(f))
                            yaziOku("https://prnt.sc/"+str(a)+str(b)+str(c)+str(d)+str(e)+str(f),"6Karakter-"+str(deger))
                            deger = deger+1

def karakterDon7():
    liste = [ "a","b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","0","1","2","3","4","5","6","7","8","9"]
    deger = 0
    for a in liste:
        for b in liste:
            for c in liste:
                for d in liste:
                    for e in liste:
                        for f in liste:
                            for g in liste:
                                print("https://prnt.sc/" + str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g))
                                yaziOku("https://prnt.sc/"+str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g),"7Karakter-"+str(deger))
                                deger = deger+1

karakterDon5()
# karakterDon6()
# karakterDon7()

#https://prnt.sc/saaad

#print(yaziOku("https://prnt.sc/saaad","aaaa"))
