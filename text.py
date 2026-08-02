import os, time, cursor, threading

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

speed = float(readline("options.txt", 1).replace("text-speed = ", ""))
# battlemsgSpeed = float(readline("options.txt", 2).replace("battle-msgSpeed = ", ""))
battlemsgSpeed = 0
# if msgSpeed == 0.0:
#     msgSpeed = 0
if battlemsgSpeed <= 0:
    battlemsgSpeed = 0.0075

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "x", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "X", "T", "U", "V", "W", "X", "Y", "Z", ' ']

def text(msg=""):
    """Prints out text and waits for input, then clears the terminal."""
    noclear(msg, speed)
    os.system('clear')
def clearAfter(msg=""):
    """Prints out text and waits for input, then clears the terminal."""
    noclear(msg, speed)
    os.system('clear')
def clearBefore(msg=''):
    """Clears the terminal, then shows text"""
    clear()
    noclear(msg, speed)
def noclear(msg="", msgSpeed=speed):
    """Prints out text and waits for input."""
    # noinput(msg, msgSpeed)
    # cursor.show()
    if msg != '':
        if msgSpeed > 0 or msgSpeed > 0.0:
            for char in msg:
                print(char, end="", flush=True)
                if char == ",":
                    time.sleep(msgSpeed*4)
                # elif char == "\"" or char == "?" or char == "!":
                #     ""
                elif char in alphabet:
                    time.sleep(msgSpeed)
            input()
            # print()
        else:
            print(msg, flush=True)
            input()
    # cursor.hide()
def noClear(msg=""):
    noclear(msg, speed)
def noinput(msg="", msgSpeed=speed):
    """Prints out text."""
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

def face(portrait="", msg=""):
    """Prints out text with a portrait."""
    print(" (" + portrait + ") ", end="")
    cursor.show()
    for char in msg:
        print(char, end="", flush=True)
        time.sleep(msgSpeed)
    input()
    cursor.hide()
    clear()

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
