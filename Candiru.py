import os, extra, fish, json

# chapter selector
def Candiru(sel, folder_last, folder, folders_pretty, folder_display, show_tags):
    """Chapter select"""
    if not sel > folder_last:
        while True:
            chapters_list = os.listdir('./content/' + folder + '')
            chapter_list = dict()
            chapters = list()
            chapter_output = list()
            chapter_raw_output = list()
            folders = list()

            for name in chapters_list:
                # if folder_display == '1':
                #     pass

                if folder_display == '2':
                    if os.path.isdir(f"./content/{folder}/{name}") and not name.startswith("."):
                        if "meta.json" in os.listdir(f"./content/{folder}/{name}"):
                            metaJson = json.loads(extra.readfile(f'./content/{folder}/{name}/meta.json'))
                            if "title" in metaJson:
                                folderTitle = json.loads(extra.readfile(f'./content/{folder}/{name}/meta.json'))["title"]
                                if folderTitle.strip() != "":
                                    chapter_output.append("\033[1m" + f'{folderTitle}\033[0m/' )
                                    folders.append(name)
                                else:
                                    chapter_output.append("\033[1m" + f"{name}/")
                                    folders.append(name)
                            else:
                                chapter_output.append("\033[1m" + str(name) + "/" + extra.ansi_code("0"))
                                folders.append(name)
                        else:
                            chapter_output.append("\033[1m" + f"{name}/")
                            folders.append(name)

                elif folder_display == '3':
                    if os.path.isdir(f"./content/{folder}/{name}") and not name.startswith("."):
                        if "meta.json" in os.listdir(f"./content/{folder}/{name}"):
                            metaJson = json.loads(extra.readfile(f'./content/{folder}/{name}/meta.json'))
                            if "title" in metaJson:
                                folderTitle = json.loads(extra.readfile(f'./content/{folder}/{name}/meta.json'))["title"]
                                if folderTitle.strip() != "":
                                    chapter_output.append("\033[1m" + f'{folderTitle} \033[0m({name})' + "/")
                                    folders.append(name)
                                else:
                                    chapter_output.append("\033[1m" + f"{name}/")
                                    folders.append(name)
                            else:
                                chapter_output.append("\033[1m" + str(name) + "/" + extra.ansi_code("0"))
                                folders.append(name)
                        else:
                            chapter_output.append("\033[1m" + f"{name}/")
                            folders.append(name)

                else:
                    if os.path.isdir(os.path.abspath('./content/' + folder + "/" + name)) and not name.startswith("."):
                        chapter_output.append("\033[1m" + str(name) + "/" + extra.ansi_code("0"))
                        folders.append(name)
            chapter_raw_output += folders

            # chapter_output = list(dict(chapter_output))
            # chapter_raw_output = list(dict(chapter_raw_output))
            # chapter_raw_output.sort()

            # for i in chapter_output:
            #     chapters.append(i)
            chapters += chapter_output
            for num, name in enumerate(chapter_raw_output):
                chapter_list[chapters[num]] = name
            chapters.sort()
            # chapter_list.sort()
            chapter_output = list()
            # chapter_raw_output = list()

            script_files = list()
            for i in chapters_list:
                if i.endswith('.scri'):
                    script_files.append(str(i))
            if len(script_files) > 0:
                for num, name in enumerate(script_files):
                    chapter_list[script_files[num]] = name
            chapter_output.sort()
            chapter_raw_output.sort()
            script_files.sort()
            chapter_raw_output += script_files
            chapters += script_files
            # for i in chapter_output:
            #     chapters.append(i)

            chapters_pretty = list()
            for num, name in enumerate(chapters):
                output = name
                if output.startswith("_"):
                    output = output.removeprefix("_")
                    output = '.' + output
                output = output.replace("_", ' ')
                output = output.replace('zzz-', '_')
                output = output.removesuffix('.scri')
                chapters_pretty.append(output)

            chapter_last = len(chapters)

            # print all the meta stuff
            fish.Mako(folder, sel, folders_pretty, folder_display, show_tags)

            print('\n0. ' + '\033[1m' + 'Back' + "\033[m")
            for i, x in enumerate(chapters):
                print(str(i+1) + '. ' + str(chapters_pretty[i]) + "\033[m") #'Chapter ' + str(i+1) + ': ' +
            try: chap_select = input('\n> ')
            except KeyboardInterrupt: break
            try:
                chap_sel = int(chap_select)-1
                chap_select = int(chap_select)
            except ValueError:
                extra.clear()
                continue
            extra.clear()
            if chap_select == 0:
                break
            if not chap_sel > chapter_last-1:
                # try:
                path = os.path.abspath(
                    os.path.join('./content', folder, chapter_list[chapters[chap_sel]])
                    )
                if os.path.isdir( path ):
                    Candiru(sel, folder_last, os.path.join(folder, chapter_list[chapters[chap_sel]]), folders_pretty, folder_display, show_tags)
                # except: print(f"Could not find key...")
                else:
                    if not chapters[chap_sel].endswith(".scri"):
                        chapters[chap_sel] += ".scri"
                    # chap_story = extra.readfile().splitlines()
                    fish.Taimen(os.path.join('./content', folder, chapter_list[chapters[chap_sel]]), './content/' + folder)