import curses
import zumo_soft as zumo
screen=curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
try:
    while True:
        char=screen.getch()
        if char==ord('q'):
            print("quitting...")
            zumo.stop()
            break
        elif char==curses.KEY_UP:
            print("up")
            zumo.forward()
        elif char==curses.KEY_DOWN:
            print("down")
            zumo.backward()
        elif char==curses.KEY_RIGHT:
            print("right")
            zumo.spin_acw()
        elif char==curses.KEY_LEFT:
            print("left")
            zumo.spin_cw()
        elif char==ord(' '):
            print("stop")
            zumo.stop()
        elif char==ord('d'):
            print("deccelerating")
            zumo.decelerate()
        elif char==ord('a'):
            print("accelerating")
            zumo.accelerate()
            

finally:
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
