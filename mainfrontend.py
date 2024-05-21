import curses
from curses import wrapper 
from screenshotobs import *

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
            stdscr.refresh()

            

    return


if __name__ == "__main__":
    wrapper(main)