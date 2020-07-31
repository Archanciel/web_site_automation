import mechanize, pickle

FILE_PATH='C:\\temp\\plusconscient.bin'

with open(FILE_PATH, 'rb') as handle:
    cred = pickle.loads(handle.read())

USERNAME = cred['usr']
PASSWORD = cred['pw']

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
br.open('http://plusconscient.net/administrator')
br.select_form(nr = 0)
br.form['username'] = USERNAME
br.form['passwd'] = PASSWORD
br.submit()
br.open('http://plusconscient.net/administrator/index.php?option=com_cache')
print(br.response().read())

selectAllChkboxId = "cb1"
deleteBtnId = "toolbar-delete"
# for form in br.forms():
#      print("Form name:", form.name)
#      print(form)
br.select_form("adminForm")
# for control in br.form.controls:
#     print(control)
#     print("type=%s, name=%s value=%s" % (control.type, control.name, br[control.name]))
#print(br.find_control("cid[]").items[0].selected)
for chkbox in br.find_control("cid[]").items:
	print(chkbox)
	chkbox.selected=True
#print(br.find_control("cid[]").items[0].selected)
#br.submit(id='toolbar-delete')
br.form.action="submitbutton(\'delete\')"