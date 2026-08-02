import os

def readfile(file=""):
  """Reads a file."""
  with open(file) as f:
    return f.read()

def generate(logging=True):

  if logging:
    print('generating collections...')

  for i in os.scandir('./content/'):
    if i.is_dir():
      if '.folders' in os.listdir(i):
        # os.system('cd ./content/' + i.name)
        os.chdir('./content/' + i.name)

        folders = readfile('./.folders').splitlines()
        for folder in folders:
          if folder.startswith('#'):
            if logging:
              print(i.name + ': commented, skipping...')
          else:
            for direct in os.listdir(folder):
              if direct.endswith('.scri'):
                direct = direct.replace("'", "\\'")
                if logging:
                  print(direct)
                os.system('ln -s -f ' + folder + str(direct))
        # os.system('cd ../../')
        os.chdir(os.path.expanduser('~/.local/share/prokid/text-porn'))

  if logging:
    print('done')
# generate()
