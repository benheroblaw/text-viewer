import os, time, random, sys, cmd
# from colorama import *
from importlib import reload

os.system('clear')
print('loading extra...')

textReset = '\033[0;0;0m'
dev = 'dev'

if os.name == "posix":
  # terminalPath = os.path.expanduser("~/.local/share/prokid/text-porn")
  ""
elif os.name == "nt":
  # terminalPath = os.path.expanduser("~\\AppData\\Local\\prokid\\text-terminal")
  print('you\'re fucked buddy :\'(')
# if not os.path.exists(terminalPath):
#   os.makedirs(terminalPath)
# os.chdir(terminalPath)

# file management
def createfile(file="", contents=""):
  """Creates a file, errors if the file exists."""
  with open(file, "x") as f:
    f.write(contents)

def terminalName(name):
  print('\33]0;'+name+'\a', end='', flush=True)

def writefile(file="", contents=""):
  """Overwrites a file."""
  with open(file, "w") as f:
    f.write(contents)
def writeline(file="", line=1, contents=""):
  """Writes a line to a file.
  Line starts at 1."""
  contents = str(contents)
  line -= 1
  contents += "\n"
  with open(file) as f:
    data = f.readlines()
  # print(data)
  try: data[line] = contents
  except: print("failed to write to " + file); return ResourceWarning
  with open(file, "w") as f:
    f.writelines(data)

def readfile(file=""):
  """Reads a file."""
  with open(file) as f:
    return f.read()
def readline(file="", line=1):
  """Reads a line from a file.
  Lines start at 1."""
  line -= 1
  try:
    with open(file) as f:
      data = f.readlines()
      return data[line].replace("\n", "")
  except: return "error"

def getlines(file=""):
  """Returns the number of lines in a file."""
  with open(file) as f:
    data = f.readlines()
    return len(data)
def newline(file=""):
  """nonfunctional
  It's supposed to add a line to the end of the file."""
  line = getlines(file) +1
  contents = "\n"
  with open(file) as f:
    data = f.readlines()
  try: data[line] = contents
  except: print(Fore.RED + "failed to write to: \"" + file + '"' + Fore.RESET)
  with open(file, "w") as f:
    f.writelines(data)

# terminal management
def clear(force=''):
  """Clears the terminal."""
  # if dev not in cmd.name and force == '':
  os.system("clear")
  # elif dev in cmd.name and force != '':
  #   print('\n\033[1;37;40mforcing clear through \033[1;30m_dev_login_\033[1;37m...' + textReset + '\n')
  # else: print('\n\033[1;37;40mextra.clear blocked by \033[1;30m_dev_login_' + textReset + '\n')
def pos(x, y):
  """Returns the position of the cursor."""
  return '\x1b[' + str(y) + ';' + str(x) + 'H'

class cursor:
  def move(x, y):
    """Changes the position of the cursor."""
    print(pos(x, y), end="")
  def show():
    """Shows the cursor."""
    functions.show_cursor()
  def hide():
    """Hides the cursor."""
    functions.hide_cursor()

class functions:
  def hide_cursor():
    if os.name == 'nt':
      ci = _CursorInfo()
      handle = ctypes.windll.kernel32.GetStdHandle(-11)
      ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
      ci.visible = False
      ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
    elif os.name == 'posix':
      sys.stdout.write("\033[?25l")
      sys.stdout.flush()
  def show_cursor():
    if os.name == 'nt':
      ci = _CursorInfo()
      handle = ctypes.windll.kernel32.GetStdHandle(-11)
      ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
      ci.visible = True
      ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
    elif os.name == 'posix':
      sys.stdout.write("\033[?25h")
      sys.stdout.flush()

def console(location ='~/.local/share/prokid/webserver', cmd = 'python3 /webserver/prokid.py'):
  os.system("cd " + location + "; gnome-terminal -e 'bash -c \"" + cmd + " ;bash\"'")
def newConsole(cmd = '', name=''):
  print(name)
  os.system("gnome-terminal -e 'bash -c \"" + cmd + " ;bash\"'")

def done(end=''):
  print('\033[0;32mdone' + textReset + end)

# print('running extra.cmd')
# exec(readfile('extra.cmd'))
# os.system('clear')