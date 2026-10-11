import text, extra

# text stuff

def Taimen(file=''):
  """Text display"""
  try:
    formatNames = []
    formatDefs = []

    # format everything
    for i in file:
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
      usingDefs = False
      text_indent = 0

      if i != '':
        textSpeed = float(extra.readline("options.txt", 1).replace("text-speed = ", ""))

        if 'ESC>' not in i:

          # adding definitions for strings of format commands
          if "DEF>" in i:
            formatDef = i.replace("DEF>", '', 1)
            i = i.replace(f"DEF>{formatDef}", '')
            params = formatDef.split(',', 2)
            for num, x in enumerate(params):
              params[num] = params[num].strip()
            if not params[0].endswith(">"):
              params[0] += '>'
            formatNames.append(params[0])
            try: formatDefs.append(params[1].replace(" ", ""))
            except IndexError:
              print('\033[0;31m' + f"error: No second argument in \"{params[0]}\"; did you miss a comma?" + '\033[0;0;0m');
            usingDefs = True
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

          if 'BLD(' in i:
            bold = i[i.find('BLD(') + 4 : i.find(')')]
            i = i.replace(f"BLD({bold})", f"\udff2{bold}\udff3")
          elif 'BLD>' in i:
            # bold = i[i.find('BLD(') + 4 : i.find('>')]
            i = i.replace('BLD>', '\udff2')
            i += '\udff3'

          if 'BOLD(' in i:
            bold = i[i.find('BOLD(') + 4 : i.find(')')]
            i = i.replace(f"BOLD({bold})", f"\udff2{bold}\udff3")
          elif 'BOLD>' in i:
            # bold = i[i.find('BLD(') + 4 : i.find('>')]
            i = i.replace('BOLD>', '\udff2')
            i += '\udff3'

          if 'ITAL(' in i:
            italics = i[i.find('ITAL(') + 5 : i.find(')')]
            i = i.replace(f"ITAL({italics})", f"\udff0{italics}\udff1")
          elif 'ITAL>' in i:
            # bold = i[i.find('BLD(') + 4 : i.find('>')]
            i = i.replace('ITAL>', '\udff0')
            i += '\udff1'

          # other text formatting
          if i.startswith('PORT('):
            portrait = i[i.find('PORT(') + 5 : i.find(')')]
            i = i.replace(f"PORT({portrait})", "", 1)
            i = i.removeprefix(' ')
            # print(f"({portrait}) ', end='')
          elif i.startswith('SPD('):
            try:
              textSpeed = float(i[i.find('SPD(') + 4 : i.find(')')])
              i = i.replace(f"SPD({textSpeed})", "", 1)
            except ValueError:
              print('\033[0;31m' + f"error: Speed \"{i[i.find('SPD(') + 4 : i.find(')')]}\" is not a valid number!" + '\033[0;0;0m');
              continue
          elif i.startswith("NMPLT("):
            nameplate = i[i.find('NMPLT(') + 6 : i.find(')')]
            i = i.replace(f"NMPLT({nameplate})", '', 1)
            i = i.removeprefix(' ')
            if extra.readline("options.txt", 6) == "0":
              nameplate = "<\\none/>"
          elif i.startswith("INDNT("):
            try:
              text_indent = int(i[i.find('INDNT(') + 6 : i.find(')')])
            except ValueError:
              print('\033[0;31m' + f"error: Indent \"{i[i.find('INDNT(') + 6 : i.find(')')]}\" is not a valid number!" + '\033[0;0;0m');
              continue
            i = i.replace(f"INDNT({text_indent})", '', 1)

          if 'SPD(' in i:
            try:
              textSpeed = float(i[i.find('SPD(') + 4 : i.find(')')])
            except ValueError:
              print('\033[0;31m' + f"error: Speed \"{i[i.find('SPD(') + 4 : i.find(')')]}\" is not a valid number!" + '\033[0;0;0m');
              continue
            i = i.replace(f"SPD({textSpeed})", '', 1)

          if 'PORT(' in i:
            portrait = i[i.find('PORT(') + 5 : i.find(')')]
            i = i.replace(f"PORT({portrait})", '', 1)
            i = i.removeprefix(' ')
            # print(f"({portrait}) ', end='')

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
              print('\033[0;31m' + f"error: Indent \"{i[i.find('INDNT(') + 6 : i.find(')')]}\" is not a valid number!" + '\033[0;0;0m');
              continue
            i = i.replace(f"INDNT({text_indent})", '', 1)

          if 'BLD(' in i:
            bold = i[i.find('BLD(') + 4 : i.find(')')]
            i = i.replace(f"BLD({bold})", f"\udff2{bold}\udff3")
          elif 'BLD>' in i:
            # bold = i[i.find('BLD(') + 4 : i.find('>')]
            i = i.replace('BLD>', '\udff2')
            i += '\udff3'
          if 'BOLD(' in i:
            bold = i[i.find('BOLD(') + 4 : i.find(')')]
            i = i.replace(f"BOLD({bold})", f"\udff2{bold}\udff3")
          elif 'BOLD>' in i:
            # bold = i[i.find('BLD(') + 4 : i.find('>')]
            i = i.replace('BOLD>', '\udff2')
            i += '\udff3'

          if 'ITAL(' in i:
            italics = i[i.find('ITAL(') + 5 : i.find(')')]
            i = i.replace(f"ITAL({italics})", f"\udff0{italics}\udff1")
          elif 'ITAL>' in i:
            # bold = i[i.find('BLD(') + 4 : i.find('>')]
            i = i.replace('ITAL>', '\udff0')
            i += '\udff1'

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
        print(line_indent, end="")
        text.display(i, textSpeed, continue_text, clear, portrait, nameplate, nobr)

        print('\033[0m', end='')
      # if i == len(file):
      #   print()

    # set the indent
    try:
      line_indent = " " * int(extra.readline("options.txt", 5))
      line_indent += " " * text_indent
    except: line_indent = ""

    input(f"{line_indent}Return > ")
    extra.clear()

  except KeyboardInterrupt: pass