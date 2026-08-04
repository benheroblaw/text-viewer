import os, datetime, textwrap

os.chdir(os.path.expanduser('~/.local/share/prokid/text-porn/devtools'))

def readfile(file=""):
  """Reads a file."""
  with open(file) as f:
    return f.read()
def readline(file="", line=1):
  """Reads a line from a file.
  Lines start at 1."""
  line -= 1
  try:
    with open(file) as f:
      data = f.readlines()
      return data[line].replace("\n", "")
  except: return "error"

def getTerminalWidth():
  save = os.get_terminal_size()
  return int(save.columns)
dashes = '-' * getTerminalWidth()

size = os.get_terminal_size()
class terminal:
  width = size.columns

def runCommands(command=''):

  if command == 'help':
    print(readfile('help'))
    print()

  elif command == 'copypush' or command == 'releasepush':
    os.system('shopt -s dotglob; cd ~/.local/share/prokid/text-porn; cp --verbose * ~/.local/share/prokid/text-viewer;')
    date = datetime.datetime.now()
    os.system('cd ' + os.path.expanduser('~/.local/share/prokid/text-viewer') + '; git add -A; git commit -m ' + str(date.strftime('%m')) + '/' + str(date.strftime('%d')) + '-' + str(date.strftime('%H')) + ':' + date.strftime('%M') + '; git push origin release')

  elif command == 'devpush':
    date = datetime.datetime.now()
    os.system('cd ~/.local/share/prokid/text-porn; git add -A; git commit -m ' + str(date.strftime('%m')) + '/' + str(date.strftime('%d')) + '-' + str(date.strftime('%H')) + ':' + date.strftime('%M') + '; git push origin master')

  elif command == 'test' or command == 'viewer':
    os.system("gnome-terminal -e 'bash -c \" python3 ~/.local/share/prokid/text-porn/ ;bash\"'")

  elif command == 'fullpush':
    print(dashes + '\ndev\n')
    date = datetime.datetime.now()
    os.system('cd ~/.local/share/prokid/text-porn; git add -A; git commit -m ' + str(date.strftime('%m')) + '/' + str(date.strftime('%d')) + '-' + str(date.strftime('%H')) + ':' + date.strftime('%M') + '; git push origin master')

    print(dashes)

    print('release\n')
    os.system('shopt -s dotglob; cd ~/.local/share/prokid/text-porn; cp --verbose * ~/.local/share/prokid/text-viewer;')
    date = datetime.datetime.now()
    os.system('cd ' + os.path.expanduser('~/.local/share/prokid/text-viewer') + '; git add -A; git commit -m ' + str(date.strftime('%m')) + '/' + str(date.strftime('%d')) + '-' + str(date.strftime('%H')) + ':' + date.strftime('%M') + '; git push origin release')


  else:
    try: exec(command)
    except: os.system(command)

def parse():
  output = []
  command = input('devtools@text-viewer> ')
  output += command.split('; ')
  output += command.split(';')

  output = list(set(output))
  # print(output)
  for i in output:
    runCommands(i)

os.system('clear')
while __name__ == "__main__":
  parse()