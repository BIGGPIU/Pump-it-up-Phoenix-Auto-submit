import curses
from curses import wrapper 
from screenshotobs import *
from piuscores import POST
from time import sleep

def main(stdscr):
    stdscr.clear()
    monitor,res,auth = readsettings()


    
    z=1 
    while True:
        sleep(1)
        scorepath = getscore(res,monitor)
        songpath = getsongname(res,monitor)
        platepath = getplate(res,monitor)
        score = readtextfromimage(scorepath,False)
        song = readtextfromimage(songpath)
        plate = readtextfromimage(platepath,False)
        if song == None:
            stdscr.clear()
            if z == 1:
                stdscr.addstr("Searching for Clear.")
                z+=1
            elif z == 2:
                stdscr.addstr("Searching for Clear..")
                z+=1
            elif z==3:
                stdscr.addstr("Searching for Clear...")
                z=1
            stdscr.refresh()
        if song != None:
            stdscr.clear()
            stdscr.refresh()
            stdscr.addstr(0,0,f"New Clear!!")
            stdscr.addstr(1,0,f"{song}")
            stdscr.addstr(2,0,f"Score: {score[0]}")
            stdscr.addstr(3,0,f"Plate: {plate[0]} GAME")
            stdscr.addstr(4,0,"What difficulty did you play?") #EXAMPLE FORMAT: "S21"
            stdscr.addstr(5,0,"")
            hold = []
            x=0
            while len(hold) != 3:
                stdscr.refresh()
                temp = stdscr.getkey()
                if len(temp) != 1:
                    pass
                else:
                    hold.append(temp)
                    stdscr.addstr(5,x,f"{temp}")
                    stdscr.refresh()
                    x+=1
            sleep(1)
            stdscr.clear()
            stdscr.refresh()
            stdscr.addstr(0,0,f"New Clear!!")
            stdscr.addstr(1,0,f"{song}")
            stdscr.addstr(2,0,f"Score: {score[0]}")
            stdscr.addstr(3,0,f"Plate: {plate[0]} GAME")
            stdscr.addstr(4,0,"Would you like to submit this play? y/n") #EXAMPLE FORMAT: "S21"
            stdscr.addstr(5,0,"")
            temp2 = []
            while len(temp2)  != 1:
                usrinput = stdscr.getkey() #OK I want to get this out fast so im not gonna check if they actually cleared or not lets go with the honor system for now
                if usrinput == "y":
                    hold2 = POST(hold[0],f"{hold[1]}{hold[2]}",song,score[0],plate[0],auth)
                    stdscr.clear()
                    stdscr.addstr(0,0,f"{hold2}")
                    stdscr.refresh()
                    sleep(5)
                if usrinput == "n":
                    sleep(5)


                



if __name__ == "__main__":
    wrapper(main)