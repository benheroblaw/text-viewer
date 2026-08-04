#!/usr/bin/env python3
import main, importlib, os

while __name__ == '__main__':
  os.system('git pull')
  main.main()
  print('\nreloading main...')
  importlib.reload(main)
  print('reloaded!')