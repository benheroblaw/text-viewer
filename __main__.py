#!/usr/bin/env python3
print('\33]0;loading... please wait :3\a', end='')
import os

if os.name == "posix":
  terminalPath = os.path.expanduser("~/.local/share/bhrobla/text-porn")
elif os.name == "nt":
  # terminalPath = os.path.expanduser("~\\AppData\\Local\\prokid\\text-terminal")
  print('you\'re fucked buddy :,(')
if not os.path.exists(terminalPath):
  os.makedirs(terminalPath)
os.chdir(terminalPath)

import viewer, importlib, genCollections, extra

while __name__ == '__main__':
  # print(os.curdir)
  print('\n\33]0;loading... please wait :3\a', end='')
  os.system('./chkdeps.bash')
  # input('> ')
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