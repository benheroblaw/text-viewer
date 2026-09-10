import os, time, random, sys, cmd
# from colorama import *
from importlib import reload

clearCommand = ''
if os.name == 'posix':
  clearCommand = 'clear'
elif os.name == 'nt':
  clearCommand = 'cls'

os.system(clearCommand)
print('loading extra...')
# print(os.curdir)

textReset = '\033[0;0;0m'

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
  """nonfunctional :C
  It's supposed to add a line to the end of the file."""
  line = getlines(file) +1
  contents = "\n"
  with open(file) as f:
    data = f.readlines()
  try: data[line] = contents
  except: print("failed to write to: \"" + file + '"')
  with open(file, "w") as f:
    f.writelines(data)

# terminal management
def clear(force=''):
  """Clears the terminal."""
  os.system(clearCommand)
  print(textReset, end='')
def pos(x, y):
  """Returns the position of the cursor."""
  return '\x1b[' + str(y) + ';' + str(x) + 'H'

def done(end=''):
  print('\033[0;32m done' + textReset + end)

# print('running extra.cmd')
# exec(readfile('extra.cmd'))
# os.system(clearCommand)