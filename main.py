#!/usr/bin/env python3
import sys
sys.path += '~/.local/share/prokid/text-porn/'
import extra
try: extra.createfile('options.txt', '0.025')
except: print('options.txt exists, continuing...')
import os
os.system('./chkdeps.bash')
import genCollections
import text, sys, time, textwrap, threading
# import colorama
# from colorama import *

def checkSpeed():
  while True:
    text.speed = float(extra.readline("options.txt", 1).replace("text-speed = ", ""))
    # print('text.speed is ' + str(text.speed))
    time.sleep(0.1)
speedCheck = threading.Thread(target=checkSpeed)

print('\33]0;benheroblaw\'s text viewer :3\a', end='', flush=True)


# speedCheck.start()
# speedCheck.join()

def main():

  while True:
    genCollections.generate(False)
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
      # output = output[0].upper() + output[1:]
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
    except KeyboardInterrupt: break
    try:
      sel = int(selection)-1
      if sel == -1:
        sel = folder_last +1
      selection = int(selection)
      extra.clear()
    except ValueError:
      print("")
      continue

    if selection == 0:
      while True:
        extra.clear()
        print('Options\n\n0. Back\n1. Change text speed\n2. Update')
        try: opt_sel = input('\n> ')
        except KeyboardInterrupt: break
        try:
          opt_sel = int(opt_sel)
          # selection = int(selection)
          extra.clear()
        except ValueError:
          # print("Input a number")
          extra.clear()
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
          text.speed = float(speed)
        elif opt_sel == 2:
          # print()
          os.system("printf '%b' 'updating... '; git pull origin release")
          print('Restart to finish updating')
          time.sleep(2)
        continue

    # if selection == 'update':
    #   os.system('git pull')

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
          # output = output[0].upper() + output[1:]
          chapters_pretty[i] = output
        chapters = []
        for i, x in enumerate(chapters_list):
          if x.endswith('.scri'):
            chapters.append(str(x))
        chapters.sort()
        chapter_last = len(chapters)
        print(folders_pretty[sel])
        print('Folder: ./content/' + folders[sel] + '/')

        def readmeta(line=1):
          return extra.readline('./content/' + folders[sel] + '/.meta', line)

        # meta handling
        if '.meta' in os.listdir('./content/' + folders[sel]):
          meta_lines = extra.getlines('./content/' + folders[sel] + '/.meta')
          if meta_lines >= 1:
            meta_author = extra.readline('./content/' + folders[sel] + '/.meta', 1)
            if 'authors: ' in meta_author or 'authors:' in meta_author:
              if meta_author != '':
                meta_author = meta_author.replace('authors: ', '')
                meta_author = meta_author.replace('authors:', '')
                print('Authors: ' + meta_author)
            else:
              if meta_author != '':
                meta_author = meta_author.replace('author: ', '')
                meta_author = meta_author.replace('author:', '')
                print('Author: ' + meta_author)

          if meta_lines >= 2:
            meta_rating = extra.readline('./content/' + folders[sel] + '/.meta', 2)
            if 'rating: ' or 'rating:' in meta_rating:
              meta_rating = meta_rating.replace('rating: ', '')
              meta_rating = meta_rating.replace('rating:', '')

            if meta_rating == 'error': print('Rating: ???')
            elif meta_rating == '': print('Rating: Unset; options are: g, t, e, a')
            elif 'g' in meta_rating: print('Rating: General Audiences')
            elif 't' in meta_rating: print('Rating: Teen')
            elif 'e' in meta_rating: print('Rating: Explicit')
            elif 'a' in meta_rating: print('Rating: Adult')
            else: print('Rating: ???')

          if meta_lines >= 4:
            meta_warnings = readmeta(4)
            if 'warnings: ' in meta_warnings: meta_warnings = meta_warnings.replace('warnings: ', '')
            if 'warnings:' in meta_warnings: meta_warnings = meta_warnings.replace('warnings:', '')
            # if 'warning: ' in meta_warnings: meta_warnings = meta_warnings.replace('warning: ', '')
            # if 'warning:' in meta_warnings: meta_warnings = meta_warnings.replace('warning:', '')
            if meta_warnings != '':
              print('Warnings: ' + meta_warnings)

          if meta_lines >= 3:
            meta_links = extra.readline('./content/' + folders[sel] + '/.meta', 3)
            if 'links: ' in meta_links: meta_links = meta_links.replace('links: ', '')
            if 'links:' in meta_links: meta_links = meta_links.replace('links:', '')
            if meta_links != '':
              print('Links: ' + meta_links)

        print('\n0. Back')
        for i, x in enumerate(chapters):
          print(str(i+1) + '. ' + str(chapters_pretty[i])) #'Chapter ' + str(i+1) + ': ' +
        try: chap_select = input('\n> ')
        except KeyboardInterrupt: break
        try:
          chap_sel = int(chap_select)-1
          chap_select = int(chap_select)
        except ValueError:
          # print("")
          extra.clear()
          continue
        extra.clear()
        if chap_select == 0:
          break
        if not chap_sel > chapter_last-1:
          chap_story = extra.readfile('./content/' + folders[sel] + '/' + chapters[chap_sel]).splitlines()
          try:
            for i in chap_story:
              i = i.strip()
              if i != '':
                nobr = False
                if '#' in i or '//' in i and '/ESC' not in i:
                  continue
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
                  i = i.replace('/BLD', '')
                  print('\033[1m', end='')
                if '/NOBR' in i:
                  i = i.replace('/NOBR', '')
                  nobr = True
                if '/CONT' in i:
                  i = i.replace('/CONT', '')
                  text.noinput(i)
                  if nobr:
                    print('\033[0;0;0m', end='')
                  else:
                    print('\033[0;0;0m')
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
          except KeyboardInterrupt: break

while __name__ == '__main__':
  main()