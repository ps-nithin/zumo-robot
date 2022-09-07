import curses
import zumo
screen=curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

try:
    while True:
        char=screen.getch()
        if char==ord('q'):
            break
        elif char==curses.KEY_UP:
            print("up")
            zumo.forward(255)
        elif char==curses.KEY_DOWN:
            print("down")
            zumo.backward(255)
        elif char==curses.KEY_RIGHT:
            print("right")
            zumo.spin_acw(255)
        elif char==curses.KEY_LEFT:
            print("left")
            zumo.spin_cw(255)
        elif char==ord(' '):
            print("stop")
            zumo.stop()

finally:
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
