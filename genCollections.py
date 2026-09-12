import os

def readfile(file=""):
  """Reads a file."""
  with open(file) as f:
    return f.read()

def generate(logging=False, debug=False):
  extra_path = readfile('extra/path').strip()
  if logging:
    print('generating collections...')
    print(f'first directory: {str(os.getcwd())}\nfolders with .folders:')
  for i in os.scandir('./content/'):
    if i.is_dir():
      if '.folders' in os.listdir(i):
        os.chdir('./content/' + i.name)
        if logging:
          print(f'  {str(os.getcwd())}')

        folders = readfile('./.folders').splitlines()
        for folder in folders:
          if folder.startswith('#'):
            if logging:
              print(i.name + ': commented, skipping...')
          else:
            folder = os.path.expanduser(f'~/.local/share/bhrobla/{extra_path}/content/{folder}')
            print(f'file path to search: {folder}')
            try:
              print('files to link:')
              for direct in os.listdir(folder):
                if direct.endswith('.scri'):
                  direct = direct.replace("'", "\\'")
                  if logging:
                    print(f'  {direct}')
                  os.system(f'ln -s -f {folder}{str(direct)}')

            except FileNotFoundError:
              if logging: print(f'could not link files in: {folder}')

            for i in os.listdir(os.path.expanduser(f'~/.local/share/bhrobla/{extra_path}/content/')):
              print(i)
              output = i.replace('\'', '\\\'')
              output = output.replace('"', '\\"')
              os.system(f'find ~/.local/share/bhrobla/{extra_path}/content/{output}/*.scri -xtype l -delete'.replace('//', '/'))
        os.chdir(os.path.expanduser(f'~/.local/share/bhrobla/{extra_path}'))

  if debug:
    input('done, waiting for input: ')