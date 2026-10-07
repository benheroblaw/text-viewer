import os

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
  print('generating collections...')
  if debug:
    print('\033[0;32m' + 'debug mode!' + '\033[0;38;5;255m')
  print()
  if logging:
    print(f'first directory: {str(os.getcwd())}\n\nfolders with .folders:')
  for i in os.scandir('./content/'):
    if i.is_dir():
      if '.folders' in os.listdir(i):
        os.chdir('./content/' + i.name)
        if logging:
          print(f'  {str(os.getcwd())}')

        folders = readfile('./.folders').splitlines()
        for number, folder in enumerate(folders):
          if folder.startswith('#'):
            if logging:
              print(f'line {number+1} commented, skipping...')
          else:
            folder = os.path.expanduser(f'{extra_path}/content/{folder}')
            print(f'file path to search: {folder}')
            try:
              print('files to link:')
              for direct in os.listdir(folder):
                if direct.endswith('.scri'):
                  direct = direct.replace("'", "\\'")
                  if logging:
                    print(f'  {direct}')
                  os.system(f'printf "%b" "   "; ln -s -f -v {folder}{str(direct)}')

            except FileNotFoundError:
              if logging: print(f'could not link files in: {folder}')

            print('\nremoving broken links in folders:')
            for i in os.listdir(f'{extra_path}/content/'):
              print(' ' + i)
              output = i.replace('\'', '\\\'')
              output = output.replace('"', '\\"')
              os.system(f'find {extra_path}/content/{output}/*.scri -xtype l -delete'.replace('//', '/'))
            print()
        os.chdir(extra_path)

  print('\033[0;0;0m', end='')

  if debug:
    input('done, waiting for input: ')