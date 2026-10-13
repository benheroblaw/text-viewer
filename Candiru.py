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

            for name in chapters_list:
                # if folder_display == '1':
                #     pass

                if folder_display == '2':
                    if os.path.isdir(f"./content/{folder}/{name}") and not name.startswith("."):
                        if "meta.json" in os.listdir(f"./content/{folder}/{name}"):
                            folderTitle = json.loads(extra.readfile(f'./content/{folder}/{name}/meta.json'))["title"]
                            if folderTitle.strip() != "":
                                chapter_output.append("\033[1m" + f'{folderTitle}\033[0m/' )
                                chapter_raw_output.append(name)
                            else:
                                chapter_output.append("\033[1m" + f"{name}/")
                                chapter_raw_output.append(name)
                        else:
                            chapter_output.append("\033[1m" + f"{name}/")
                            chapter_raw_output.append(name)

                elif folder_display == '3':
                    if os.path.isdir(f"./content/{folder}/{name}") and not name.startswith("."):
                        if "meta.json" in os.listdir(f"./content/{folder}/{name}"):
                            folderTitle = json.loads(extra.readfile(f'./content/{folder}/{name}/meta.json'))["title"]
                            if folderTitle.strip() != "":
                                chapter_output.append("\033[1m" + f'{folderTitle} \033[0m({name})' + "/")
                                chapter_raw_output.append(name)
                            else:
                                chapter_output.append("\033[1m" + f"{name}/")
                                chapter_raw_output.append(name)
                        else:
                            chapter_output.append("\033[1m" + f"{name}/")
                            chapter_raw_output.append(name)

                else:
                    if os.path.isdir(os.path.abspath('./content/' + folder + "/" + x)) and not x.startswith("."):
                        chapter_output.append(str(x) + "/")

            # chapter_output.sort()
            # chapter_raw_output.sort()

            for i in chapter_output:
                chapters.append(i)
            for num, name in enumerate(chapter_raw_output):
                chapter_list[chapters[num]] = name
            chapters.sort()
            # chapter_list.sort()
            chapter_output = list()

            for x in chapters_list:
                if x.endswith('.scri'):
                    chapter_output.append(str(x))
                    chapter_raw_output.append(str(x))
            chapter_output.sort()
            chapter_raw_output.sort()
            for i in chapter_output:
                chapters.append(i)
            # for num, name in enumerate(chapter_raw_output):
            #     chapter_list[chapters[num]] = name

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
                if os.path.isdir(os.path.abspath('./content/' + folder + "/" + chapter_list[chapters[chap_sel]])):
                    Candiru(sel, folder_last, folder + "/" + chapter_list[chapters[chap_sel]].removesuffix("/"), folders_pretty, folder_display, show_tags)
                else:
                    if not chapters[chap_sel].endswith(".scri"):
                        chapters[chap_sel] += ".scri"
                    # chap_story = extra.readfile().splitlines()
                    fish.Taimen('./content/' + folder + '/' + chapter_list[chapters[chap_sel]], './content/' + folder)