import text, extra

# text stuff

def Taimen(file=''):
  """Text display"""
  try:
    for i in file:
      nobr = False
      cont = False
      clear = 'none'
      if i != '':
        textSpeed = float(extra.readline("options.txt", 1).replace("text-speed = ", ""))

        if 'ESC>' not in i:

          if "CONT>" in i:
            i = i.replace('CONT>', '', 1)
            cont = True

          if 'NOBR>' in i:
            i = i.replace('NOBR>', '', 1)
            nobr = True

          if 'CLRA>' in i:
            i = i.replace('CLRA>', '', 1)
            clear = 'after'

          if 'CLRB>' in i:
            i = i.replace('CLRB>', '', 1)
            clear = 'before'

          if 'SPD<' in i:
            try: textSpeed = float(i[i.find('SPD<') + 4 : i.find('>')])
            except ValueError: print('error: SPD is not a valid number!')

            i = i.replace(f'SPD<{textSpeed}>', '', 1)
            i = i.replace(f'SPD<{int(textSpeed)}>', '', 1)

          if 'CMT<' in i:
              comment = i[i.find('CMT<') : i.find('>')+1]
              i = i.replace(comment, '')
              i = i.removeprefix(' ')

          # light colors
          if 'LGRN>' in i:
              i = i.replace('LGRN>', '\ud807', 1)

          if 'LGRY>' in i:
              i =i.replace('LGRY>', '\ud808', 1)

          if 'LBLU>' in i:
              i = i.replace('LBLU>', '\ud809', 1)

          # dark colors
          if 'DGRY>' in i:
              i =i.replace('DGRY>', '\ud80a', 1)

          # colors

          if 'RES>' in i:
              i = i.replace('RES>', '\ud7fc', 1)

          if 'RED>' in i:
              i = i.replace('RED>', '\ud7fd', 1)

          if 'BLU>' in i:
              i = i.replace('BLU>', '\ud7fe', 1)

          if 'GRN>' in i:
              i = i.replace('GRN>', '\ud7ff', 1)

          if 'YLW>' in i:
              i=i.replace('YLW>', '\ud800', 1)

          if 'PNK>' in i:
              i = i.replace('PNK>', '\ud801', 1)

          if 'CYN>' in i:
              i = i.replace('CYN>', '\ud802', 1)

          if 'PUR>' in i:
              i = i.replace('PUR>', '\ud803', 1)

          if 'WHI>' in i:
              i = i.replace('WHI>', '\ud804', 1)

          if 'LME>' in i:
              i = i.replace('LME>', '\ud805', 1)

          if 'GRY>' in i:
              i =i.replace('GRY>', '\ud806', 1)

          # other text formatting
          if 'BLD>' in i:
            i = i.replace('BLD>', '', 1)
            print('\033[1m', end='')

          if 'ITAL<' in i:
              italics = i[i.find('ITAL<') + 5 : i.find('>')]
              i = i.replace(f'ITAL<{italics}>', f'\udff0{italics}\udff1')

          if 'PORT<' in i:
            portrait = i[i.find('PORT<') + 5 : i.find('>')]
            i = i.replace(f'PORT<{portrait}>', '', 1)
            print(f'({portrait}) ', end='')

        i = i.replace('ESC>', '', 1)
        text.text(i, textSpeed, cont, clear)
        if nobr and textSpeed > 0:
          print('\033[0;0;0m', end='')
        else:
          print('\033[0;0;0m')
      # print()
    input('Return > ')
    extra.clear()
  except KeyboardInterrupt: pass