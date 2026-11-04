import os, textwrap, fish, averylib, json, importlib
importlib.reload(fish)

# folder selector

def Barracuda():
    """Folder display"""
    while True:
        # set the window title
        print('\33]0;benheroblaw\'s text viewer :3\a', end='', flush=True)
        # folder =
        folders = []
        for entry in os.scandir('./content'):
            if entry.is_dir():
                # print(entry)
                folders.append(str(entry.name))
        folders.sort()

        folder_last = len(folders)

        folders_pretty = list(folders)
        for i, x in enumerate(folders_pretty):
            output = x
            if output.startswith("_"):
                output = "." + output[1:]
            output = output.replace("_", ' ')
            output = output.replace('zzz-', '_')
            folders_pretty[i] = output

        folders.sort()

        averylib.clear()
        size = os.get_terminal_size()

        # raw
        if averylib.readline('options.txt', 2) == '1':
            output = str(folders)
            output = output.removeprefix('[')
            output = output.removesuffix(']')
            files_indent = '  '
            print('Folders in ./content: ')
            print(textwrap.fill(str(output), size.columns, break_on_hyphens=False, subsequent_indent=files_indent, initial_indent=' '))
        # pretty
        elif averylib.readline('options.txt', 2) == '0':
            print('./content/...')
        # use meta.json titles
        elif averylib.readline('options.txt', 2) == '2':
            output = str(folders)
            output = output.removeprefix('[')
            output = output.removesuffix(']')
            files_indent = '  '
            print('Folders in ./content: ')
            print(textwrap.fill(str(output), size.columns, break_on_hyphens=False, subsequent_indent=files_indent, initial_indent=' '))
        # use meta.json titles and folder names
        elif averylib.readline('options.txt', 2) == '3':
            output = str(folders)
            output = output.removeprefix('[')
            output = output.removesuffix(']')
            files_indent = '  '
            print('Folders in ./content: ')
            print(textwrap.fill(str(output), size.columns, break_on_hyphens=False, subsequent_indent=files_indent, initial_indent=' '))
        # neither
        else:
            averylib.writefile('options.txt', averylib.readline('options.txt', 1) + '\n1')
            continue
        print(averylib.AnsiCode("0;1") + "\n0. Options" + averylib.AnsiCode("0"))

        # show tags
        if averylib.readline('options.txt', 3) == '1':
            # print(textwrap.fill('Folders in ./content: ' + str(folders), size.columns, break_on_hyphens=False) + '\n\n0. Options')
            pass
        # don't show tags
        elif averylib.readline('options.txt', 3) == '0':
            # print('./content/...\n\n0. Options')
            pass
        # neither
        else:
            averylib.writefile('options.txt', f'{averylib.readline('options.txt', 1)}\n{averylib.readline('options.txt', 2)}\n0')
            continue

        # sort tags
        if averylib.readline('options.txt', 4) == '1':
            pass
        # don't sort tags
        elif averylib.readline('options.txt', 4) == '0':
            pass
        # neither
        else:
            averylib.writefile('options.txt', f'{averylib.readline('options.txt', 1)}\n{averylib.readline('options.txt', 2)}\n{averylib.readline('options.txt', 3)}\n0')
            continue

        if averylib.readline('options.txt', 4) == '1':
            pass
        elif averylib.readline('options.txt', 4) == '0':
            pass
        # neither
        else:
            averylib.writefile('options.txt', f'{averylib.readline('options.txt', 1)}\n{averylib.readline('options.txt', 2)}\n{averylib.readline('options.txt', 3)}\n0')
            continue
        if averylib.readline('options.txt', 4) == '1':
            pass
        elif averylib.readline('options.txt', 4) == '0':
            pass
        # neither
        else:
            averylib.writefile('options.txt', f'{averylib.readline('options.txt', 1)}\n{averylib.readline('options.txt', 2)}\n{averylib.readline('options.txt', 3)}\n0')
            continue

        folder_display = averylib.readline('options.txt', 2)
        show_tags = averylib.readline('options.txt', 3)

        # pretty
        if folder_display == '1':
            for i, x in enumerate(folders):
                print(averylib.AnsiCode("0;1") + str(i+1) + '. ' + averylib.AnsiCode("1") + folders_pretty[i] + averylib.AnsiCode("0"))
        # meta.json titles
        elif folder_display == '2':
            folderTitles = []
            for num, name in enumerate(folders):
                if "meta.json" in os.listdir(f"./content/{name}"):
                    try:
                        metaJson = json.loads(averylib.readfile(f'./content/{folders[num]}/meta.json'))
                        if "title" in metaJson:
                            folderTitle = metaJson["title"]
                            if folderTitle.strip() != "":
                                folderTitles.append(folderTitle + "/")
                            else:
                                folderTitles.append(folders_pretty[num] + "/")
                        else:
                            folderTitles.append(folders_pretty[num] + "/")
                    except json.decoder.JSONDecodeError:
                        folderTitles.append(name + "/" + averylib.AnsiCode("0"))
                else:
                    folderTitles.append(folders_pretty[num] + "/")
            for i, x in enumerate(folderTitles):
                print(averylib.AnsiCode("0;1") + str(i+1) + '. ' + averylib.AnsiCode("0") + folderTitles[i] + averylib.AnsiCode("0"))
        # meta.json titles with folder names
        elif folder_display == '3':
            folderTitles = []
            for num, name in enumerate(folders):
                if "meta.json" in os.listdir(f"./content/{name}"):
                    try:
                        metaJson = json.loads(averylib.readfile(f'./content/{folders[num]}/meta.json'))
                        if "title" in metaJson:
                            folderTitle = metaJson["title"]
                            if folderTitle.strip() != "":
                                folderTitles.append(folderTitle + "/")
                            else:
                                folderTitles.append(folders_pretty[num] + "/")
                        else:
                            folderTitles.append(folders_pretty[num] + "/")
                    except json.decoder.JSONDecodeError:
                        folderTitles.append(name + '/' + averylib.AnsiCode("0"))
                else:
                    folderTitles.append(folders_pretty[num] + "/")
            for i, x in enumerate(folderTitles):
                print(averylib.AnsiCode("0;1") + str(i+1) + '. ' + averylib.AnsiCode("0") + folderTitles[i] + averylib.AnsiCode("0") + f" ({folders[i]})")
        # raw
        else:
            for i, x in enumerate(folders):
                print(averylib.AnsiCode("0;1") + str(i+1) + '.' + averylib.AnsiCode("0") + '.../' + folders[i] + averylib.AnsiCode("0"))

        try: selection = input('\n> ')
        except KeyboardInterrupt: break
        try:
            sel = int(selection)-1
            if sel == -1:
                sel = folder_last +1
            selection = int(selection)
            averylib.clear()
        except ValueError:
            print("Input a number")
            continue

        # settings
        if selection == 0:
            fish.Sixgill()

        # pass it to Candiru
        elif selection <= len(folders):
            fish.Candiru(sel, folder_last, folders[sel], folders_pretty, folder_display, show_tags)

        else:
            input('wtf')