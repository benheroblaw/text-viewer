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

# set the path between dev and release versions
extra_path = readline('extra/path', 1)

# are we using portable mode?
if 'portable' not in os.listdir('extra/'):
  # set the terminal path for unix
  if os.name == "posix":
    terminalPath = os.path.expanduser("~/.local/share/bhrobla/" + extra_path)
  # set the terminal path for windows
  elif os.name == "nt" or platform.system == 'Windows':
    terminalPath = os.path.expanduser("~/AppData/Local/bhrobla/" + extra_path)
    print(terminalPath)
  if not os.path.exists(terminalPath):
    os.makedirs(terminalPath)
  os.chdir(terminalPath)

import extra
try: extra.createfile('options.txt', '\
  0.025\n\
  2\n\
  1\n\
  0\n\
  '
  .strip()
)
except FileExistsError: print('options.txt exists, continuing...')



import fish, importlib, genCollections



while __name__ == '__main__':
  # are we in debug mode?
  debug = False
  if 'debug' in extra.readfile('options.txt'):
    debug = True

  # debug: get the absolute cwd
  if debug:
    print(f'current working directory: {os.path.abspath(".")}')

  # set the window title
  print('\n\33]0;loading... please wait :3\a', end='')

  # if we're on unix, run chkdeps.bash
  if os.name == 'posix':
    if debug:
      print("chmodding chkdeps.bash...")
    os.system('chmod +x ./chkdeps.bash')
    if debug:
      print("chmodded chkdeps!\n\nrunning chkdeps...")
    os.system("./chkdeps.bash")
    print()

  # update with git (system-dependent)
  if os.name == 'posix':
    os.system('printf "%b" "Updating... "; git pull origin ' + extra.readfile('./extra/origin'))
  elif os.name == "nt":
    print("Updating...")
    os.system("git pull origin " + extra.readfile('./extra/origin'))
  print()

  # generate symlinks for collections
  genCollections.generate(debug, debug)

  # barracuda
  fish.Barracuda()

  # reload everything (doesn't work fully goddammit)
  print('\33]0;loading... please wait :3\a', end='')
  extra.clear()
  print('reloading viewer...')
  importlib.reload(fish)
  print('reloaded!\n')