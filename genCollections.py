import os, extra

def readfile(file=""):
  """Reads a file."""
  with open(file) as f:
    return f.read()

def generate(logging=False, debug=False):
  ospath = ''
  if os.name == 'posix':
    ospath = '~/.local/share/bhrobla/'
  elif os.name == 'nt':
    ospath = '~/AppData/Local/bhrobla/'
  extra_path = os.path.expanduser(ospath + readfile('extra/path').strip())
  print('\033[0;38;5;255m' + 'generating collections...')
  if debug:
    print('\033[0;32m' + 'debug mode!' + '\033[0;38;5;255m')
  print()
  if logging:
    print(f'first directory: {str(os.getcwd())}\n\nfolders with .folders:')
  dirs_to_search = list()
  starting_dirs = list()
  for i in os.listdir(os.path.join(".", "content")):
    if ".git" not in i and not i.endswith(".git"):
      starting_dirs.append(os.path.abspath(os.path.join(".", "content", i)))
  for num, name in enumerate(starting_dirs):
    if ".git" in name or name.endswith(".git"):
      continue
    for path in os.scandir(name):
      if path.is_dir() and ".git" not in path.name and not path.name.endswith(".git"):
        dirs_to_search.append(os.path.abspath(path))
  for i in starting_dirs:
    if ".git" not in i and not i.endswith(".git"):
      dirs_to_search.append(i)
  for path in dirs_to_search:
    for i in os.scandir(path):
      if i.is_dir():
        if '.folders' in os.listdir(i):
          os.chdir(os.path.join(path, i))
          if logging:
            print(f'  {str(os.getcwd())}')

          folders = readfile(".folders").splitlines()
          for number, folder in enumerate(folders):
            if folder.startswith('#'):
              if logging:
                print(f'line {number+1} commented, skipping...')
            else:
              folder = os.path.abspath(f'{folder}')
              print(f'\nfile path to search: {folder}')
              try:
                print('files to link:')
                for direct in os.listdir(folder):
                  if direct.endswith('.scri'):
                    # direct = direct.replace("'", "\\'")
                    if logging:
                      print(f'  {direct}')
                    if os.name == "posix":
                      # print(f"{folder}/{str(direct)}")
                      os.system(f'printf "%b" "   "; ln -s -f -v "{folder}/{str(direct)}"')
                    elif os.name == "nt":
                      command = f"mklink {folder.replace("/", "\\")}\\{str(direct)} {os.path.abspath(".")}\\"
                      # print(os.path.abspath("."))
                      print(command)
                      os.system(command)

              except FileNotFoundError:
                if logging: print(f'could not link files in: {folder}')
          os.chdir(extra_path)

  print('\nremoving broken links in folders:')
  ignored = extra.readfile("extra/ignored").strip().splitlines()
  for path in dirs_to_search:
    # for i in ignored:
    if path not in ignored:
      for i in os.scandir(path):
        if i.is_dir() and i.name not in ignored:
          print(" " + i.name)
          # output = i.name.replace('\'', '\\\'')
          output = i.name.replace('"', '\\"')
          if os.name == "posix":
            os.system(f'printf "%b" "  "; find "{path}/{output}/*.scri" -xtype l -delete; printf "%b\n" ""'.replace('//', '/').replace("\\\\", "\\"))
          elif os.name == "nt":
            os.system(f'find {extra_path}/content/{output}/*.scri -xtype l -delete'.replace('//', '/').replace("/", "\\"))
  print()

  print('\033[0;0;0m', end='')

  if debug:
    input('done, waiting for input: ')