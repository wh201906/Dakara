from util import *
from os import environ
from login import login
from ast import literal_eval


def checkState():
    return ('今日已打卡' in driver.page_source)


for i in range(5):
    printTime()
    print('Info: Open url#' + str(i + 1))
    try:
        driver.get(url)
    except BaseException as e:
        print("Error: Failed to open url#" + str(i + 1))
        my_print_exc(e)
        if i == 4:
            printTime()
            print("Error: Failed to open url")
            exit(1)
        else:
            continue

    sleep(sleepTime)
    driver.implicitly_wait(pageWaitTime)
    if urlcore not in driver.current_url and login() is False:
        printTime()
        print("Info: Unexpected url at " + driver.current_url)
        continue

    sleep(sleepTime)
    driver.implicitly_wait(pageWaitTime)
    sleep(sleepTime)
    printTime()
    print('Now at: ' + driver.current_url)
    if urlcore not in driver.current_url:
        printTime()
        print("Error: Failed to login#" + str(i + 1))
        continue
    else:
        printTime()
        print("Info: Login successed!")
        break

if urlcore not in driver.current_url:
    printTime()
    print("Error: Failed to login")
    exit(1)

if checkState():
    printTime()
    print("Error: Already check in")
    exit(1)
else:
    printTime()
    print("Info: Start")

location = environ['MY_SECRET_LOCATION']
location = literal_eval(location)

printTime()
print("Info: Manual location")
manualXpath = '/html/body/div[1]/div[2]/div[3]/div[1]/div/div[1]/span[2]'
tryClick(By.XPATH, manualXpath)
locationXpath = '/html/body/div[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div/input'
tryClick(By.XPATH, locationXpath)

printTime()
print("Info: Selecting location")
for i in range(1, int(location['province']) + 1):
    XPath = '/html/body/div[1]/div[2]/div[3]/div[1]/div[3]/div/div[2]/div[1]/ul/li['
    XPath += str(i) + ']'
    tryClick(By.XPATH, XPath)
for i in range(1, int(location['city']) + 1):
    XPath = '/html/body/div[1]/div[2]/div[3]/div[1]/div[3]/div/div[2]/div[2]/ul/li['
    XPath += str(i) + ']'
    tryClick(By.XPATH, XPath)
for i in range(1, int(location['district']) + 1):
    XPath = '/html/body/div[1]/div[2]/div[3]/div[1]/div[3]/div/div[2]/div[3]/ul/li['
    XPath += str(i) + ']'
    tryClick(By.XPATH, XPath)

confirmXPath = '/html/body/div[1]/div[2]/div[3]/div[1]/div[3]/div/div[1]/button[2]'
tryClick(By.XPATH, confirmXPath)

printTime()
print("Info: Selecting vaccine")
vaccineXPath = '/html/body/div[1]/div[2]/div[3]/div[2]/div[8]/div[2]/div/div[4]/div[2]'
tryClick(By.XPATH, vaccineXPath)

printTime()
print("Info: Confirming")
dakaXPath = '/html/body/div[1]/div[2]/div[3]/p/button'
tryClick(By.XPATH, dakaXPath)
sleep(sleepTime)
finalXPath = '/html/body/div[4]/div[3]/button[2]'
tryClick(By.XPATH, finalXPath)

printTime()
print("Info: Checking state")
sleep(sleepTime)
driver.refresh()
sleep(sleepTime)
driver.implicitly_wait(implicitWaitTime)
sleep(sleepTime)
if checkState() == False:
    printTime()
    print("Error: Failed to check in")
    exit(1)
else:
    printTime()
    print("Info: Successed!")