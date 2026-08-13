#!/usr/bin/env python3
import sys
# sys.path += '~/.local/share/prokid/text-porn/'
import extra
try: extra.createfile('options.txt', '0.05')
except: print('options.txt exists, continuing...')
import os
os.system('./chkdeps.bash')
import genCollections
import text, sys, time, textwrap, threading, json
# import colorama
# from colorama import *

def checkSpeed():
  while True:
    text.speed = float(extra.readline("options.txt", 1).replace("text-speed = ", ""))
    # print('text.speed is ' + str(text.speed))
    time.sleep(0.1)
speedCheck = threading.Thread(target=checkSpeed)



# speedCheck.start()
# speedCheck.join()

def main():

  while True:
    print('\33]0;benheroblaw\'s text viewer :3\a', end='', flush=True)
    if 'devtools' in os.listdir('./'):
      if 'debug' in extra.readfile('options.txt'):
        genCollections.generate(True, True)
      else:
        genCollections.generate(True, False)
    else:
      genCollections.generate()
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
    # raw
    if extra.readline('options.txt', 2) == '1':
      output = str(folders)
      output = output.removeprefix('[')
      output = output.removesuffix(']')
      files_indent = '  '
      print('Folders in ./content: ')
      print(textwrap.fill(str(output), size.columns, break_on_hyphens=False, subsequent_indent=files_indent, initial_indent=' ') + '\n\n0. Options')
    # pretty
    elif extra.readline('options.txt', 2) == '0':
      print('./content/...\n\n0. Options')
    # neither
    else:
      extra.writefile('options.txt', extra.readline('options.txt', 1) + '\n1')
      continue

    # show tags
    if extra.readline('options.txt', 3) == '1':
      # print(textwrap.fill('Folders in ./content: ' + str(folders), size.columns, break_on_hyphens=False) + '\n\n0. Options')
      pass
    # don't show tags
    elif extra.readline('options.txt', 3) == '0':
      # print('./content/...\n\n0. Options')
      pass
    # neither
    else:
      extra.writefile('options.txt', f'{extra.readline('options.txt', 1)}\n{extra.readline('options.txt', 2)}\n0')
      continue

    # sort tags
    if extra.readline('options.txt', 4) == '1':
      # print(textwrap.fill('Folders in ./content: ' + str(folders), size.columns, break_on_hyphens=False) + '\n\n0. Options')
      pass
    # don't sort tags
    elif extra.readline('options.txt', 4) == '0':
      # print('./content/...\n\n0. Options')
      pass
    # neither
    else:
      extra.writefile('options.txt', f'{extra.readline('options.txt', 1)}\n{extra.readline('options.txt', 2)}\n{extra.readline('options.txt', 3)}\n0')
      continue

    folder_display = extra.readline('options.txt', 2)
    show_tags = extra.readline('options.txt', 3)

    # pretty
    if folder_display == '1':
      for i, x in enumerate(folders):
        print(str(i+1) + '. ' + folders_pretty[i])
    # raw
    else:
      for i, x in enumerate(folders):
        print(str(i+1) + '. .../' + folders[i])

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

    # settings
    if selection == 0:
      while True:
        extra.clear()
        size = os.get_terminal_size()
        print('Options\n\n0. Back\n1. Update\n2. Text Speed\n3. Folder Display\n4. Show Tags (experimental)\n5. Sort Tags (experimental)')
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
          os.system("printf '%b' 'updating... '; git pull origin release")
          input('> Restart to finish updating')

        elif opt_sel == 2:
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
          input('succeeded! > ')

        elif opt_sel == 3:
          while True:
            extra.clear()
            print('Options\n\nDisplaying file names: ', end='')
            if extra.readline('options.txt', 2) == '0':
              print('raw')
            else:
              print('formatted')
            print('Display as:\n\n1. Formatted\n2. Raw\n')
            try: file_display = input('> ')
            except KeyboardInterrupt: break
            try:
              file_display = int(file_display)
              # selection = int(selection)
            except ValueError:
              print("Input a number")
              continue

            if file_display == 1:
              extra.writeline('options.txt', 2, '1')
              input('succeeded! > ')
              break
            elif file_display == 2:
              extra.writeline('options.txt', 2, '0')
              input('succeeded! > ')
              break
            else: continue

        elif opt_sel == 4:
          while True:
            extra.clear()
            print('Options\n\nShowing tags: ', end='')
            if extra.readline('options.txt', 3) == '0':
              print('false')
            else:
              print('true')

            print('Display as:\n\n1. Hidden\n2. Shown')
            try: tags_shown = input('> ')
            except KeyboardInterrupt: break

            try:
              tags_shown = int(tags_shown)
            except ValueError: continue

            if tags_shown == 1:
              extra.writeline('options.txt', 3, 0)
              input('succeeded! > ')
              break
            elif tags_shown == 2:
              extra.writeline('options.txt', 3, 1)
              input('succeeded! > ')
              break
            else:
              continue

        elif opt_sel == 5:
          while True:
            extra.clear()
            print('Options\n\nSorting tags: ', end='')
            if extra.readline('options.txt', 4) == '0':
              print('false')
            else:
              print('true')

            print('Display as:\n\n1. Not sorted\n2. Sorted')
            try: tags_shown = input('> ')
            except KeyboardInterrupt: break

            try:
              tags_shown = int(tags_shown)
            except ValueError: continue

            if tags_shown == 1:
              extra.writeline('options.txt', 4, 0)
              input('succeeded! > ')
              break
            elif tags_shown == 2:
              extra.writeline('options.txt', 4, 1)
              input('succeeded! > ')
              break
            else:
              continue

        continue

    # if selection == 'update':
    #   os.system('git pull')

    # if sel

    # chapters = os.listdir('./content/' + folders[sel] + '')

    if not sel > folder_last:
      while True:
        if 'devtools' in os.listdir('./'):
          if 'debug' in extra.readfile('options.txt'):
            genCollections.generate(True, True)
          else:
            genCollections.generate(True)
        else:
          genCollections.generate()
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
        # new meta handling
        meta_author =   ''
        meta_authors =  ''
        meta_rating =   ''
        meta_warnings = ''
        meta_links =    ''
        meta_credits =  ''
        meta_title =    ''
        meta_desc =     ''
        meta_tags =     []
        meta_indent =   '           '
        if '.meta' in os.listdir('./content/' + folders[sel]):
          # meta_author =   ''
          # meta_authors =  ''
          # meta_rating =   ''
          # meta_warnings = ''
          # meta_links =    ''
          # meta_credits =  ''
          # meta_title =    ''

          meta_file = extra.readfile('./content/' + folders[sel] + '/.meta').splitlines()

          # print(str(meta_file))

          for x in meta_file:
            if 'authors:' in x:
              meta_authors = x.replace('authors: ', '')
              meta_authors = meta_authors.replace('authors:', '')
              meta_authors = meta_authors.strip()
            elif 'author:' in x:
              meta_author = x.replace('author: ', '')
              meta_author = meta_author.replace('author:', '')
              meta_author = meta_author.strip()

            if 'rating:' in x: meta_rating = x.replace('rating: ', ''); meta_rating = meta_rating.replace('rating:', '')

            if 'warnings:' in x: meta_warnings = x.replace('warnings: ', ''); meta_warnings.replace('warnings:', '')
            meta_warnings = meta_warnings.strip()

            if 'links:' in x: meta_links = x.replace('links: ', ''); meta_links.replace('links:', '')
            meta_links = meta_links.strip()

            if 'credits:' in x: meta_credits = x.replace('credits: ', ''); meta_credits.replace('credits:', '')
            meta_credits = meta_credits.strip()

            if 'title:' in x: meta_title = x.replace('title: ', ''); meta_title = meta_title.replace('title:', '')
            meta_title = meta_title.strip()

            if 'description:' in x: meta_desc = x.replace('description: ', ''); meta_desc = meta_desc.replace('description:', '')
            meta_desc = meta_desc.strip()

        # newer json meta file
        if 'meta.json' in os.listdir('./content/' + folders[sel]):
          decoder = json.JSONDecoder()
          meta_json = json.loads(extra.readfile(f'./content/{folders[sel]}/meta.json'))

          if 'authors'.capitalize() in meta_json:
            meta_authors = meta_json["authors".capitalize()]

          if 'author'.capitalize() in meta_json:
            meta_author = meta_json["author".capitalize()]

          if 'rating'.capitalize() in meta_json:
            meta_rating = meta_json["rating".capitalize()]

          if 'warnings'.capitalize() in meta_json:
            meta_warnings = meta_json["warnings".capitalize()]

          if 'title'.capitalize() in meta_json:
            meta_title = meta_json["title".capitalize()]

          if 'links'.capitalize() in meta_json:
            meta_links = meta_json["links".capitalize()]

          if 'credits'.capitalize() in meta_json:
            meta_credits = meta_json["credits".capitalize()]

          if 'description'.capitalize() in meta_json:
            meta_desc = meta_json["description".capitalize()]

          if 'tags'.capitalize() in meta_json:
            meta_tags = list(meta_json["tags".capitalize()])

          if 'authors' in meta_json:
            meta_authors = meta_json["authors"]

          if 'author' in meta_json:
            meta_author = meta_json["author"]

          if 'rating' in meta_json:
            meta_rating = meta_json["rating"]

          if 'warnings' in meta_json:
            meta_warnings = meta_json["warnings"]

          if 'title' in meta_json:
            meta_title = meta_json["title"]

          if 'links' in meta_json:
            meta_links = meta_json["links"]

          if 'credits' in meta_json:
            meta_credits = meta_json["credits"]

          if 'description' in meta_json:
            meta_desc = meta_json["description"]

          if 'tags' in meta_json:
            meta_tags = list(meta_json["tags"])

        # print meta
        extra.clear()
        if meta_title != '':
          size = os.get_terminal_size()
          print(textwrap.fill('Title:    ' + meta_title, size.columns))
        else:
          size = os.get_terminal_size()
          print(textwrap.fill('Title:    ' + folders_pretty[sel], size.columns))

        if folder_display == '0':
          size = os.get_terminal_size()
          print(textwrap.fill('Folder:   ./content/' + folders[sel] + '/', size.columns))

        if meta_rating == 'g' or meta_rating == 'G' or meta_rating == 0: print(textwrap.fill('Rating:   \033[0;32mGeneral Audiences', size.columns))
        elif meta_rating == 't' or meta_rating == 'T' or meta_rating == 1: print(textwrap.fill('Rating:   \033[0;36mTeen', size.columns))
        elif meta_rating == 'e' or meta_rating == 'E' or meta_rating == 2: print(textwrap.fill('Rating:   \033[1;33mExplicit', size.columns))
        elif meta_rating == 'a' or meta_rating == 'A' or meta_rating == 3: print(textwrap.fill('Rating:   \033[1;31mAdult', size.columns))
        else: print('Rating:   ???')
        print('\033[0;0;0m', end='')

        if meta_warnings != '':
          size = os.get_terminal_size()
          print(textwrap.fill('Warnings: \033[1m' + meta_warnings + '\033[0;0;0m', size.columns, subsequent_indent=meta_indent))

        if meta_tags != [] and extra.readline('options.txt', 3) == '1':
          print('\nTags: ', end='')
          if extra.readline('options.txt', 4) == '1':
            meta_tags.sort()
          meta_tags_display = str(meta_tags).removeprefix('[')
          meta_tags_display = meta_tags_display.removesuffix(']')
          meta_tags_display = meta_tags_display.replace('\\\'', '\'')
          size = os.get_terminal_size()
          print(textwrap.fill(meta_tags_display, size.columns, subsequent_indent='        '))

        if meta_authors != '' and meta_author == '':
          size = os.get_terminal_size()
          print()
          print(textwrap.fill('Authors:  ' + meta_authors, size.columns, subsequent_indent=meta_indent))

        if meta_author != '':
          size = os.get_terminal_size()
          print()
          print(textwrap.fill('Author:   ' + meta_author, size.columns, subsequent_indent=meta_indent))

        if meta_links != '':
          size = os.get_terminal_size()
          print(textwrap.fill('Links:    ' + meta_links, size.columns, subsequent_indent=meta_indent))

        if meta_credits != '':
          size = os.get_terminal_size()
          print(textwrap.fill('Credits:  ' + meta_credits, size.columns, subsequent_indent=meta_indent))

        if meta_desc != '':
          size = os.get_terminal_size()
          print('\nDesc: ', end='')
          meta_desc = meta_desc.splitlines()
          for i, x in enumerate(meta_desc):
            if x == '':
              continue
            if i == 0:
              print(textwrap.fill(x, size.columns))
            # else: print(' ', end='')
            else:
              print(textwrap.fill(x, size.columns, initial_indent='       ', subsequent_indent='       ', ))

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
              # i = i.strip()
              italic_temp = ''
              i = i.replace('/i*', '\e[3m')
              i = i.replace('*i/', '\e[23m')
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
                  if '/PORT' in i:
                    plit = i.split('/PORT')
                    msg = str(plit[0])
                    portrait = str(plit[1]).replace('/PORT', '')
                    if '/CONT' in msg:
                      msg = msg.replace('/CONT', '')
                      if '/CLRA' in msg:
                        msg = msg.replace('/CLRA', '')
                        text.faceCont(portrait, msg)
                        extra.clear()
                        continue
                      elif '/CLRB' in msg:
                        msg = msg.replace('/CLRB', '')
                        extra.clear()
                        # text.faceCont(portrait)
                      text.faceCont(portrait, msg)
                      continue
                    else:
                      if '/CLRA' in msg:
                        msg = msg.replace('/CLRA', '')
                        text.face(portrait, msg)
                        extra.clear()
                        continue
                      elif '/CLRB' in msg:
                        msg = msg.replace('/CLRB', '')
                        extra.clear()
                      text.face(portrait, msg)
                    if nobr:
                      print('\033[0;0;0m', end='')
                    else:
                      print('\033[0;0;0m')
                    continue
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
            input('Return > ')
            extra.clear()
          except KeyboardInterrupt: break

# while __name__ == '__main__':
#   main()