import os, json, averylib, textwrap, time

# meta handling
def Mako(folder, sel, folders_pretty, folder_display, show_tags):
  """meta.json handler"""

  output = folder
  output = output.removeprefix('_')
  output = output.replace("_", ' ')
  output = output.replace('zzz-', '_')
  folder_pretty = output

  candiru_folder = folder.replace("\\", "/")

  # new meta handling
  meta_author =   ''
  meta_authors =  ''
  meta_rating =   ''
  meta_warnings = ''
  meta_links =    ''
  meta_credits =  ''
  meta_title =    ''
  meta_desc =     ''
  meta_tags =     list()
  meta_ships =    list()
  meta_indent =   '           '

  while not "meta.json" in os.listdir('./content/' + folder):
    if os.path.abspath("./content/" + folder) == os.path.abspath("./content"):
      print("\033[2m" + "No meta.json in ./content/" + folder.replace("\\", "/").replace("/..", "") + "\033[0m")
      break
    folder += "/.."

  # newer json meta file
  if 'meta.json' in os.listdir('./content/' + folder):
    try:
      meta_json = json.loads(averylib.readfile(f'./content/{folder}/meta.json'))


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
        meta_ships = list(meta_json["relationships".capitalize()])

      elif 'ships'.capitalize() in meta_json:
        meta_ships = list(meta_json["relationships".capitalize()])

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
        meta_ships = list(meta_json["relationships"])

      elif 'ships' in meta_json:
        meta_ships = list(meta_json["ships"])


      # print meta
      averylib.clear()
      if meta_title.strip() != '':
        size = os.get_terminal_size()
        print(textwrap.fill('Title:    ' + "\033[1m" + meta_title + "\033[m", size.columns))
        print(f"Folder:   ./content/{candiru_folder}/\n")
      else:
        size = os.get_terminal_size()
        print(textwrap.fill('Title:    ' + "\033[1m" + folder_pretty + "\033[m", size.columns))
        print(f"Folder:   ./content/{candiru_folder}/\n")

      if folder_display == '0':
        size = os.get_terminal_size()
        print(textwrap.fill('Folder:   ' + '\033[1m' + './content/' + folder + '/', size.columns), end='\033[0m\n')

      if meta_rating == 'g' or meta_rating == 'G' or meta_rating == 0:   print(textwrap.fill('Rating:   \033[1;32mGeneral Audiences', size.columns))
      elif meta_rating == 't' or meta_rating == 'T' or meta_rating == 1: print(textwrap.fill('Rating:   \033[1;36mTeen', size.columns))
      elif meta_rating == 'e' or meta_rating == 'E' or meta_rating == 2: print(textwrap.fill('Rating:   \033[1;33mExplicit', size.columns))
      elif meta_rating == 'a' or meta_rating == 'A' or meta_rating == 3: print(textwrap.fill('Rating:   \033[1;31mAdult', size.columns))
      else: print('Rating:   ???')
      print('\033[0;0;0m', end='')

      if meta_warnings != '':
        size = os.get_terminal_size()
        print(textwrap.fill('Warnings: ' + "\033[1m" + meta_warnings + '\033[m', size.columns, subsequent_indent=meta_indent))

      # tags an ships are experimental
      if meta_tags != [] and show_tags == '1':
        print('\nTags:  ' +
              "\033[1m", end='')
        if averylib.readline('options.txt', 4) == '1':
          meta_tags.sort()
        meta_tags_display = str(meta_tags).removeprefix('[')
        meta_tags_display = meta_tags_display.removesuffix(']')
        meta_tags_display = meta_tags_display.replace('\\\'', '\'')
        size = os.get_terminal_size()
        print(textwrap.fill(meta_tags_display, size.columns - 8, subsequent_indent='        '))
        print("\033[m", end="")
      if meta_ships != [] and show_tags == '1':
        print('Ships: ', end="\033[1m")
        if averylib.readline('options.txt', 4) == '1':
          meta_ships.sort()
        meta_ships_display = str(meta_ships).removeprefix('[')
        meta_ships_display = meta_ships_display.removesuffix(']')
        meta_ships_display = meta_ships_display.replace('\\\'', '\'')
        size = os.get_terminal_size()
        print(textwrap.fill(meta_ships_display, size.columns - 8, subsequent_indent='        '))
        print(end="\033[m")

      if meta_authors != '' and meta_author == '':
        size = os.get_terminal_size()
        print()
        print(textwrap.fill('Authors:  ' + "\033[1m" + meta_authors + "\033[m", size.columns, subsequent_indent=meta_indent))

      if meta_author != '':
        size = os.get_terminal_size()
        print()
        print(textwrap.fill('Author:   ' + "\033[1m" + meta_author + "\033[m", size.columns, subsequent_indent=meta_indent))

      if meta_links != '':
        size = os.get_terminal_size()
        print(textwrap.fill('Links:    ' + "\033[1m" + meta_links + "\033[m", size.columns, subsequent_indent=meta_indent))

      if meta_credits != '':
        size = os.get_terminal_size()
        print(textwrap.fill('Credits:  ' + "\033[1m" + meta_credits + "\033[m", size.columns, subsequent_indent=meta_indent))

      if meta_desc != '':
        size = os.get_terminal_size()
        print('\nDesc: ', end="\033[1m")
        meta_desc = meta_desc.splitlines()
        for i, x in enumerate(meta_desc):
          if x == '':
            continue
          if i == 0:
            print(textwrap.fill(x, size.columns))
          # else: print(' ', end='')
          else:
            print(textwrap.fill(x, size.columns, initial_indent='       ', subsequent_indent='       ', ))
        print(end="\033[m")
    except json.decoder.JSONDecodeError:
      print('\033[0;38;5;196m' + f'Invalid JSON in ./content/{folder}/meta.json!\033[m')

  else: print(f"Folder: ./content/{candiru_folder}")