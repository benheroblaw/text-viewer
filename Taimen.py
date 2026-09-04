import text, extra

def Taimen(file=''):
  """Text display"""
  try:
    for i in file:
      # i = i.strip()
      italic_temp = ''
      i = i.replace('/i*', '\e[3m')
      i = i.replace('*i/', '\e[23m')
      if i != '':
        nobr = False
        cont = False
        clear = 'none'
        textSpeed = float(extra.readline("options.txt", 1).replace("text-speed = ", ""))

        if "CONT>" in i:
          i = i.replace('CONT>', '', 1)
          cont = True

        if '/NOBR' in i or 'NOBR>' in i:
          i = i.replace('/NOBR', '', 1)
          i = i.replace('NOBR>', '', 1)
          nobr = True

        if 'CLRA>' in i:
          i = i.replace('CLRA>', '', 1)
          clear = 'after'

        if 'CLRB>' in i:
          i = i.replace('CLRB>', '', 1)
          clear = 'before'

        if 'SPD<' in i:
          textSpeed = float(i[i.find('SPD<') + 4 : i.find('>')])
          i = i.replace(f'SPD<{textSpeed}>', '', 1)

        if '#' in i or '/*' in i and 'ESC>' not in i:
          continue

        else:
          if 'ESC>' not in i:
            # light colors
            if 'LGRN>' in i:
              i = i.replace('LGRN>', '', 1)
              print('\033[38;5;46m', end="")

            if 'LBLU>' in i:
              i = i.replace('LBLU>', '', 1)
              print('\033[38;5;45m', end="")

            # colors
            if 'RED>' in i:
              i = i.replace('RED>', '', 1)
              print('\033[38;5;196m', end='')

            if 'GRN>' in i:
              i = i.replace('GRN>', '', 1)
              print('\033[38;5;34m', end="")

            if 'YLW>' in i:
              i=i.replace('YLW>', '', 1)
              print('\033[38;5;220m', end='')

            if 'BLU>' in i:
              i = i.replace('BLU>', '', 1)
              print('\033[38;5;21m', end='')

            if 'PNK>' in i:
              i = i.replace('PNK>', '', 1)
              print('\033[38;5;206m', end='')

            if 'CYN>' in i:
              i = i.replace('CYN>', '', 1)
              print('\033[38;5;m51', end='')

            if 'PUR>' in i:
              i = i.replace('PUR>', '', 1)
              print('\033[38;5;57m', end='')

            if '/WHI' in i or 'WHI>' in i:
              i = i.replace('/WHI', '', 1)
              i = i.replace('WHI>', '', 1)
              print('\033[38;5;255m', end='')
            if 'LME>' in i:
              i = i.replace('LME>', '', 1)
              print('\033[38;5;40m', end='')

            # other text formatting
            if '/BLD' in i or 'BLD>' in i:
              i = i.replace('/BLD', '', 1)
              i = i.replace('BLD>', '', 1)
              print('\033[1m', end='')

            i = i.replace('ESC>', '', 1)
            if 'PORT<' in i:
              portrait = i[i.find('PORT<') + 5 : i.find('>')]
              msg = i.replace(f'PORT<{portrait}>', '', 1)
              if 'CLRA>' in msg:
                msg = msg.replace('CLRA>', '', 1)
                text.face(portrait, msg)
                if nobr:
                  print('\033[0;0;0m', end='')
                else:
                  print('\033[0;0;0m')
                extra.clear()
                continue
              elif 'CLRB>' in msg:
                msg = msg.replace('CLRB>', '', 1)
                extra.clear()
                # text.faceCont(portrait)
              text.face(portrait, msg)
            else:
              text.text(i, textSpeed, cont, clear)
            if nobr and textSpeed > 0:
              print('\033[0;0;0m', end='')
            else:
              print('\033[0;0;0m')
      # print()
    input('Return > ')
    extra.clear()
  except KeyboardInterrupt: pass