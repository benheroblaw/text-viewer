import os, averylib

# Options

def Sixgill():
  """Options"""
  while True:
    averylib.clear()
    size = os.get_terminal_size()
    print("Options")
    print("\ndist: ", end="")
    if "portable" in os.listdir("extra/"): print("portable")
    else: print("base")
    print("\n0. Back\n1. Update\n2. Creation Tools (in progress)\n3. Default Text Speed\n4. Folder Display\n5. Default Indent\n6. Show Tags (experimental)\n7. Show nameplates")
    if averylib.readline("options.txt", 3) != "0":
      print("8. Sort Tags (experimental)")
    try: opt_sel = input("\n> ")
    except KeyboardInterrupt: break
    try:
      opt_sel = int(opt_sel)
      # selection = int(selection)
      averylib.clear()
    except ValueError:
      input("Input a number\n> ")
      averylib.clear()
      continue

    # cancel
    if opt_sel == 0:
      break

    # update
    elif opt_sel == 1:
      os.system("printf '%b' 'updating... '; git pull origin release")
      input("Restart to finish updating\n> ")

    elif opt_sel == 2:
      print("Options")
      print()
      print("Creation Tools")
      print()
      print("1. Create story")
      print("2. meta.json Template")

      try: creation_sel = input("\n> ")
      except KeyboardInterrupt: break

      try:
        creation_sel = int(creation_sel)
        # selection = int(selection)
        averylib.clear()
      except ValueError:
        input("Input a number\n> ")
        averylib.clear()
        continue

      if creation_sel == 2:
        averylib.clear()
        print("Where would you like to create the meta.json?")

        meta_location = input("\n> ")
        
        os.makedirs(os.path.abspath(meta_location))

        try: averylib.createfile(os.path.abspath(meta_location) + "meta.json")
        except FileExistsError: print(f"meta.json exists in {os.path.abspath(meta_location)}!")

    # text speed
    elif opt_sel == 3:
      print("Options\n\nCurrent speed: " + averylib.readline("options.txt", 1))
      print("New speed (in seconds):")
      try: speed = input("\n> ")
      except KeyboardInterrupt: continue
      try:
        speed = float(speed)
        # selection = int(selection)
      except ValueError:
        input("Input a number\n> ")
        continue
      averylib.writeline("options.txt", 1, speed)
      # text.speed = float(speed)
      input("succeeded! > ")

    # set folder display
    elif opt_sel == 4:
      while True:
        averylib.clear()
        print("Options\n\nDisplaying: ", end="")
        if averylib.readline("options.txt", 2) == "0":
          print("raw")
        elif averylib.readline("options.txt", 2) == "1":
          print("formatted folder names")
        elif averylib.readline("options.txt", 2) == "2":
          print("defined titles")
        elif averylib.readline("options.txt", 2) == "3":
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
          averylib.writeline("options.txt", 2, "2")
          input("succeeded! > ")
          break
        # defined titles with folder names
        elif file_display == 2:
          averylib.writeline("options.txt", 2, "3")
          input("succeeded! > ")
          break
        # formatted
        elif file_display == 3:
          averylib.writeline("options.txt", 2, "1")
          input("succeeded! > ")
          break
        # raw
        elif file_display == 4:
          averylib.writeline("options.txt", 2, "0")
          input("succeeded! > ")
          break
        else: continue

    # set indent
    elif opt_sel == 5:
      while True:
        averylib.clear()
        print(f"Options\n\nIndent before text: {averylib.readline("options.txt", 5)}")
        print("New indent:\n")
        try: new_indent = input("> ")
        except KeyboardInterrupt: break
        try:
          new_indent = int(new_indent)
          # selection = int(selection)
        except ValueError:
          input("Input a number\n> ")
          continue
        averylib.writeline("options.txt", 5, new_indent)
        input("succeeded! > ")
        break

    # show tags
    elif opt_sel == 6:
      while True:
        averylib.clear()
        print("Options\n\nShowing tags: ", end="")
        if averylib.readline("options.txt", 3) == "0":
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
          averylib.writeline("options.txt", 3, 0)
          input("succeeded! > ")
          break
        elif tags_shown == 2:
          averylib.writeline("options.txt", 3, 1)
          input("succeeded! > ")
          break
        else:
          continue

    # show nameplates
    elif opt_sel == 7:
      while True:
        averylib.clear()
        print("Options\n\nWARNING: Writers may not have characters introduce themselves.\n\nShowing nameplates: ".strip(), end="")
        if averylib.readline("options.txt", 6) == "0":
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
          averylib.writeline("options.txt", 6, "1")
          input("succeeded! > ")
          break
        elif nameplates == 2:
          averylib.writeline("options.txt", 6, "0")
          input("succeeded! > ")
          break
        else:
          continue

    # sort tags
    elif opt_sel == 8:
      while True:
        averylib.clear()
        print("Options\n\nSorting tags: ", end="")
        if averylib.readline("options.txt", 4) == "0":
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
          averylib.writeline("options.txt", 4, "0")
          input("succeeded! > ")
          break
        elif tags_shown == 2:
          averylib.writeline("options.txt", 4, "1")
          input("succeeded! > ")
          break
        else:
          continue

    continue