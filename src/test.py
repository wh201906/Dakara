from util import *
from login import login

for _ in range(5):
    try:
        driver.get(url)
    except WebDriverException:
        continue

driver.implicitly_wait(200)
print(driver.current_url)
print(driver.page_source)
login()
driver.implicitly_wait(200)
print(driver.current_url)
print(driver.page_source)