#!/usr/bin/env python3
import sys
sys.path += '~/.local/share/prokid/text-porn/'
import extra
try: extra.createfile('options.txt', '0.025')
except: print('options.txt exists, continuing...')
import text, os, sys, time, textwrap, threading

def checkSpeed():
  while True:
    text.speed = float(extra.readline("options.txt", 1).replace("text-speed = ", ""))
    # print('text.speed is ' + str(text.speed))
    time.sleep(0.1)
speedCheck = threading.Thread(target=checkSpeed)

print('\33]0;benheroblaw\'s text-based pornography viewer\a', end='', flush=True)


# speedCheck.start()
# speedCheck.join()

while True:
  folder = os.scandir('./content')
  folders = []
  for entry in folder:
    if entry.is_dir():
      # print(entry)
      folders.append(str(entry.name))
  folders.sort()

  folder_last = len(folders)

  folders_pretty = folders
  for i, x in enumerate(folders_pretty):
    # text.text(i)
    output = x
    output = output.removeprefix('_')
    output = output.replace("_", ' ')
    output = output.replace('zzz-', '_')
    output = output[0].upper() + output[1:]
    # folders_pretty[i] = x.replace('_', ' ')
    folders_pretty[i] = output
    # print(i)

  folders = os.listdir('content')
  folders.sort()
  # folders_pretty.sort()

  extra.clear()
  print('Folders in ./content: ' + str(folders))
  print('\n0. Options')
  for i, x in enumerate(folders):
    print(str(i+1) + '. ' + folders_pretty[i])
  try: selection = input('\n> ')
  except KeyboardInterrupt: continue
  try:
    sel = int(selection)-1
    if sel == -1:
      sel = folder_last +1
    selection = int(selection)
    extra.clear()
  except ValueError:
    print("Input a number")
    continue

  if selection == 0:
    while True:
      extra.clear()
      print('Options\n\n0. Back\n1. Change text speed')
      try: opt_sel = input('\n> ')
      except KeyboardInterrupt: break
      try:
        opt_sel = int(opt_sel)
        # selection = int(selection)
        extra.clear()
      except ValueError:
        print("Input a number")
        continue
      if opt_sel == 0:
        break
      elif opt_sel == 1:
        print('Options\n\nCurrent speed: ' + str(text.speed))
        print('New speed (in seconds):')
        try: speed = input('\n> ')
        except KeyboardInterrupt: continue
        try:
          speed = float(speed)
          # selection = int(selection)
        except ValueError:
          print("Input a number")
          continue
        extra.writeline('options.txt', 1, speed)
        text.speed = float(extra.readline("options.txt", 1))
      continue

  # if sel

  # chapters = os.listdir('./content/' + folders[sel] + '')

  if not sel > folder_last:
    while True:
      chapters_list = os.listdir('./content/' + folders[sel] + '')
      chapters = []
      for i, x in enumerate(chapters_list):
        if x.endswith('.scri'):
          chapters.append(str(x))
      chapters.sort()
      chapters_pretty = chapters
      for i, x in enumerate(chapters_pretty):
        output = x.replace("_", ' ')
        output = output.replace('zzz-', '_')
        output = output.removesuffix('.scri')
        output = output[0].upper() + output[1:]
        chapters_pretty[i] = output
      chapters = []
      for i, x in enumerate(chapters_list):
        if x.endswith('.scri'):
          chapters.append(str(x))
      chapters.sort()
      chapter_last = len(chapters)
      print(folders_pretty[sel])
      print('Folder: ./content/' + folders[sel] + '/')
      if 'author' in os.listdir('./content/' + folders[sel]):
        print('Author: ' + extra.readline('./content/' + folders[sel] + '/author', 1))
      print('\n0. Back')
      for i, x in enumerate(chapters):
        print(str(i+1) + '. ' + str(chapters_pretty[i])) #'Chapter ' + str(i+1) + ': ' +
      try: chap_select = input('\n> ')
      except KeyboardInterrupt: break
      try:
        chap_sel = int(chap_select)-1
        chap_select = int(chap_select)
      except ValueError:
        print("Input a number")
        extra.clear()
        continue
      extra.clear()
      if chap_select == 0:
        break
      if not chap_sel > chapter_last-1:
        chap_story = extra.readfile('./content/' + folders[sel] + '/' + chapters[chap_sel]).splitlines()
        for i in chap_story:
          i = i.strip()
          if i != '':
            nobr = False
            if '/RED' in i:
              i = i.replace('/RED', '')
              print('\033[0;31m', end='')
            if '/GRN' in i:
              i = i.replace('/GRN', '')
              print('\033[0;32m', end="")
            if '/YLW' in i:
              i=i.replace('/YLW', '')
              print('\033[0;33m', end='')
            if '/BLU' in i:
              i = i.replace('/BLU', '')
              print('\033[0;34m', end='')
            if '/BLD' in i:
              i = i.replace('/b', '')
              i = i.replace('/BLD', '')
              i = i.replace('/B', '')
              print('\033[1m', end='')
            elif '#' in i:
              continue
            if '/NOBR' in i:
              i = i.replace('/NOBR', '')
              nobr = True
            if '/CONT' in i:
              i = i.replace('/CONT', '')
              text.noinput(i)
              continue
            if '/CLRA' in i:
              i = i.replace('/CLRA', '')
              text.clearAfter(i)
              continue
            if '/CLRB' in i:
              i = i.replace('/CLRB', '')
              text.clearBefore(i)
              continue
            else:
              text.noClear(i)
            if nobr:
              print('\033[0;0;0m', end='')
            else:
              print('\033[0;0;0m')
          # print()
        input('> Return ')
        extra.clear()