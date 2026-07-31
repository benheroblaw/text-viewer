import os, time

if os.name == "posix":
  terminalPath = os.path.expanduser("~/.local/share/prokid/")
elif os.name == "nt":
  print('youre fucked buddy :(')
if not os.path.exists(terminalPath):
  os.makedirs(terminalPath)
os.chdir(terminalPath)

os.system('git clone -b release https://github.com/benheroblaw/text-viewer')
print('\nSuccessfully installed!')
time.sleep(4)