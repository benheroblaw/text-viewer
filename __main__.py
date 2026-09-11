#!/usr/bin/env python3
print('\33]0;loading... please wait :3\a', end='')
import os, platform

def readline(file="", line=1):
  """Reads a line from a file.
  Lines start at 1."""
  line -= 1
  try:
    with open(file) as f:
      data = f.readlines()
      return data[line].replace("\n", "")
  except: return "error"
def readfile(file="", line=1):
  """Reads a file."""
  line -= 1
  try:
    with open(file) as f:
      return f.readlines()
  except: return "error"

extra_path = readline('extra/path', 1)

if 'portable' not in os.listdir('extra/'):
  if os.name == "posix":
    terminalPath = os.path.expanduser("~/.local/share/bhrobla/" + extra_path)
  elif os.name == "nt" or platform.system == 'Windows':
    terminalPath = os.path.expanduser("~/AppData/Local/bhrobla/" + extra_path)
    print(terminalPath)
  if not os.path.exists(terminalPath):
    os.makedirs(terminalPath)
  os.chdir(terminalPath)

import viewer, importlib, genCollections, extra

while __name__ == '__main__':
  if 'debug' in extra.readfile('options.txt'):
    print(os.curdir)
  print('\n\33]0;loading... please wait :3\a', end='')
  if os.name == 'posix':
    os.system('./chkdeps.bash')
  if 'debug' in extra.readfile('options.txt'):
    input('> ')
  print()
  if 'debug' in extra.readfile('options.txt'):
    genCollections.generate(True, True)
  else:
    genCollections.generate(True, False)
  if os.name == 'posix':
    os.system('printf "%b" "\nUpdating... "; git pull origin ' + extra.readfile('./extra/origin'))
  viewer.main()
  print('\33]0;loading... please wait :3\a', end='')
  extra.clear()
  print('reloading viewer...')
  importlib.reload(viewer)
  print('reloaded!\n')