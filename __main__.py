#!/usr/bin/env python3
import main, importlib

while __name__ == '__main__':
  main.main()
  print('\nreloading main...')
  importlib.reload(main)
  print('reloaded!')