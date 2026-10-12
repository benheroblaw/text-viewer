import os, extra

# settings

def Sixgill():
  """Settings"""
  while True:
    extra.clear()
    size = os.get_terminal_size()
    print("Settings")
    print("\ndist: ", end="")
    if "portable" in os.listdir("extra/"): print("portable")
    else: print("base")
    print("\n0. Back\n1. Update\n2. Default Text Speed\n3. Folder Display\n4. Default Indent\n5. Show Tags (experimental)\n6. Show nameplates")
    if extra.readline("options.txt", 3) != "0":
      print("7. Sort Tags (experimental)")
    try: opt_sel = input("\n> ")
    except KeyboardInterrupt: break
    try:
      opt_sel = int(opt_sel)
      # selection = int(selection)
      extra.clear()
    except ValueError:
      input("Input a number\n> ")
      extra.clear()
      continue

    # cancel
    if opt_sel == 0:
      break

    # update
    elif opt_sel == 1:
      os.system("printf '%b' 'updating... '; git pull origin release")
      input("Restart to finish updating\n> ")

    # text speed
    elif opt_sel == 2:
      print("Settings\n\nCurrent speed: " + extra.readline("options.txt", 1))
      print("New speed (in seconds):")
      try: speed = input("\n> ")
      except KeyboardInterrupt: continue
      try:
        speed = float(speed)
        # selection = int(selection)
      except ValueError:
        input("Input a number\n> ")
        continue
      extra.writeline("options.txt", 1, speed)
      # text.speed = float(speed)
      input("succeeded! > ")

    # set folder display
    elif opt_sel == 3:
      while True:
        extra.clear()
        print("Settings\n\nDisplaying: ", end="")
        if extra.readline("options.txt", 2) == "0":
          print("raw")
        elif extra.readline("options.txt", 2) == "1":
          print("formatted folder names")
        elif extra.readline("options.txt", 2) == "2":
          print("defined titles")
        elif extra.readline("options.txt", 2) == "3":
          print("defined titles with folder names")
        print("Display as:\n\n1. Defined Titles\n2. Defined Titles with Folder Names\n3. Formatted\n4. Raw\n")
        try: file_display = input("> ")
        except KeyboardInterrupt: break
        try:
          file_display = int(file_display)
          # selection = int(selection)
        except ValueError:
          input("Input a number\n> ")
          continue

        # defined titles
        if file_display == 1:
          extra.writeline("options.txt", 2, "2")
          input("succeeded! > ")
          break
        # defined titles with folder names
        elif file_display == 2:
          extra.writeline("options.txt", 2, "3")
          input("succeeded! > ")
          break
        # formatted
        elif file_display == 3:
          extra.writeline("options.txt", 2, "1")
          input("succeeded! > ")
          break
        # raw
        elif file_display == 4:
          extra.writeline("options.txt", 2, "0")
          input("succeeded! > ")
          break
        else: continue

    # set indent
    elif opt_sel == 4:
      while True:
        extra.clear()
        print(f"Settings\n\nIndent before text: {extra.readline("options.txt", 5)}")
        print("New indent:\n")
        try: new_indent = input("> ")
        except KeyboardInterrupt: break
        try:
          new_indent = int(new_indent)
          # selection = int(selection)
        except ValueError:
          input("Input a number\n> ")
          continue
        extra.writeline("options.txt", 5, new_indent)
        input("succeeded! > ")
        break

    # show tags
    elif opt_sel == 5:
      while True:
        extra.clear()
        print("Settings\n\nShowing tags: ", end="")
        if extra.readline("options.txt", 3) == "0":
          print("false")
        else:
          print("true")

        print("Display as:\n\n1. Hidden\n2. Shown")
        try: tags_shown = input("> ")
        except KeyboardInterrupt: break

        try:
          tags_shown = int(tags_shown)
        except ValueError: continue

        if tags_shown == 1:
          extra.writeline("options.txt", 3, 0)
          input("succeeded! > ")
          break
        elif tags_shown == 2:
          extra.writeline("options.txt", 3, 1)
          input("succeeded! > ")
          break
        else:
          continue

    # show nameplates
    elif opt_sel == 6:
      while True:
        extra.clear()
        print("Settings\n\nWARNING: Writers may not have characters introduce themselves.\n\nShowing nameplates: ".strip(), end="")
        if extra.readline("options.txt", 6) == "0":
          print("false")
        else:
          print("true")

        print("\nDisplay as:\n\n1. Shown\n2. Hidden")
        try: nameplates = input("> ")
        except KeyboardInterrupt: break

        try:
          nameplates = int(nameplates)
        except ValueError: continue

        if nameplates == 1:
          extra.writeline("options.txt", 6, "1")
          input("succeeded! > ")
          break
        elif nameplates == 2:
          extra.writeline("options.txt", 6, "0")
          input("succeeded! > ")
          break
        else:
          continue

    # sort tags
    elif opt_sel == 7:
      while True:
        extra.clear()
        print("Settings\n\nSorting tags: ", end="")
        if extra.readline("options.txt", 4) == "0":
          print("false")
        else:
          print("true")

        print("Display as:\n\n1. Not sorted\n2. Sorted")
        try: tags_shown = input("> ")
        except KeyboardInterrupt: break

        try:
          tags_shown = int(tags_shown)
        except ValueError: continue

        if tags_shown == 1:
          extra.writeline("options.txt", 4, "0")
          input("succeeded! > ")
          break
        elif tags_shown == 2:
          extra.writeline("options.txt", 4, "1")
          input("succeeded! > ")
          break
        else:
          continue

    continue