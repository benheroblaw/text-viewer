#!/usr/bin/env python3
import os
def readfile(file=""):
  """Reads a file."""
  with open(file) as f:
    return f.read()
folders = readfile('./folders').splitlines()
for folder in folders:
  for direct in os.listdir(folder):
    if direct.endswith('.scri'):
      direct = direct.replace("'", "\\'")
      print(direct)
      os.system('ln -s ' + folder + str(direct))