# my little cross-platform library :}
import os, time, random, sys, json, traceback, datetime, subprocess

clearCommand = ""
if os.name == "posix":
  clearCommand = "clear"
elif os.name == "nt":
  clearCommand = "cls"

os.system(clearCommand)
print("averylib: start load...")

# ansi codes are a bitch
def ansi_code(code=""):
  """Returns the provided string, formatted as an ansi code."""
  code = code.replace("\033[", "").replace("m", "")
  return f"\033[{code}m"
def AnsiCode(code=""):
  """Returns the provided string, formatted as an ansi code."""
  return ansi_code(code)

def print_ansi_code(code="", end=""):
  """Prints the string, formatted as an ansi code.
  """
  print(ansi_code(code), end=end)
def PrintAnsiCode(code="", end=""):
  """Prints the string, formatted as an ansi code.
  """
  print_ansi_code(code, end)

def print_bold(msg="", end="\n\r"):
  print(ansi_code("1") + msg + ansi_code("0"), end=end)

textReset = ansi_code("0")

# file management
def createfile(file="", contents=""):
  """Creates a file, errors if the file exists."""
  with open(file, "x") as f:
    f.write(contents)

def writefile(file="", contents=""):
  """Overwrites a file."""
  with open(file, "w") as f:
    f.write(contents)
def writeline(file="", line=1, contents=""):
  """Writes a line to a file.
  Line starts at 1."""
  contents = str(contents)
  line -= 1
  contents += "\n"
  with open(file) as f:
    data = f.readlines()
  # print(data)
  try: data[line] = contents
  except: print("failed to write to " + file); return ResourceWarning
  with open(file, "w") as f:
    f.writelines(data)
def writeJSON(json, file_name):
  if not file_name.endswith(".json"):
    file_name += ".json"
  with open(file_name, "w", encoding="utf-8") as f:
      json.dump(json, f, ensure_ascii=False, indent=4)

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
      return data[line].replace('\n', '')
  except: return "error"

def getlines(file=""):
  """Returns the number of lines in a file."""
  with open(file) as f:
    data = f.readlines()
    return len(data)
def newline(file=""):
  """nonfunctional :C
  It"s supposed to add a line to the end of the file."""
  line = getlines(file) +1
  contents = "\n"
  with open(file) as f:
    data = f.readlines()
  try: data[line] = contents
  except: print("failed to write to: \"" + file + "\"")
  with open(file, "w") as f:
    f.writelines(data)

# terminal management
def clear():
  """Clears the terminal; supports Linux and Windows"""
  os.system(clearCommand)
  print(textReset, end="")
def pos(x, y):
  """Returns the position of the cursor."""
  return "\x1b[" + str(y) + ";" + str(x) + "H"

def terminalName(name):
  print("\33]0;"+name+"\a", end="", flush=True)

def done(end=""):
  """Prints a cute little \"done!\" message"""
  print(ansi_code("0;32") + "done" + textReset + end)

def rmdupes(inputFile):
  """"""
  inputFile = inputFile.removeprefix("'")
  inputFile = inputFile.removesuffix("'")
  outputFile = readfile(os.path.expanduser(inputFile)).splitlines()
  outputFile = list(set(outputFile))
  outputFile = '\n'.join(outputFile)
  writefile(inputFile, outputFile)

Signed32BitIntegerLimit = 2147483647

def Error():
  """Should handle any error."""
  try:
    ErrorScreen()
    print("(" + ErrorLog() + ")")
    print()
    input('Exit > ')
    print("Exiting...")
    exit()
  except KeyboardInterrupt: print("Exiting..."); exit()

def ErrorScreen():
  """Prints a screen that tells you an exception has occurred"""
  clear()
  print(AnsiCode("0;1;31") + "An uncaught exception has occurred!" + AnsiCode("0"))
  traceback.print_exc();
  print()
  print_bold("Please submit this crash report to benheroblaw!")

def ErrorLog():
  """Writes the exception to a file"""
  if not os.path.exists("./logs"):
    os.makedirs("./logs")
  logName = datetime.datetime.now().strftime("%m-%d-%Y_%H-%M-%S_crashreport.txt")
  writefile(os.path.join(os.path.abspath("."), "logs", logName), traceback.format_exc().strip())

  return f"Crash report has been saved to {os.path.abspath(os.path.join(".", "logs", logName))}"


if os.path.exists("./averylib.cmd"):
  print("running averylib.cmd")
  exec(readfile("averylib.cmd"))
else:
  print("no averylib.cmd")

print('averylib: done loading!\n')