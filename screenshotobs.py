import pytesseract
import mss
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
from allsongsinphoenix import songs

def readtextfromimage(PATH):
    hold = str(pytesseract.image_to_string(Image.open(f"{PATH}")))
    hold = hold.split("\n")
    i=0
    while i != len(hold):
        if hold[i] in str(songs):
            song = hold[i]
            break
        else: 
            i+=1
    return song

def screenshotobs():
    f = open("settings.txt","r")
    screenres = f.readline()
    screenres = remove(screenres,"screen resolution=") 
    monitor = f.readline()
    monitor = int(remove(monitor,"screen="))
    print (monitor)
    print (screenres)
    return

def remove(string,remove):
    hold = str(string)
    hold = hold.replace(f"{remove}","")
    hold = hold.replace("\n","")
    return hold

if __name__ == "__main__":
    readtextfromimage("testimages/c9OYZy9pCB.png")