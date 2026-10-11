import os, extra, fish

# chapter selector
def Candiru(sel, folder_last, folders, folders_pretty, folder_display, show_tags):
	"""Chapter select"""
	if not sel > folder_last:
		while True:
			chapters_list = os.listdir('./content/' + folders[sel] + '')
			chapters = []
			for i, x in enumerate(chapters_list):
				if x.endswith('.scri'):
					chapters.append(str(x))
			chapters.sort()
			chapters_pretty = chapters
			for num, name in enumerate(chapters_pretty):
				output = name
				if output.startswith("_"):
					output = output.removeprefix("_")
					output = '.' + output
				output = output.replace("_", ' ')
				output = output.replace('zzz-', '_')
				output = output.removesuffix('.scri')
				# output = output[0].upper() + output[1:]
				chapters_pretty[num] = output
			chapters = []
			for i, x in enumerate(chapters_list):
				if x.endswith('.scri'):
					chapters.append(str(x))
			chapters.sort()
			chapter_last = len(chapters)

			# print all the meta stuff
			fish.Mako(folders, sel, folders_pretty, folder_display, show_tags)

			print('\n0. ' + '\033[1m' + 'Back' + "\033[m")
			for i, x in enumerate(chapters):
				print(str(i+1) + '. ' + "\033[1m" + str(chapters_pretty[i]) + "\033[m") #'Chapter ' + str(i+1) + ': ' +
			try: chap_select = input('\n> ')
			except KeyboardInterrupt: break
			try:
				chap_sel = int(chap_select)-1
				chap_select = int(chap_select)
			except ValueError:
				# print("")
				extra.clear()
				continue
			extra.clear()
			if chap_select == 0:
				break
			if not chap_sel > chapter_last-1:
				chap_story = extra.readfile('./content/' + folders[sel] + '/' + chapters[chap_sel]).splitlines()
				fish.Taimen(chap_story)