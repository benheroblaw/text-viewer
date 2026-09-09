import os, genCollections, extra
from Mako import Mako
from Taimen import Taimen

# chapter selector

def Candiru(sel, folder_last, folders, folders_pretty, folder_display):
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
      for i, x in enumerate(chapters_pretty):
        output = x.replace("_", ' ')
        output = output.replace('zzz-', '_')
        output = output.removesuffix('.scri')
        # output = output[0].upper() + output[1:]
        chapters_pretty[i] = output
      chapters = []
      for i, x in enumerate(chapters_list):
        if x.endswith('.scri'):
          chapters.append(str(x))
      chapters.sort()
      chapter_last = len(chapters)

      Mako(folders, sel, folders_pretty, folder_display)

      print('\n0. Back')
      for i, x in enumerate(chapters):
        print(str(i+1) + '. ' + str(chapters_pretty[i])) #'Chapter ' + str(i+1) + ': ' +
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
        Taimen(chap_story)