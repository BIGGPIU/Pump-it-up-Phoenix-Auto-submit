import curses
from curses import wrapper 
from screenshotobs import *
from piuscores import POST
from time import sleep

def main(stdscr):
    stdscr.clear()
    monitor,res = readsettings()




    while True:
        sleep(1)
        scorepath = getscore(res,monitor)
        songpath = getsongname(res,monitor)
        platepath = getplate(res,monitor)
        score = readtextfromimage(scorepath,False)
        song = readtextfromimage(songpath)
        plate = readtextfromimage(platepath,False)
        if song == None:
            pass
        if song != None:
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
            usrinput = stdscr.getkey()
            if usrinput == "y":
                POST(hold[0],f"{hold[1]}{hold[2]}",song,score[0],plate[0])


            

    return


if __name__ == "__main__":
    wrapper(main)