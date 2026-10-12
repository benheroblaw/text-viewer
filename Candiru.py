import os, extra, fish

# chapter selector
def Candiru(sel, folder_last, folder, folders_pretty, folder_display, show_tags):
	"""Chapter select"""
	if not sel > folder_last:
		while True:
			chapters_list = os.listdir('./content/' + folder + '')
			chapters = []
			chapter_output = list()

			for x in chapters_list:
				if os.path.isdir(os.path.abspath('./content/' + folder + "/" + x)) and not x.startswith("."):
					chapter_output.append(str(x) + "/")
			chapter_output.sort()
			for i in chapter_output:
				chapters.append(i)
			chapter_output = list()

			for x in chapters_list:
				if x.endswith('.scri'):
					chapter_output.append(str(x))
			chapter_output.sort()
			for i in chapter_output:
				chapters.append(i)

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
				print(str(i+1) + '. ' + "\033[1m" + str(chapters_pretty[i]) + "\033[m") #'Chapter ' + str(i+1) + ': ' +
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
				if os.path.isdir(os.path.abspath('./content/' + folder + "/" + chapters[chap_sel])):
					Candiru(sel, folder_last, folder + "/" + chapters[chap_sel].removesuffix("/"), folders_pretty, folder_display, show_tags)
				else:
					if not chapters[chap_sel].endswith(".scri"):
						chapters[chap_sel] += ".scri"
					chap_story = extra.readfile('./content/' + folder + '/' + chapters[chap_sel]).splitlines()
					fish.Taimen(chap_story)