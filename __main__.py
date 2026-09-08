#!/usr/bin/env python3
print('\33]0;loading... please wait :3\a', end='')
import os

def readline(file="", line=1):
  """Reads a line from a file.
  Lines start at 1."""
  line -= 1
  try:
    with open(file) as f:
      data = f.readlines()
      return data[line].replace("\n", "")
  except: return "error"

extra_path = readline('extra/path', 1)

if os.name == "posix":
  terminalPath = os.path.expanduser("~/.local/share/bhrobla/" + extra_path)
elif os.name == "nt":
  # terminalPath = os.path.expanduser("~\\AppData\\Local\\prokid\\text-terminal")
  print('you\'re fucked buddy :,(')
if not os.path.exists(terminalPath):
  os.makedirs(terminalPath)
os.chdir(terminalPath)

import viewer, importlib, genCollections, extra

while __name__ == '__main__':
  if 'debug' in extra.readfile('options.txt'):
    print(os.curdir)
  print('\n\33]0;loading... please wait :3\a', end='')
  os.system('./chkdeps.bash')
  if 'debug' in extra.readfile('options.txt'):
    input('> ')
  print()
  if 'debug' in extra.readfile('options.txt'):
    genCollections.generate(True, True)
  else:
    genCollections.generate(True, False)
  os.system('printf "%b" "\nUpdating... "; git pull origin ' + extra.readfile('./extra/origin'))
  viewer.main()
  print('\33]0;loading... please wait :3\a', end='')
  os.system('clear')
  print('reloading viewer...')
  importlib.reload(viewer)
  print('reloaded!\n')