import text, extra

def ansi_code(code=""):
  return f"\033[{code}m"

# text stuff

def Taimen(file='', path=""):
  """Text display"""


  # ooh-hoo-hoo we're doing imports :P
  file_contents = extra.readfile(file).splitlines()
  file_contents = [x for x in file_contents if x]
  imported = list()
  for num, i in enumerate(file_contents):
    if i.startswith("IMPORT>") and "ESC>" not in i:
      # output = file.replace("")
      statement = i
      file_contents[num] = ""
      if statement != "":
        imported_raw = str()
        try:
          imported_raw = extra.readfile(path + "/" + statement.replace("IMPORT>", "", 1).strip() + ".defs")
          for i in imported_raw.splitlines():
            if i.startswith("DEF>"):
              imported.append(i)
          # break
        except FileNotFoundError:
          try:
            imported_raw = extra.readfile(path + "/" + statement.replace("IMPORT>", "", 1).strip() + ".def")
            for i in imported_raw.splitlines():
              if i.startswith("DEF>"):
                imported.append(i)
          except FileNotFoundError:
            try:
              print('\033[0;31m' + f"Import {statement.replace("IMPORT>", "", 1).strip()} not found!" + "\033[0m")
              line_indent = " " * int(extra.readline("options.txt", 5))
              line_indent += " " * text_indent
            except: line_indent = ""
            input(f"\n{line_indent}Return > ")
            return
  file_contents = imported + file_contents
  file_contents = [x for x in file_contents if x]

  try:
    formatNames = []
    formatDefs = []

    # if not file.endswith(".scri"):
    #   file += ".scri"

    # format everything
    for num, i in enumerate(file_contents):
      if 'CMT>' in i:
        continue
      if 'CMT<' in i:
        comment = i[i.find('CMT<')+4 : i.find('>')]
        i = i.replace(f"CMT<{comment}>", "")
        i = i.removeprefix(' ')

      nobr = False
      continue_text = False
      clear = 'none'
      portrait, nameplate = '<\\none/>', '<\\none/>'
      # usingDefs = False
      text_indent = 0

      if i != '':
        textSpeed = float(extra.readline("options.txt", 1).replace("text-speed = ", ""))

        if 'ESC>' not in i:

          # adding definitions for strings of format commands
          if "DEF>" in i:
            disallowedNames = [
              "DEF",
              "ESC",
              "CMT",
              "CONT",
              "CLRA",
              "CLRB",
              # reset
              "RES",
              "RESET",
              # background colors
              "BGWHI",
              "BGRED",
              "BGBLU",
              "BGGRN",
              "BGYLW",
              "BGPNK",
              "BGCYN",
              "BGPUR",
              "BGLME",
              "BGGRY",
              "BGBLK",
              # light colors
              "LGRN",
              "LGRY",
              # dark colors
              "DGRY",
              # normal colors
              "RED",
              "BLU",
              "GRN",
              "YLW",
              "PNK",
              "CYN",
              "PUR",
              "WHI",
              "LME",
              "GRY",
              "BLK",
              # other stuff
              "BLD",
              "BOLD",
              "ITAL",
              "PORT",
              "IMPORT",
              "SPD",
              "NMPLT",
              "INDNT",
            ]

            formatDef = i.replace("DEF>", '', 1)
            i = i.replace(f"DEF>{formatDef}", '')
            params = formatDef.split(',', 2)
            # make sure the thing has a definition
            if params[0] == "":
              print(ansi_code("0;31") + f"Error on line {num+1}: Missing name for definition" + ansi_code("0"))
              print()
              break
            # strip everything
            for num, x in enumerate(params):
              params[num] = params[num].strip()
            # no redefining builtins.
            if params[0].upper().removesuffix(">") in disallowedNames:
              print("\033[0;31m" + f"Error on line {num+1}: Cannot redefine built-in command \"{params[0].upper().removesuffix(">")}>\"" + "\033[0m")
              print()
              break
            # add a greater-than sign in case you forgot :)
            if not params[0].endswith(">"):
              params[0] += '>'
            formatNames.insert(0, params[0])
            # remove every space from the defs
            try: formatDefs.insert(0, params[1].replace(" ", ""))
            except IndexError:
              print('\033[0;31m' + f"Error on line {num+1}: No second argument in \"{params[0]}\"; did you miss a comma?" + ansi_code(0));
            # usingDefs = True
            continue

          if "CONT>" in i:
            continue_text = True
            i = i.replace('CONT>', '', 1)

          if 'NOBR>' in i:
            nobr = True
            i = i.replace('NOBR>', '', 1)

          if 'CLRA>' in i:
            clear = 'after'
            i = i.replace('CLRA>', '', 1)

          if 'CLRB>' in i:
            clear = 'before'
            i = i.replace('CLRB>', '', 1)

          if "BR>" in i or "BREAK>" in i:
            i = i.replace("BR>", "\uda00")
            i = i.replace("BREAK>", "\uda00")

          # check for custom format cmds
          # HOLY FUCKING SHIT IT WORKS!!!!!!!!!!!!!!!!!!!!! YEAAAAAAAAAAAAAAAASSSSSSSSSSSSSSSSSSSSS!!!!!!!!!!!!!!!
          if formatNames != []:
            for num, name in enumerate(formatNames):
              if formatNames[num] in i:
                i = i.replace(formatNames[num], formatDefs[num])

          # reset
          if 'RES>' in i:
              i = i.replace('RES>', '\ud7fc')
          if 'RESET>' in i:
              i = i.replace('RESET>', '\ud7fc')

          # background colors
          if "BGWHI>" in i:
            i = i.replace("BGWHI>", '\udb00')

          if "BGRED>" in i:
            i = i.replace("BGRED>", '\udb01')

          if 'BGBLU>' in i:
              i = i.replace('BGBLU>', '\udb02')

          if 'BGGRN>' in i:
              i = i.replace('BGGRN>', "\udb03")

          if 'BGYLW>' in i:
              i=i.replace('BGYLW>', '\udb04')

          if 'BGPNK>' in i:
              i = i.replace('BGPNK>', '\udb05')

          if 'BGCYN>' in i:
              i = i.replace('BGCYN>', '\udb06')

          if 'BGPUR>' in i:
              i = i.replace('BGPUR>', '\udb07')

          if 'BGLME>' in i:
              i = i.replace('BGLME>', '\udb08')

          if 'BGGRY>' in i:
              i = i.replace('BGGRY>', '\udb09')

          if "BGBLK>" in i:
            i = i.replace('BGBLK>', '\udb0a')

          if "BGORN>" in i:
            i = i.replace("ORN>", "\udb0b")

          # light colors
          if 'LGRN>' in i:
              i = i.replace('LGRN>', '\ud807')

          if 'LGRY>' in i:
              i =i.replace('LGRY>', '\ud808')

          if 'LBLU>' in i:
              i = i.replace('LBLU>', '\ud809')

          # dark colors
          if 'DGRY>' in i:
              i =i.replace('DGRY>', '\ud80a')

          # colors
          if 'RED>' in i:
              i = i.replace('RED>', '\ud7fd')

          if 'BLU>' in i:
              i = i.replace('BLU>', '\ud7fe')

          if 'GRN>' in i:
              i = i.replace('GRN>', "\ud7ff")

          if 'YLW>' in i:
              i=i.replace('YLW>', '\ud800')

          if 'PNK>' in i:
              i = i.replace('PNK>', '\ud801')

          if 'CYN>' in i:
              i = i.replace('CYN>', '\ud802')

          if 'PUR>' in i:
              i = i.replace('PUR>', '\ud803')

          if 'WHI>' in i:
              i = i.replace('WHI>', '\ud804')

          if 'LME>' in i:
              i = i.replace('LME>', '\ud805')

          if 'GRY>' in i:
              i = i.replace('GRY>', '\ud806')

          if "BLK>" in i:
            i = i.replace('BLK>', '\ud80b')

          if "ORN>" in i:
            i = i.replace("ORN>", "\ud80c")



          # other text formatting

          # check for specified bold area
          if 'BLD(' in i:
            bold = i[i.find('BLD(') + 4 : i.find(')')]
            i = i.replace(f"BLD({bold})", f"\udff2{bold}\udff3")
          # bold the whole line
          elif 'BLD>' in i:
            i = i.replace('BOLD>', '\udff2')
            i = "" + i + '\udff3'

          # same as above
          if 'BOLD(' in i:
            bold = i[i.find('BOLD(') + 5 : i.find(')')]
            i = i.replace(f"BOLD({bold})", f"\udff2{bold}\udff3")
          elif 'BOLD>' in i:
            i = i.replace('BOLD>', '\udff2')
            i = "" + i + '\udff3'

          # check for specified italic area
          if 'ITAL(' in i:
            italics = i[i.find('ITAL(') + 5 : i.find(')')]
            i = i.replace(f"ITAL({italics})", f"\udff0{italics}\udff1")
          # italicize the whole line
          elif 'ITAL>' in i:
            i = i.replace('ITAL>', '\udff0')
            i = "" + i + '\udff1'

          # check for portrait
          if i.startswith('PORT('):
            portrait = i[i.find('PORT(') + 5 : i.find(')')]
            i = i.replace(f"PORT({portrait})", "", 1)
            i = i.removeprefix(' ')
          # or speed
          elif i.startswith('SPD('):
            try:
              textSpeed = float(i[i.find('SPD(') + 4 : i.find(')')])
            except ValueError:
              print('\033[0;31m' + f"error: Speed \"{i[i.find('SPD(') + 4 : i.find(')')]}\" is not a valid number!" + '\033[0m');
              continue
            i = i.replace(f"SPD({textSpeed})", "", 1)
            i = i.replace(f"SPD({int(textSpeed)})", "", 1)
          # or nameplate
          elif i.startswith("NMPLT("):
            nameplate = i[i.find('NMPLT(') + 6 : i.find(')')]
            i = i.replace(f"NMPLT({nameplate})", '', 1)
            i = i.removeprefix(' ')
            if extra.readline("options.txt", 6) == "0":
              nameplate = "<\\none/>"
          # or indent
          elif i.startswith("INDNT("):
            try:
              text_indent = int(i[i.find('INDNT(') + 6 : i.find(')')])
            except ValueError:
              print('\033[0;31m' + f"error: Indent \"{i[i.find('INDNT(') + 6 : i.find(')')]}\" is not a valid number!" + '\033[0m');
              continue
            i = i.replace(f"INDNT({text_indent})", '', 1)

          # check all of that stuff again
          if 'SPD(' in i:
            try:
              textSpeed = float(i[i.find('SPD(') + 4 : i.find(')')])
            except ValueError:
              print('\033[0;31m' + f"error: Speed \"{i[i.find('SPD(') + 4 : i.find(')')]}\" is not a valid number!" + '\033[0m');
              continue
            i = i.replace(f"SPD({textSpeed})", '', 1)
            i = i.replace(f"SPD({int(textSpeed)})", "", 1)

          if 'PORT(' in i:
            portrait = i[i.find('PORT(') + 5 : i.find(')')]
            i = i.replace(f"PORT({portrait})", '', 1)
            i = i.removeprefix(' ')

          if 'NMPLT(' in i:
            nameplate = i[i.find('NMPLT(') + 6 : i.find(')')]
            i = i.replace(f"NMPLT({nameplate})", '', 1)
            i = i.removeprefix(' ')
            if extra.readline("options.txt", 6) == "0":
              nameplate = "<\\none/>"

          if 'INDNT(' in i:
            try:
              text_indent = int(i[i.find('INDNT(') + 6 : i.find(')')])
            except ValueError:
              print('\033[0;31m' + f"error: Indent \"{i[i.find('INDNT(') + 6 : i.find(')')]}\" is not a valid number!" + '\033[0m');
              continue
            i = i.replace(f"INDNT({text_indent})", '', 1)

          if 'BLD(' in i:
            bold = i[i.find('BLD(') + 4 : i.find(')')]
            i = i.replace(f"BLD({bold})", f"\udff2{bold}\udff3")
          elif 'BLD>' in i:
            i = i.replace('BOLD>', '')
            i = "\udff2" + i + '\udff3'
          if 'BOLD(' in i:
            bold = i[i.find('BOLD(') + 5 : i.find(')')]
            i = i.replace(f"BOLD({bold})", f"\udff2{bold}\udff3")
          elif 'BOLD>' in i:
            i = i.replace('BOLD>', '')
            i = "\udff2" + i + '\udff3'

          while 'BLD(' in i:
            bold = i[i.find('BLD(') + 4 : i.find(')')]
            i = i.replace(f"BLD({bold})", f"\udff2{bold}\udff3")
          while 'BOLD(' in i:
            bold = i[i.find('BOLD(') + 5 : i.find(')')]
            i = i.replace(f"BOLD({bold})", f"\udff2{bold}\udff3")

          if 'ITAL(' in i:
            italics = i[i.find('ITAL(') + 5 : i.find(')')]
            i = i.replace(f"ITAL({italics})", f"\udff0{italics}\udff1")
          elif 'ITAL>' in i:
            i = i.replace('ITAL>', '')
            i = "\udff0" + i + '\udff1'

          while 'ITAL(' in i:
            italics = i[i.find('ITAL(') + 5 : i.find(')')]
            i = i.replace(f"ITAL({italics})", f"\udff0{italics}\udff1")

        i = i.replace('ESC>', '', 1)

        # set the indent
        try:
          line_indent = " " * int(extra.readline("options.txt", 5))
          line_indent += " " * text_indent
        except: line_indent = ""

        # pass everything to text display
        if i.strip() != "":
          print(line_indent, end="")
          if i == "\uda00":
            print('\n')
          else:
            text.display(i, textSpeed, continue_text, clear, portrait, nameplate, nobr)

          print('\033[0m', end='')

    # properly indent return text
    try:
      line_indent = " " * int(extra.readline("options.txt", 5))
      line_indent += " " * text_indent
    except: line_indent = ""

    # let the user know the script is done
    input(f"{line_indent}Return > ")
    extra.clear()

  except KeyboardInterrupt: pass