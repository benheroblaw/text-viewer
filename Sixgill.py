import os, extra

# settings

def Sixgill():
  """Settings"""
  while True:
    extra.clear()
    size = os.get_terminal_size()
    print('Options\n\n0. Back\n1. Update\n2. Text Speed\n3. Folder Display\n4. Show Tags (experimental)')
    if extra.readline('options.txt', 3) != '0':
      print('5. Sort Tags (experimental)')
    try: opt_sel = input('\n> ')
    except KeyboardInterrupt: break
    try:
      opt_sel = int(opt_sel)
      # selection = int(selection)
      extra.clear()
    except ValueError:
      # print("Input a number")
      extra.clear()
      continue

    if opt_sel == 0:
      break

    elif opt_sel == 1:
      os.system("printf '%b' 'updating... '; git pull origin release")
      input('> Restart to finish updating')

    elif opt_sel == 2:
      print('Options\n\nCurrent speed: ' + extra.readline('options.txt', 1))
      print('New speed (in seconds):')
      try: speed = input('\n> ')
      except KeyboardInterrupt: continue
      try:
        speed = float(speed)
        # selection = int(selection)
      except ValueError:
        print("Input a number")
        continue
      extra.writeline('options.txt', 1, speed)
      # text.speed = float(speed)
      input('succeeded! > ')

    elif opt_sel == 3:
      while True:
        extra.clear()
        print('Options\n\nDisplaying file names: ', end='')
        if extra.readline('options.txt', 2) == '0':
          print('raw')
        else:
          print('formatted')
        print('Display as:\n\n1. Formatted\n2. Raw\n')
        try: file_display = input('> ')
        except KeyboardInterrupt: break
        try:
          file_display = int(file_display)
          # selection = int(selection)
        except ValueError:
          print("Input a number")
          continue

        if file_display == 1:
          extra.writeline('options.txt', 2, '1')
          input('succeeded! > ')
          break
        elif file_display == 2:
          extra.writeline('options.txt', 2, '0')
          input('succeeded! > ')
          break
        else: continue

    elif opt_sel == 4:
      while True:
        extra.clear()
        print('Options\n\nShowing tags: ', end='')
        if extra.readline('options.txt', 3) == '0':
          print('false')
        else:
          print('true')

        print('Display as:\n\n1. Hidden\n2. Shown')
        try: tags_shown = input('> ')
        except KeyboardInterrupt: break

        try:
          tags_shown = int(tags_shown)
        except ValueError: continue

        if tags_shown == 1:
          extra.writeline('options.txt', 3, 0)
          input('succeeded! > ')
          break
        elif tags_shown == 2:
          extra.writeline('options.txt', 3, 1)
          input('succeeded! > ')
          break
        else:
          continue

    elif opt_sel == 5:
      while True:
        extra.clear()
        print('Options\n\nSorting tags: ', end='')
        if extra.readline('options.txt', 4) == '0':
          print('false')
        else:
          print('true')

        print('Display as:\n\n1. Not sorted\n2. Sorted')
        try: tags_shown = input('> ')
        except KeyboardInterrupt: break

        try:
          tags_shown = int(tags_shown)
        except ValueError: continue

        if tags_shown == 1:
          extra.writeline('options.txt', 4, '0')
          input('succeeded! > ')
          break
        elif tags_shown == 2:
          extra.writeline('options.txt', 4, '1')
          input('succeeded! > ')
          break
        else:
          continue

    continue