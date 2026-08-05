#!/usr/bin/env python3
import sys
# sys.path += '~/.local/share/prokid/text-porn/'
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
    size = os.get_terminal_size()
    print(textwrap.fill('Folders in ./content: ' + str(folders), size.columns, break_on_hyphens=False) + '\n\n0. Options')
    # print()
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
        size = os.get_terminal_size()
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
        print('Title:    ' + folders_pretty[sel])
        print('Folder:   ./content/' + folders[sel] + '/\n')

        def readmeta(line=1):
          return extra.readline('./content/' + folders[sel] + '/.meta', line)

        # old meta handling
        # if '.meta' in os.listdir('./content/' + folders[sel]):
        #   meta_lines = extra.getlines('./content/' + folders[sel] + '/.meta')
        #   if meta_lines >= 1:
        #     meta_author = extra.readline('./content/' + folders[sel] + '/.meta', 1)
        #     if 'authors: ' in meta_author or 'authors:' in meta_author:
        #       if meta_author != '':
        #         meta_author = meta_author.replace('authors: ', '')
        #         meta_author = meta_author.replace('authors:', '')
        #         meta_author = meta_author.strip()
        #         size = os.get_terminal_size()
        #         print(textwrap.fill('Authors:  ' + meta_author, size.columns))
        #     else:
        #       if meta_author != '':
        #         meta_author = meta_author.replace('author: ', '')
        #         meta_author = meta_author.replace('author:', '')
        #         meta_author = meta_author.strip()
        #         size = os.get_terminal_size()
        #         print(textwrap.fill('Author:   ' + meta_author, size.columns))

        #   if meta_lines >= 2:
        #     meta_rating = extra.readline('./content/' + folders[sel] + '/.meta', 2)
        #     meta_rating = meta_rating.strip()
        #     if 'rating: ' or 'rating:' in meta_rating:
        #       meta_rating = meta_rating.replace('rating: ', '')
        #       meta_rating = meta_rating.replace('rating:', '')

        #     size = os.get_terminal_size()
        #     if meta_rating == 'error': print('Rating: ???')
        #     elif meta_rating == '': print(textwrap.fill('Rating:   Unset; options are: g, t, e, a', size.columns))
        #     elif 'g' in meta_rating: print(textwrap.fill('Rating:   \033[1;32mGeneral Audiences', size.columns))
        #     elif 't' in meta_rating: print(textwrap.fill('Rating:   \033[1;36mTeen', size.columns))
        #     elif 'e' in meta_rating: print(textwrap.fill('Rating:   \033[1;33mExplicit', size.columns))
        #     elif 'a' in meta_rating: print(textwrap.fill('Rating:   \033[1;31mAdult', size.columns))
        #     else: print('Rating: ???')
        #     print('\033[0;0;0m', end='')

        #   if meta_lines >= 4:
        #     meta_warnings = readmeta(4)
        #     if 'warnings: ' in meta_warnings: meta_warnings = meta_warnings.replace('warnings: ', '')
        #     if 'warnings:' in meta_warnings: meta_warnings = meta_warnings.replace('warnings:', '')
        #     # if 'warning: ' in meta_warnings: meta_warnings = meta_warnings.replace('warning: ', '')
        #     # if 'warning:' in meta_warnings: meta_warnings = meta_warnings.replace('warning:', '')
        #     meta_warnings = meta_warnings.strip()
        #     if meta_warnings != '':
        #       size = os.get_terminal_size()
        #       print('Warnings: ' + meta_warnings)

        #   if meta_lines >= 3:
        #     meta_links = extra.readline('./content/' + folders[sel] + '/.meta', 3)
        #     if 'links: ' in meta_links: meta_links = meta_links.replace('links: ', '')
        #     if 'links:' in meta_links: meta_links = meta_links.replace('links:', '')
        #     meta_links.strip()
        #     if meta_links != '':
        #       size = os.get_terminal_size()
        #       print(textwrap.fill('Links:    ' + meta_links, size.columns))

        #   if meta_lines >= 5:
        #     meta_credits = readmeta(5)
        #     if 'credits: ' in meta_credits: meta_credits = meta_credits.replace('credits: ')
        #     if 'credits:' in meta_credits: meta_credits = meta_credits.replace('credits:')
        #     meta_credits = meta_credits.strip()
        #     if meta_credits != '':
        #       size = os.get_terminal_size()
        #       print(textwrap.fill('Credits:  ' + meta_credits, size.columns))

        # new meta handling
        if '.meta' in os.listdir('./content/' + folders[sel]):
          meta_author =   ''
          meta_authors =   ''
          meta_rating =   ''
          meta_warnings = ''
          meta_links =    ''
          meta_credits =  ''

          meta_file = extra.readfile('./content/' + folders[sel] + '/.meta').splitlines()

          # print(str(meta_file))

          for x in meta_file:
            if 'authors:' in x:
              meta_author = x.replace('authors: ', '')
              meta_author = meta_author.replace('authors:', '')
              meta_author = meta_author.strip()
            elif 'author:' in x:
              meta_author = x.replace('author: ', '')
              meta_author = meta_author.replace('author:', '')
              meta_author = meta_author.strip()

            if 'rating:' in x: meta_rating = x.replace('rating: ', ''); meta_rating = meta_rating.replace('rating:', '')

            if 'warnings:' in x: meta_warnings = x.replace('warnings: ', ''); meta_warnings.replace('warnings:', '')
            # if 'warning: ' in meta_warnings: meta_warnings = meta_warnings.replace('warning: ', '')
            # if 'warning:' in meta_warnings: meta_warnings = meta_warnings.replace('warning:', '')
            meta_warnings = meta_warnings.strip()

            # if 'links: ' in meta_links: meta_links = meta_links.replace('links: ', '')
            if 'links:' in x: meta_links = x.replace('links: ', ''); meta_links.replace('links:', '')
            meta_links.strip()

            if 'credits:' in x: meta_credits = x.replace('credits: ', ''); meta_credits.replace('credits:', '')
            meta_credits = meta_credits.strip()

          # print meta
          # elif meta_rating == '': print(textwrap.fill('Rating:   Unset; options are: g, t, e, a', size.columns))
          if 'g' in meta_rating: print(textwrap.fill('Rating:   \033[1;32mGeneral Audiences', size.columns))
          elif 't' in meta_rating: print(textwrap.fill('Rating:   \033[1;36mTeen', size.columns))
          elif 'e' in meta_rating: print(textwrap.fill('Rating:   \033[1;33mExplicit', size.columns))
          elif 'a' in meta_rating: print(textwrap.fill('Rating:   \033[1;31mAdult', size.columns))
          else: print('Rating:   ???')
          print('\033[0;0;0m', end='')
          if meta_warnings != '':
            size = os.get_terminal_size()
            print(textwrap.fill('Warnings: ' + meta_warnings, size.columns))

          if meta_authors != '':
            size = os.get_terminal_size()
            print(textwrap.fill('Authors:  ' + meta_authors, size.columns))

          if meta_author != '':
            size = os.get_terminal_size()
            print(textwrap.fill('Author:   ' + meta_author, size.columns))

          if meta_links != '':
            size = os.get_terminal_size()
            print(textwrap.fill('Links:    ' + meta_links, size.columns))

          if meta_credits != '':
            size = os.get_terminal_size()
            print(textwrap.fill('Credits:  ' + meta_credits, size.columns))



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
                else:
                  i = i.replace('/ESC', '')
                if '/ESCSTRS' not in i:
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
                    if nobr:
                      print('\033[0;0;0m', end='')
                    else:
                      print('\033[0;0;0m')
                    continue
                  if '/CLRB' in i:
                    i = i.replace('/CLRB', '')
                    text.clearBefore(i)
                    if nobr:
                      print('\033[0;0;0m', end='')
                    else:
                      print('\033[0;0;0m')
                    continue
                  else:
                    text.noClear(i)
                    if nobr:
                      print('\033[0;0;0m', end='')
                    else:
                      print('\033[0;0;0m')
                else:
                  text.noclear(i)
              # print()
            input('> Return ')
            extra.clear()
          except KeyboardInterrupt: break

while __name__ == '__main__':
  main()