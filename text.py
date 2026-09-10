import os, time, cursor, threading, textwrap, extra

def clear():
    extra.clear()
def readline(file="", line=1):
    """Reads one line of a file"""
    line -= 1
    try:
        with open(file) as f:
            data = f.readlines()
            return data[line].replace("\n", "")
    except: return "error"

size = os.get_terminal_size()
class terminal:
    width = size.columns

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "x", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "X", "T", "U", "V", "W", "X", "Y", "Z", ' ']

def text(msg="", msgSpeed=0, cont=False, clear='none'):
    """All-purpose text thing."""
    size = os.get_terminal_size()
    msg = textwrap.fill(msg, size.columns, fix_sentence_endings=True, drop_whitespace=False)
    # msg = r'{msg}'/
    # msgSpeed = float(readline("options.txt", 1).replace("text-speed = ", ""))
    if clear == 'before':
        extra.clear()
    # noinput(msg, msgSpeed)
    # cursor.show()
    if msg != '':
        for i in msg:
            if i == '\ud7fc': # reset
                print('\033[0;0;0m', end='')

            elif i == '\ud7fd': # red
                print('\033[38;5;196m', end='')

            elif i == '\ud7fe': # blue
                print('\033[38;5;20m', end='')

            elif i == '\ud7ff': # green
                print('\033[38;5;34m', end="")

            elif i == '\ud800': # yellow
                print('\033[38;5;220m', end="")

            elif i == '\ud801': # pink
                print('\033[38;5;206m', end="")

            elif i == '\ud802': # cyan
                print('\033[38;5;51m', end='')

            elif i == '\ud803': # purple
                print('\033[38;5;57m', end='')

            elif i == '\ud804': # white
                print('\033[38;5;255m', end='')

            elif i == '\ud805': # lime
                print('\033[38;5;40m', end='')

            elif i == '\ud806': # gray
                print('\033[38;5;240m', end="")

            elif i == '\ud807': # light green
                print('\033[38;5;46m', end="")

            elif i == '\ud808': # light gray
                print('\033[38;5;248m', end="")

            elif i == '\ud809': # light blue
                print('\033[38;5;45m', end="")

            elif i == '\ud80a': # dark gray
                print('\033[38;5;234m', end="")

            elif i == '\udff0': # italic start
                print('\x1B[3m', end="")

            elif i == '\udff1': # italics end
                print('\x1B[0m', end="")

            else:
                print(i, end="", flush=True)
                time.sleep(msgSpeed)

        if not cont:
            input()
        # else:
        #     print()

        # print()

        if clear == 'after':
            extra.clear()
def clearAfter(msg="", speed=0.1, cont=False):
    """Prints out text and waits for input, then clears the terminal."""
    noclear(msg, speed, cont)
    extra.clear()
def clearBefore(msg='', speed=0.1, cont=False):
    """Clears the terminal, then shows text"""
    clear()
    noclear(msg, speed, cont)
def noclear(msg="", msgSpeed=float(readline("options.txt", 1).replace("text-speed = ", "")), cont=False):
    """Prints out text and waits for input."""
    size = os.get_terminal_size()
    msg = textwrap.fill(msg.strip(), size.columns, fix_sentence_endings=True, drop_whitespace=True)
    msgSpeed = float(readline("options.txt", 1).replace("text-speed = ", ""))
    if msg != '':
        if msgSpeed > 0 or msgSpeed > 0.0:
            for char in msg:
                print(char, end="", flush=True)
                if char == ",":
                    time.sleep(msgSpeed*4)
                # elif char == "\"" or char == "?" or char == "!":
                #     ""
                else:
                    time.sleep(msgSpeed)
            # input()
            # print()
        else:
            raw_msg = fr'{msg}'
            os.system('echo -n "' + msg + '"') # print(msg, flush=False, end='')
        if cont:
            print()
        else:
            input()
    # cursor.hide()
def noClear(msg="", speed=0.1, ):
    noclear(msg, speed)
def noclearinput(msg="", msgSpeed=0):
    """Prints out text."""
    size = os.get_terminal_size()
    msg = textwrap.fill(msg.strip(), size.columns, fix_sentence_endings=True, drop_whitespace=True)
    msgSpeed = float(readline("options.txt", 1).replace("text-speed = ", ""))
    if msg != '':
        if msgSpeed > 0 or msgSpeed > 0.0:
            for char in msg:
                print(char, end="", flush=True)
                if char == ",":
                    time.sleep(msgSpeed*4)
                else:
                    time.sleep(msgSpeed)
            print('')
        else:
            print(msg, flush=True)
            time.sleep(msgSpeed**msgSpeed/2)

def face(portrait="", msg="", clear='none'):
    """Prints out text with a portrait."""
    print(f"({portrait}) ", end="")
    text(msg, cont=False, clear=clear)
def faceCont(portrait="", msg=""):
    """Prints out text with a portrait."""
    print(f"({portrait}) ", end="")
    noclearinput(msg)
