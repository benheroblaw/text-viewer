import os, textwrap, fish, extra, json, importlib
importlib.reload(fish)

# folder selector

def Barracuda():
	"""Folder display"""
	while True:
		print('\33]0;benheroblaw\'s text viewer :3\a', end='', flush=True)
		folder = os.scandir('./content')
		folders = []
		for entry in folder:
			if entry.is_dir():
				# print(entry)
				folders.append(str(entry.name))
		folders.sort()

		folder_last = len(folders)

		folders_pretty = folders
		for i, x in enumerate(folders_pretty):
			# text.text(i)
			output = x
			output = output.removeprefix('_')
			output = output.replace("_", ' ')
			output = output.replace('zzz-', '_')
			# output = output[0].upper() + output[1:]
			# folders_pretty[i] = x.replace('_', ' ')
			folders_pretty[i] = output
			# print(i)

		folders = os.listdir('./content')
		folders.sort()
		# folders_pretty.sort()

		extra.clear()
		size = os.get_terminal_size()

		# raw
		if extra.readline('options.txt', 2) == '1':
			output = str(folders)
			output = output.removeprefix('[')
			output = output.removesuffix(']')
			files_indent = '  '
			print('Folders in ./content: ')
			print(textwrap.fill(str(output), size.columns, break_on_hyphens=False, subsequent_indent=files_indent, initial_indent=' '))
		# pretty
		elif extra.readline('options.txt', 2) == '0':
			print('./content/...\n\n0. Options')
		# use meta.json titles
		elif extra.readline('options.txt', 2) == '2':
			output = str(folders)
			output = output.removeprefix('[')
			output = output.removesuffix(']')
			files_indent = '  '
			print('Folders in ./content: ')
			print(textwrap.fill(str(output), size.columns, break_on_hyphens=False, subsequent_indent=files_indent, initial_indent=' '))
		# use meta.json titles and folder names
		elif extra.readline('options.txt', 2) == '3':
			output = str(folders)
			output = output.removeprefix('[')
			output = output.removesuffix(']')
			files_indent = '  '
			print('Folders in ./content: ')
			print(textwrap.fill(str(output), size.columns, break_on_hyphens=False, subsequent_indent=files_indent, initial_indent=' '))
		# neither
		else:
			extra.writefile('options.txt', extra.readline('options.txt', 1) + '\n1')
			continue
		print("\n0. Settings")

		# show tags
		if extra.readline('options.txt', 3) == '1':
			# print(textwrap.fill('Folders in ./content: ' + str(folders), size.columns, break_on_hyphens=False) + '\n\n0. Options')
			pass
		# don't show tags
		elif extra.readline('options.txt', 3) == '0':
			# print('./content/...\n\n0. Options')
			pass
		# neither
		else:
			extra.writefile('options.txt', f'{extra.readline('options.txt', 1)}\n{extra.readline('options.txt', 2)}\n0')
			continue

		# sort tags
		if extra.readline('options.txt', 4) == '1':
			# print(textwrap.fill('Folders in ./content: ' + str(folders), size.columns, break_on_hyphens=False) + '\n\n0. Options')
			pass
		# don't sort tags
		elif extra.readline('options.txt', 4) == '0':
			# print('./content/...\n\n0. Options')
			pass
		# neither
		else:
			extra.writefile('options.txt', f'{extra.readline('options.txt', 1)}\n{extra.readline('options.txt', 2)}\n{extra.readline('options.txt', 3)}\n0')
			continue

		folder_display = extra.readline('options.txt', 2)
		# if folder_display == '1': folder_display = True
		show_tags = extra.readline('options.txt', 3)

		# pretty
		if folder_display == '1':
			for i, x in enumerate(folders):
				print(str(i+1) + '. ' + folders_pretty[i])
		# meta.json titles
		elif folder_display == '2':
			folderTitles = []
			for num, name in enumerate(folders):
				if "meta.json" in os.listdir(f"./content/{name}"):
					folderTitle = json.loads(extra.readfile(f'./content/{folders[num]}/meta.json'))["title"]
					if folderTitle.strip() != "":
						folderTitles.append(folderTitle)
					else:
						folderTitles.append(folders_pretty[num])
			for i, x in enumerate(folderTitles):
				print(str(i+1) + '. ' + folderTitles[i])
		# meta.json titles with folder names
		elif folder_display == '3':
			folderTitles = []
			for num, name in enumerate(folders):
				if "meta.json" in os.listdir(f"./content/{name}"):
					folderTitle = json.loads(extra.readfile(f'./content/{folders[num]}/meta.json'))["title"]
					if folderTitle.strip() != "":
						folderTitles.append(folderTitle + f" ({folders[num]})")
					else:
						folderTitles.append(folders_pretty[num] + f" ({folders[num]})")
			for i, x in enumerate(folderTitles):
				print(str(i+1) + '. ' + folderTitles[i])
		# raw
		else:
			for i, x in enumerate(folders):
				print(str(i+1) + '. .../' + folders[i])

		try: selection = input('\n> ')
		except KeyboardInterrupt: break
		try:
			sel = int(selection)-1
			if sel == -1:
				sel = folder_last +1
			selection = int(selection)
			extra.clear()
		except ValueError:
			print("")
			continue

		# settings
		if selection == 0:
			fish.Sixgill()

		# pass it to Candiru
		elif selection <= len(folders):
			fish.Candiru(sel, folder_last, folders, folders_pretty, folder_display)

		else:
			input('wtf')
			pass