import os, json, extra, textwrap

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