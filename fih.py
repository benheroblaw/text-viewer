import json, os, extra, textwrap, genCollections, text

# folder selector
def Barracuda():
  """Folder display"""
  while True:
    print('\33]0;benheroblaw\'s text viewer :3\a', end='', flush=True)
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
      Sixgill()

    # pass it to Candiru
    elif selection <= len(folders):
      Candiru(sel, folder_last, folders, folders_pretty, folder_display)

    else:
      # input('wtf')
      pass



# chapter selector
def Candiru(sel, folder_last, folders, folders_pretty, folder_display):
  """Chapter select"""
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

      Mako(folders, sel, folders_pretty, folder_display)

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
        Taimen(chap_story)



# meta handling
def Mako(folders, sel, folders_pretty, folder_display):
  """meta.json handler"""
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
  meta_relationships = []
  meta_indent =   '           '
# removing the legacy meta

  # newer json meta file
  if 'meta.json' in os.listdir('./content/' + folders[sel]):
    decoder = json.JSONDecoder()
    try:
      meta_json = json.loads(extra.readfile(f'./content/{folders[sel]}/meta.json'))


      # Capitalized
      if 'authors'.capitalize() in meta_json:
        meta_authors = meta_json["authors".capitalize()]

      elif 'author'.capitalize() in meta_json:
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

      if 'relationships'.capitalize() in meta_json:
        meta_relationships = list(meta_json["relationships".capitalize()])

      elif 'ships'.capitalize() in meta_json:
        meta_relationships = list(meta_json["relationships".capitalize()])

      # not capitalized
      if 'authors' in meta_json:
        meta_authors = meta_json["authors"]

      elif 'author' in meta_json:
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

      if 'relationships' in meta_json:
        meta_relationships = list(meta_json["relationships"])

      elif 'ships' in meta_json:
        meta_relationships = list(meta_json["ships"])

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

      # tags an ships are experimental
      if meta_tags != [] and extra.readline('options.txt', 3) == '1':
        print('\nTags:  ', end='')
        if extra.readline('options.txt', 4) == '1':
          meta_tags.sort()
        meta_tags_display = str(meta_tags).removeprefix('[')
        meta_tags_display = meta_tags_display.removesuffix(']')
        meta_tags_display = meta_tags_display.replace('\\\'', '\'')
        size = os.get_terminal_size()
        print(textwrap.fill(meta_tags_display, size.columns - 8, subsequent_indent='        '))
      if meta_relationships != [] and extra.readline('options.txt', 3) == '1':
        print('Ships: ', end='')
        if extra.readline('options.txt', 4) == '1':
          meta_relationships.sort()
        meta_relationships_display = str(meta_relationships).removeprefix('[')
        meta_relationships_display = meta_relationships_display.removesuffix(']')
        meta_relationships_display = meta_relationships_display.replace('\\\'', '\'')
        size = os.get_terminal_size()
        print(textwrap.fill(meta_relationships_display, size.columns - 8, subsequent_indent='        '))

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
    except json.decoder.JSONDecodeError:
      print(f'Invalid JSON in: ./content/{folders[sel]}/meta.json')



# settings
def Sixgill():
  """Settings"""
  while True:
    extra.clear()
    size = os.get_terminal_size()
    print('Options\n\n0. Back\n1. Update\n2. Text Speed\n3. Folder Display\n4. Show Tags (experimental)')
    if extra.readline('options.txt', 3) != '0':
      print('5. Sort Tags (experimental)')
    print("\nDist: ", end='')
    if 'portable' in os.listdir('extra/'): print('Portable')
    else: print('Base')
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
      print('Options\n\nCurrent speed: ' + extra.readline('options.txt', 1))
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
      # text.speed = float(speed)
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
          extra.writeline('options.txt', 4, '0')
          input('succeeded! > ')
          break
        elif tags_shown == 2:
          extra.writeline('options.txt', 4, '1')
          input('succeeded! > ')
          break
        else:
          continue

    continue


# text stuff
def Taimen(file=''):
  """Text display"""
  try:
    for i in file:
      nobr = False
      cont = False
      clear = 'none'
      if i != '':
        textSpeed = float(extra.readline("options.txt", 1).replace("text-speed = ", ""))

        if 'ESC>' not in i:

          if "CONT>" in i:
            i = i.replace('CONT>', '', 1)
            cont = True

          if 'NOBR>' in i:
            i = i.replace('NOBR>', '', 1)
            nobr = True

          if 'CLRA>' in i:
            i = i.replace('CLRA>', '', 1)
            clear = 'after'

          if 'CLRB>' in i:
            i = i.replace('CLRB>', '', 1)
            clear = 'before'

          if 'SPD<' in i:
            try: textSpeed = float(i[i.find('SPD<') + 4 : i.find('>')])
            except ValueError: print('error: SPD is not a valid number!')

            i = i.replace(f'SPD<{textSpeed}>', '', 1)
            i = i.replace(f'SPD<{int(textSpeed)}>', '', 1)

          if 'CMT<' in i:
              comment = i[i.find('CMT<') : i.find('>')+1]
              i = i.replace(comment, '')
              i = i.removeprefix(' ')

          # light colors
          if 'LGRN>' in i:
              i = i.replace('LGRN>', '\ud807', 1)

          if 'LGRY>' in i:
              i =i.replace('LGRY>', '\ud808', 1)

          if 'LBLU>' in i:
              i = i.replace('LBLU>', '\ud809', 1)

          # dark colors
          if 'DGRY>' in i:
              i =i.replace('DGRY>', '\ud80a', 1)

          # colors

          if 'RES>' in i:
              i = i.replace('RES>', '\ud7fc', 1)

          if 'RED>' in i:
              i = i.replace('RED>', '\ud7fd', 1)

          if 'BLU>' in i:
              i = i.replace('BLU>', '\ud7fe', 1)

          if 'GRN>' in i:
              i = i.replace('GRN>', '\ud7ff', 1)

          if 'YLW>' in i:
              i=i.replace('YLW>', '\ud800', 1)

          if 'PNK>' in i:
              i = i.replace('PNK>', '\ud801', 1)

          if 'CYN>' in i:
              i = i.replace('CYN>', '\ud802', 1)

          if 'PUR>' in i:
              i = i.replace('PUR>', '\ud803', 1)

          if 'WHI>' in i:
              i = i.replace('WHI>', '\ud804', 1)

          if 'LME>' in i:
              i = i.replace('LME>', '\ud805', 1)

          if 'GRY>' in i:
              i =i.replace('GRY>', '\ud806', 1)

          # other text formatting
          if 'BLD>' in i:
            i = i.replace('BLD>', '', 1)
            print('\033[1m', end='')

          if 'ITAL<' in i:
              italics = i[i.find('ITAL<') + 5 : i.find('>')]
              i = i.replace(f'ITAL<{italics}>', f'\udff0{italics}\udff1')

          if 'PORT<' in i:
            portrait = i[i.find('PORT<') + 5 : i.find('>')]
            i = i.replace(f'PORT<{portrait}>', '', 1)
            print(f'({portrait}) ', end='')

        i = i.replace('ESC>', '', 1)
        text.text(i, textSpeed, cont, clear)
        if nobr and textSpeed > 0:
          print('\033[0;0;0m', end='')
        else:
          print('\033[0;0;0m')
      # print()
    input('Return > ')
    extra.clear()
  except KeyboardInterrupt: pass