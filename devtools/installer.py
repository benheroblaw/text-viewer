#!/usr/bin/env python3
import os, time

if os.name == "posix":
  terminalPath = os.path.expanduser("~/.local/share/bhrobla/")
elif os.name == "nt":
  terminalPath = os.path.expanduser("~/AppData/Local/bhrobla/")
if not os.path.exists(terminalPath):
  os.makedirs(terminalPath)
os.chdir(terminalPath)

os.system('git clone -b release https://github.com/benheroblaw/text-viewer')
portable = input("Make portable? [y/n]\n")
if portable == 'y':
  os.system('echo portable! > extra/portable')
print("\nSuccessfully installed!")
time.sleep(2)
input("\nPress Enter to continue")