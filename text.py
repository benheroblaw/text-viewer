import os, time, threading, textwrap, averylib

def clear():
    averylib.clear()
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

special_chars = [
    "\ud7fc",
    "\ud7fd",
    "\ud7fe",
    "\ud7ff",
    "\ud800",
    "\ud801",
    "\ud802",
    "\ud803",
    "\ud804",
    "\ud805",
    "\ud806",
    "\ud807",
    "\ud808",
    "\ud809",
    "\ud80a",
    "\ud80b",
    "\udb00",
    "\udb01",
    "\udb02",
    "\udb03",
    "\udb04",
    "\udb05",
    "\udb06",
    "\udb07",
    "\udb08",
    "\udb09",
    "\udb0a",
    "\udb0b",
    "\udff0",
    "\udff1",
    "\udff2",
    "\udff3",
    "\udc00",
    "\udc00",
    "\udc01",
    "\udc01",
    "\ud7fc",
    "\ud7fd",
    "\ud7fe",
    "\ud7ff",
    "\ud800",
    "\ud801",
    "\ud802",
    "\ud803",
    "\ud804",
    "\ud805",
    "\ud806",
    "\ud807",
    "\ud808",
    "\ud809",
    "\ud80a",
    "\ud80b",
    "\ud80c",
    "\udb00",
    "\udb01",
    "\udb02",
    "\udb03",
    "\udb04",
    "\udb05",
    "\udb06",
    "\udb07",
    "\udb08",
    "\udb09",
    "\udb0a",
    "\udb0b",
    "\udff0",
    "\udff1",
    "\udff2",
    "\udff3",
    "\uda00",
    "\uda00",
    "\udfe0",
    "\udc00",
    "\udc00",
    "\udc01",
    "\udc01",
    "\udc00",
    "\udc01",
    "\udc02",
]

def display(msg="", msgSpeed=0, cont=False, clear='none', portrait='<\\none/>', nameplate="<\\none/>", nobr=False, skipWhitespace=True):
    """All-purpose text thing."""
    size = os.get_terminal_size()
    msg = textwrap.fill(msg, size.columns, drop_whitespace=False)
    # msg = r'{msg}'/
    # msgSpeed = float(readline("options.txt", 1).replace("text-speed = ", ""))
    if clear == 'before' or clear == "both":
        averylib.clear()
    # noinput(msg, msgSpeed)
    # cursor.show()
    msgStripped = msg
    for i in special_chars:
        msgStripped.replace(i, "")
    if msgStripped != "" or msgStripped == "" and not skipWhitespace:
        if portrait != '<\\none/>':
            print(f'({portrait}) ', end='')
        elif nameplate != '<\\none/>':
            print("(", end="")
            list_nameplate = list(nameplate)
            ansi_storage = str()
            for numb, i in enumerate(list_nameplate):
                match i:
                    case '\ud7fc': # reset
                        averylib.PrintAnsiCode("0")
                        continue

                    # colors
                    case '\ud7fd': # red
                        averylib.PrintAnsiCode("38;5;196")
                        continue

                    case '\ud7fe': # blue
                        averylib.PrintAnsiCode("38;5;20")
                        continue

                    case '\ud7ff': # green
                        averylib.PrintAnsiCode("38;5;34")
                        continue

                    case '\ud800': # yellow
                        averylib.PrintAnsiCode("38;5;220")
                        continue

                    case '\ud801': # pink
                        averylib.PrintAnsiCode("38;5;206")
                        continue

                    case '\ud802': # cyan
                        averylib.PrintAnsiCode("38;5;51")
                        continue

                    case '\ud803': # purple
                        averylib.PrintAnsiCode("38;5;57")
                        continue

                    case '\ud804': # white
                        averylib.PrintAnsiCode("38;5;255")
                        continue

                    case '\ud805': # lime
                        averylib.PrintAnsiCode("38;5;40")
                        continue

                    case '\ud806': # gray
                        averylib.PrintAnsiCode("38;5;240")
                        continue

                    case '\ud807': # light green
                        averylib.PrintAnsiCode("38;5;46")
                        continue

                    case '\ud808': # light gray
                        averylib.PrintAnsiCode("38;5;248")
                        continue

                    case '\ud809': # light blue
                        averylib.PrintAnsiCode("38;5;45")
                        continue

                    case '\ud80a': # dark gray
                        averylib.PrintAnsiCode("38;5;234")
                        continue

                    case "\ud80b": # black
                        averylib.PrintAnsiCode("38;5;0m")
                        continue

                    # background colors
                    case "\udb00": # background white
                        averylib.PrintAnsiCode("48;5;255")
                        continue

                    case "\udb01": # background red
                        averylib.PrintAnsiCode("48;5;196")
                        continue

                    case "\udb02": # background blue
                        averylib.PrintAnsiCode("48;5;20")
                        continue

                    case "\udb03": # background green
                        averylib.PrintAnsiCode("48;5;34")
                        continue

                    case "\udb04": # background yellow
                        averylib.PrintAnsiCode("48;5;220")
                        continue

                    case "\udb05": # background pink
                        averylib.PrintAnsiCode("48;5;206")
                        continue

                    case "\udb06": # background cyan
                        averylib.PrintAnsiCode("48;5;51")
                        continue

                    case "\udb07": # background purple
                        averylib.PrintAnsiCode("48;5;57")
                        continue

                    case "\udb08": # background lime
                        averylib.PrintAnsiCode("48;5;40")
                        continue

                    case "\udb09": # background gray
                        averylib.PrintAnsiCode("48;5;240")
                        continue

                    case "\udb0a": # background black
                        averylib.PrintAnsiCode("48;5;0")
                        continue

                    case "\udb0b": # background orange
                        averylib.PrintAnsiCode("48;5;202")
                        continue

                    # advanced formatting
                    case '\udff0': # italic start
                        averylib.PrintAnsiCode("3")
                        continue

                    case '\udff1': # italic end
                        averylib.PrintAnsiCode("23")
                        continue

                    case '\udff2': # bold start
                        averylib.PrintAnsiCode('1m')
                        continue

                    case '\udff3': # bold end
                        averylib.PrintAnsiCode('22m')
                        continue

                    # ANSI() start and stop characters
                    case "\udc00":
                        ansi_storage = nameplate[nameplate.find("\udc00")+1 : nameplate.find('\udc01')]
                        averylib.PrintAnsiCode(ansi_storage)
                        for numb, name in enumerate(list_nameplate):
                            if numb < num: continue
                            else:
                                if name == "\udc01": list_nameplate[numb] = ""; break
                                else: list_nameplate[numb] = ""

                        ansi_storage = str()

                    case "":
                        continue

                print(i, end="")

            print(f'{ansi_code("0")}): ', end='')

        ansi_storage = str()
        list_msg = list(msg)
        for num, i in enumerate(list_msg):
            match i:
                case'\ud7fc': # reset
                    averylib.PrintAnsiCode("0")

                # colors
                case '\ud7fd': # red
                    averylib.PrintAnsiCode("38;5;196")
                    continue

                case '\ud7fe': # blue
                    averylib.PrintAnsiCode("38;5;20")
                    continue

                case '\ud7ff': # green
                    averylib.PrintAnsiCode("38;5;34")
                    continue

                case '\ud800': # yellow
                    averylib.PrintAnsiCode("38;5;220")
                    continue

                case '\ud801': # pink
                    averylib.PrintAnsiCode("38;5;206")
                    continue

                case '\ud802': # cyan
                    averylib.PrintAnsiCode("38;5;51")
                    continue

                case '\ud803': # purple
                    averylib.PrintAnsiCode("38;5;57")
                    continue

                case '\ud804': # white
                    averylib.PrintAnsiCode("38;5;255")
                    continue

                case '\ud805': # lime
                    averylib.PrintAnsiCode("38;5;40")
                    continue

                case '\ud806': # gray
                    averylib.PrintAnsiCode("38;5;240")
                    continue

                case '\ud807': # light green
                    averylib.PrintAnsiCode("38;5;46")
                    continue

                case '\ud808': # light gray
                    averylib.PrintAnsiCode("38;5;248")
                    continue

                case '\ud809': # light blue
                    averylib.PrintAnsiCode("38;5;45")
                    continue

                case '\ud80a': # dark gray
                    averylib.PrintAnsiCode("38;5;234")
                    continue

                case "\ud80b": # black
                    averylib.PrintAnsiCode("38;5;0m")
                    continue

                case "\ud80c":
                    averylib.PrintAnsiCode("38;5;202")
                    continue

                # background colors
                case "\udb00": # background white
                    averylib.PrintAnsiCode("48;5;255")
                    continue

                case "\udb01": # background red
                    averylib.PrintAnsiCode("48;5;196")
                    continue

                case "\udb02": # background blue
                    averylib.PrintAnsiCode("48;5;20")
                    continue

                case "\udb03": # background green
                    averylib.PrintAnsiCode("48;5;34")
                    continue

                case "\udb04": # background yellow
                    averylib.PrintAnsiCode("48;5;220")
                    continue

                case "\udb05": # background pink
                    averylib.PrintAnsiCode("48;5;206")
                    continue

                case "\udb06": # background cyan
                    averylib.PrintAnsiCode("48;5;51")
                    continue

                case "\udb07": # background purple
                    averylib.PrintAnsiCode("48;5;57")
                    continue

                case "\udb08": # background lime
                    averylib.PrintAnsiCode("48;5;40")
                    continue

                case "\udb09": # background gray
                    averylib.PrintAnsiCode("48;5;240")
                    continue

                case "\udb0a": # background black
                    averylib.PrintAnsiCode("48;5;0")
                    continue

                case "\udb0b": # background orange
                    averylib.PrintAnsiCode("48;5;202")
                    continue

                # advanced formatting
                case '\udff0': # italic start
                    averylib.PrintAnsiCode('3m')
                    continue

                case '\udff1': # italic end
                    averylib.PrintAnsiCode('23m')
                    continue

                case '\udff2': # bold start
                    averylib.PrintAnsiCode('1m')
                    continue

                case '\udff3': # bold end
                    averylib.PrintAnsiCode('22m')
                    continue

                case "\uda00":
                    if not nobr: print('\n')
                    else: print()
                    if msg == "\uda00":
                        break
                    continue

                # ANSI() start and stop characters
                case "\udc00":
                    ansi_storage = msg[msg.find("\udc00")+1 : msg.find('\udc01')]
                    averylib.PrintAnsiCode(ansi_storage)
                    for numb, name in enumerate(list_msg):
                        if numb < num: continue
                        else:
                            if name == "\udc01": list_msg[numb] = ""; break
                            else: list_msg[numb] = ""

                    msg = msg.replace(f"\udc00{ansi_storage}\udc01", f"{'\udc02' * (len(ansi_storage) + 2)}")
                    ansi_storage = str()

                case "":
                    continue

                case _:
                    print(i, end="", flush=True)
                    time.sleep(msgSpeed)


        averylib.PrintAnsiCode("0")
        time.sleep(msgSpeed)
        if not cont:
            input()
        elif cont and nobr:
            print()
        elif nobr:
            print(end="")
        else:
            print()


        # print()
        if nobr and msgSpeed > 0.0:
            print(end="")
        elif nobr:
            print(end="")
        else:
            print()

        if clear == 'after' or clear == "both":
            averylib.clear()

# def formatt(i=""):


def clearAfter(msg="", speed=0.1, cont=False):
    """Prints out text and waits for input, then clears the terminal."""
    noclear(msg, speed, cont)
    averylib.clear()

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
    display(msg, cont=False, clear=clear)

def faceCont(portrait="", msg=""):
    """Prints out text with a portrait."""
    print(f"({portrait}) ", end="")
    noclearinput(msg)
