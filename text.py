import os, time, threading, textwrap, extra

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

def ansi_code(code=""):
    return f"\033[{code}m"

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "x", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "X", "T", "U", "V", "W", "X", "Y", "Z", ' ']

def display(msg="", msgSpeed=0, cont=False, clear='none', portrait='<\\none/>', nameplate="<\\none/>", nobr=False):
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
        if portrait != '<\\none/>':
            print(f'({portrait}) ', end='')
        elif nameplate != '<\\none/>':
            print("(", end="")
            for i in nameplate:
                match i:
                    case'\ud7fc': # reset
                        print('\033[m', end='')
                        nameplate = nameplate.replace("\ud7fc", "", 1)

                    # colors
                    case '\ud7fd': # red
                        print('\033[38;5;196m', end='')
                        continue

                    case '\ud7fe': # blue
                        print('\033[38;5;20m', end='')
                        continue

                    case '\ud7ff': # green
                        print('\033[38;5;34m', end="")
                        continue

                    case '\ud800': # yellow
                        print('\033[38;5;220m', end="")
                        continue

                    case '\ud801': # pink
                        print('\033[38;5;206m', end="")
                        continue

                    case '\ud802': # cyan
                        print('\033[38;5;51m', end='')
                        continue

                    case '\ud803': # purple
                        print('\033[38;5;57m', end='')
                        continue

                    case '\ud804': # white
                        print('\033[38;5;255m', end='')
                        continue

                    case '\ud805': # lime
                        print('\033[38;5;40m', end='')
                        continue

                    case '\ud806': # gray
                        print('\033[38;5;240m', end="")
                        continue

                    case '\ud807': # light green
                        print('\033[38;5;46m', end="")
                        continue

                    case '\ud808': # light gray
                        print('\033[38;5;248m', end="")
                        continue

                    case '\ud809': # light blue
                        print('\033[38;5;45m', end="")
                        continue

                    case '\ud80a': # dark gray
                        print('\033[38;5;234m', end="")
                        continue

                    case "\ud80b": # black
                        print("\033[38;5;0m", end="")
                        continue

                    # background colors
                    case "\udb00": # background white
                        print(ansi_code("0;30;47"), end="")
                        continue

                    case "\udb01": # background red
                        print(ansi_code("30;41"), end="")
                        continue

                    # advanced formatting
                    case '\udff0': # italic start
                        print('\033[3m', end="")
                        continue

                    case '\udff1': # italic end
                        print('\033[23m', end="")
                        continue

                    case '\udff2': # bold start
                        print('\x1B[1m', end="")
                        continue

                    case '\udff3': # bold end
                        print('\x1B[22m', end="")
                        continue

                print(i, end="")

            print(f'{ansi_code("0")}): ', end='')

        for i in msg:
            match i:
                case'\ud7fc': # reset
                    print('\033[0m', end='')

                # colors
                case '\ud7fd': # red
                    print('\033[38;5;196m', end='')

                case '\ud7fe': # blue
                    print('\033[38;5;20m', end='')

                case '\ud7ff': # green
                    print('\033[38;5;34m', end="")

                case '\ud800': # yellow
                    print('\033[38;5;220m', end="")

                case '\ud801': # pink
                    print('\033[38;5;206m', end="")

                case '\ud802': # cyan
                    print('\033[38;5;51m', end='')

                case '\ud803': # purple
                    print('\033[38;5;57m', end='')

                case '\ud804': # white
                    print('\033[38;5;255m', end='')

                case '\ud805': # lime
                    print('\033[38;5;40m', end='')

                case '\ud806': # gray
                    print('\033[38;5;240m', end="")

                case '\ud807': # light green
                    print('\033[38;5;46m', end="")

                case '\ud808': # light gray
                    print('\033[38;5;248m', end="")

                case '\ud809': # light blue
                    print('\033[38;5;45m', end="")

                case '\ud80a': # dark gray
                    print('\033[38;5;234m', end="")

                case "\ud80b": # black
                    print("\033[38;5;0m", end="")

                # background colors
                case "\udb00": # background white
                    print(ansi_code("30;47"), end="")

                case "\udb01": # background red
                    print(ansi_code("30;41"), end="")

                # advanced formatting
                case '\udff0': # italic start
                    print('\x1B[3m', end="")

                case '\udff1': # italic end
                    print('\x1B[23m', end="")

                case '\udff2': # bold start
                    print('\x1B[1m', end="")

                case '\udff3': # bold end
                    print('\x1B[22m', end="")

            # case '\udfe0': # input (wip)
            #     print('\x1B[0m', end="")

                case _:
                    print(i, end="", flush=True)
                    time.sleep(msgSpeed)


        if not cont:
            time.sleep(msgSpeed)
            input()
        else:
            print()

        print("\033[m", end="")

        # print()
        if nobr and msgSpeed > 0.0:
            print(end="")
        else:
            print()

        if clear == 'after':
            extra.clear()

# def formatt(i=""):


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
