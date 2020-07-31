# NOT WORKING: TU OUBLIE CE MAUDIT MECHANIZE !!B
import mechanize, pickle, sys, os
from io import StringIO

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
br.open('https://www.flvto.biz/fr74/download/LxsqR9UasLQEcPzO/1/nII-KRCER4E/')
print(br.response().read())

'''
stdin = sys.stdin
sys.stdin = StringIO('btc usd 23/9/2017 2:56 bittrex\nq\ny')

if os.name == 'posix':
	FILE_PATH = '/sdcard/webout.txt'
else:
	FILE_PATH = 'c:\\temp\\webout.txt'

stdout = sys.stdout

# using a try/catch here prevent the test from failing  due to the run of CommandQuit !

try:
	with open(FILE_PATH, 'w') as outFile:
		sys.stdout = outFile
		print(br.response().read())
except:
	pass

outFile.close()
sys.stdin = stdin
sys.stdout = stdout
'''

br.select_form(nr=0)
br.form['search_txt'] = 'https://youtu.be/nII-KRCER4E'
br.submit()
