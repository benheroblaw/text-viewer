import os, time, cursor, threading, textwrap

def clear():
    os.system("clear")
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

# speed = float(readline("options.txt", 1).replace("text-speed = ", ""))
# battlemsgSpeed = float(readline("options.txt", 2).replace("battle-msgSpeed = ", ""))
battlemsgSpeed = 0
# if msgSpeed == 0.0:
#     msgSpeed = 0
if battlemsgSpeed <= 0:
    battlemsgSpeed = 0.0075

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "x", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "X", "T", "U", "V", "W", "X", "Y", "Z", ' ']

def text(msg="", msgSpeed=0, cont=False, clear='none'):
    """All-purpose text thing."""
    size = os.get_terminal_size()
    msg = textwrap.fill(msg, size.columns, fix_sentence_endings=True, drop_whitespace=False)
    # msg = r'{msg}'/
    # msgSpeed = float(readline("options.txt", 1).replace("text-speed = ", ""))
    if clear == 'before':
        os.system('clear')
    # noinput(msg, msgSpeed)
    # cursor.show()
    if msg != '':
        if msgSpeed > 0 or msgSpeed > 0.0:
            if '\e[3m' in msg or '\e[23m' in msg:
                i_list = []
                i_list += msg.split('\e[3m')
                msg = msg.replace('\e[3m', '')
                msg = msg.replace('\e[23m', '')
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
            # raw_msg = fr'{msg}'
            print(msg, end='')
            # os.system('echo -n "' + msg + '"') # print(msg, flush=False, end='')

        if not cont:
            input()
        # else:
        #     print()

        # print()

        if clear == 'after':
            os.system('clear')
def clearAfter(msg="", cont=False):
    """Prints out text and waits for input, then clears the terminal."""
    noclear(msg, speed, cont)
    os.system('clear')
def clearBefore(msg='', cont=False):
    """Clears the terminal, then shows text"""
    clear()
    noclear(msg, speed, cont)
def noclear(msg="", msgSpeed=float(readline("options.txt", 1).replace("text-speed = ", "")), cont=False):
    """Prints out text and waits for input."""
    size = os.get_terminal_size()
    msg = textwrap.fill(msg.strip(), size.columns, fix_sentence_endings=True, drop_whitespace=True)
    # msg = r'{msg}'/
    msgSpeed = float(readline("options.txt", 1).replace("text-speed = ", ""))
    # noinput(msg, msgSpeed)
    # cursor.show()
    if msg != '':
        if msgSpeed > 0 or msgSpeed > 0.0:
            if '\e[3m' in msg or '\e[23m' in msg:
                i_list = []
                i_list += msg.split('\e[3m')
                msg = msg.replace('\e[3m', '')
                msg = msg.replace('\e[23m', '')
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
def noClear(msg=""):
    noclear(msg, speed)
def noclearinput(msg="", msgSpeed=0):
    """Prints out text."""
    size = os.get_terminal_size()
    msg = textwrap.fill(msg.strip(), size.columns, fix_sentence_endings=True, drop_whitespace=True)
    msgSpeed = float(readline("options.txt", 1).replace("text-speed = ", ""))
    if msg != '':
        if msgSpeed > 0 or msgSpeed > 0.0:
    # cursor.show()
            for char in msg:
                print(char, end="", flush=True)
                if char == ",":
                    time.sleep(msgSpeed*4)
                # elif char == "\"" or char == "?" or char == "!":
                #     ""
                else:
                    time.sleep(msgSpeed)
            # time.sleep(msgSpeed**msgSpeed*0.25)
            print('')
            # cursor.hide()
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
    # cursor.show()
    # for char in msg:
    #     print(char, end="", flush=True)
    #     time.sleep(msgSpeed)
    # input()
    noclearinput(msg)
    # cursor.hide()
    # clear()

def answer(options="", ans1="", ans2="", ans3=""):
    """Pretty input function."""
    cursor.show()
    for char in options:
        print(char, end="", flush=True)
        if char == ",":
            time.sleep(msgSpeed*4)
        elif char == "\"" or char == "?" or char == "!":
            ""
        else:
            time.sleep(msgSpeed)
    if ans3 != "":
        ans = input("\n (" + ans1 + ", " + ans2 + ", " + ans3 + ") ")
    else:
        ans = input("\n (" + ans1 + ", " + ans2 + ") ")
        cursor.hide()

    clear()
    return ans

def battletext(msg=""):
    """Prints text at a different msgSpeed and waits for input."""
    cursor.show()
    for char in msg:
        print(char, end="", flush=True)
        if char in alphabet:
            time.sleep(battlemsgSpeed)
        else:
            ""
    input()
    cursor.hide()
    print()
def losetext(msg=""):
    """Prints text at a set msgSpeed."""
    cursor.show()
    for char in msg:
        print(char, end="", flush=True)
        if char in alphabet:
            time.sleep(0.25)
        else:
            ""
    input()
    cursor.hide()
    clear()
def battleNoInput(msg=""):
    """Prints text at a different msgSpeed."""
    cursor.show()
    for char in msg:
        print(char, end="", flush=True)
        if char == ",":
            time.sleep(battlemsgSpeed)
        elif char == "\"" or char == "?" or char == "!":
            ""
        else:
            time.sleep(battlemsgSpeed)
    time.sleep(battlemsgSpeed * 5)
    cursor.hide()
    print()
def battleAnswer(options="", ans1="", ans2="", ans3="", ans4=""):
    """Fancy input function."""
    cursor.show()
    for char in options:
        print(char, end="", flush=True)
        if char in alphabet:
            time.sleep(battlemsgSpeed)
        else:
            ""
    if ans3 != "" and ans4 != "":
        ans = input("\n (" + ans1 + ", " + ans2 + ", " + ans3 + ", " + ans4 + ") ")
    elif ans3 != "":
        ans = input("\n (" + ans1 + ", " + ans2 + ", " + ans3 + ") ")
    else:
        ans = input("\n (" + ans1 + ", " + ans2 + ") ")
        cursor.hide()

    return ans

# msgSpeedCheck.start()
