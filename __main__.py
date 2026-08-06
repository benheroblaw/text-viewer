#!/usr/bin/env python3
print('\33]0;loading... please wait :3\a', end='')
import viewer, importlib, os

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
  print('\33]0;loading... please wait :3\a', end='')
  os.system('printf "%b" "Updating... "; git pull origin ' + readfile('extra/origin'))
  # input()
  viewer.main()
  print('\33]0;loading... please wait :3\a', end='')
  os.system('clear')
  print('reloading viewer...')
  importlib.reload(viewer)
  print('reloaded!')