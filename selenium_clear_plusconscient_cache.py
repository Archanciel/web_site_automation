import pickle
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

FILE_PATH='C:\\temp\\plusconscient.bin'

with open(FILE_PATH, 'rb') as handle:
    cred = pickle.loads(handle.read())

USERNAME = cred['usr']
PASSWORD = cred['pw']

driver = webdriver.Chrome(ChromeDriverManager().install())
#driver.minimize_window()

# Open the website
driver.get('http://plusconscient.net/administrator')

userNameField = driver.find_element_by_name('username')
userNameField.send_keys(USERNAME)

passwordField = driver.find_element_by_name('passwd')
passwordField.send_keys(PASSWORD)

loginButton = driver.find_element_by_class_name('button1')
loginButton.click()

driver.get('http://plusconscient.net/administrator/index.php?option=com_cache')

toggleAllCheckbox = driver.find_element_by_name('toggle')
toggleAllCheckbox.click()
deleteCacheButton = driver.find_element_by_class_name('icon-32-delete')
deleteCacheButton.click()

driver.get('http://plusconscient.net/administrator/index.php?option=com_cache&task=purgeadmin')
purgeExpCacheButton = driver.find_element_by_class_name('icon-32-delete')
purgeExpCacheButton.click()

logoutButton = driver.find_element_by_class_name('logout')
logoutButton.click()

driver.close()
