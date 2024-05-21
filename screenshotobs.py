import pytesseract
import mss
import mss.tools
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
from allsongsinphoenix import similarity
from os import remove

def readtextfromimage(PATH,SEARCH_FOR_SONG=True):
    hold = str(pytesseract.image_to_string(Image.open(f"{PATH}")))
    hold = hold.split("\n")
    i=0
    x=0
    if SEARCH_FOR_SONG == True:
        while i != len(hold):
    #        if hold[i] in songs[x]:
    #            song = hold[i]
    #            break
    #        else: 
    #            x+=1
    #            if x == len(songs):
    #                i+=1
    #                x=0
            song = similarity(hold[i])
            if song == None:
                i+=1
            else:
                song == None
                break
    if SEARCH_FOR_SONG == False:
        song = hold
    return song

def screenshotobs():
    f = open("settings.txt","r")
    screenres = f.readline()
    screenres = remove(screenres,"screen resolution=") 
    monitor = f.readline()
    monitor = int(remove(monitor,"screen="))
    f.close()
    if screenres == "1080":
        with mss.mss() as sct:
            filename = sct.shot(mon=monitor,output="temp.png")
            print (filename)
    print (monitor)
    print (screenres)
    return filename,monitor,screenres

def getscore(resolution,monitor):
    try:
        remove("name.png")
        remove("plate.png")
        remove("score.png")
    except:
        pass
    if resolution == "1080":
        with mss.mss() as sct:
            mon = sct.monitors[int(monitor)]
            monitorinfo = {
                "top":mon["top"]+200,
                "left":mon["left"] + 420,
                "width":250,
                "height":125,
                "mon":int(monitor)
            }
            output = "score.png"

            sct_img = sct.grab(monitorinfo)

            mss.tools.to_png(sct_img.rgb, sct_img.size,output=output)
    return output 

def getsongname(resolution,monitor):
    if resolution == "1080":
        with mss.mss() as sct:
            mon = sct.monitors[int(monitor)]
            monitorinfo = {
                "top":mon["top"]+142,
                "left":mon["left"] + 713,
                "width":400,
                "height":80,
                "mon":int(monitor)
            }
            output = "name.png"

            sct_img = sct.grab(monitorinfo)

            mss.tools.to_png(sct_img.rgb,sct_img.size,output=output)
    return output

def getplate(resolution,monitor):
    if resolution == "1080":
        with mss.mss() as sct:
            mon = sct.monitors[int(monitor)]
            monitorinfo = {
                "top":mon["top"]+430,
                "left":mon["left"] + 459,
                "width":200,
                "height":90,
                "mon":int(monitor)
            }
            output = "plate.png"

            sct_img = sct.grab(monitorinfo)

            mss.tools.to_png(sct_img.rgb,sct_img.size,output=output)
    return output

def readsettings():
    f = open("settings.txt","r")
    screenres = f.readline()
    screenres = remove(screenres,"screen resolution=") 
    monitor = f.readline()
    monitor = int(remove(monitor,"screen="))
    auth = f.readline()
    auth = remove(auth,"Authorization Header=")
    f.close()
    return monitor,screenres, auth

def remove(string,remove):
    hold = str(string)
    hold = hold.replace(f"{remove}","")
    hold = hold.replace("\n","")
    return hold

if __name__ == "__main__":
    #song = readtextfromimage("testimages/c9OYZy9pCB.png")
    #print (song)
    getscore("1080",1)
    getsongname("1080",1)
    getplate("1080",1)
