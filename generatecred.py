import os.path
import pickle 

if os.name == 'posix':
	FILE_PATH='/sdcard/plusconscient.bin'
else:
	# Windows
	FILE_PATH='C:\\temp\\plusconscient.bin'

DIC = {'usr': '',
       'pw': '' }

def storeDicInBinFile():
	if os.path.exists(FILE_PATH):
		print(FILE_PATH + ' already exists. To avoid overwriting it by error, delete it manually first !')
		return
	
	with open(FILE_PATH, 'wb') as handle:
		pickle.dump(DIC, handle)
    
	with open(FILE_PATH, 'rb') as handle:
		b = pickle.loads(handle.read())
    
	print(b)
	
if __name__ == '__main__':
	storeDicInBinFile() 
