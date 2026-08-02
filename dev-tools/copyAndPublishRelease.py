#!/usr/bin/env python3
import os, datetime

import copytorelease

date = datetime.datetime.now()
os.system('cd ' + os.path.expanduser('~/.local/share/prokid/text-viewer') + '; git add -A; git commit -m ' + str(date.strftime('%m')) + '/' + str(date.strftime('%d')) + '-' + str(date.strftime('%H')) + ':' + date.strftime('%M') + '; git push origin release')