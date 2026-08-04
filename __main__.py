#!/usr/bin/env python3
import main, importlib, os

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

while __name__ == '__main__':
  os.system('printf "%b" "Updating... "; git pull origin ' + readfile('extra/origin'))
  main.main()
  print('\nreloading main...')
  importlib.reload(main)
  print('reloaded!')