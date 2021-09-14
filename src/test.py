from util import *
from login import login

driver.get(url)
driver.implicitly_wait(200)
print(driver.current_url)
print(driver.page_source)
login()
driver.implicitly_wait(200)
print(driver.current_url)
print(driver.page_source)