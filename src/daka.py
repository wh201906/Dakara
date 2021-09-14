from util import *
from os import environ
from login import login

urlcore = 'heal' + 'thch' + 'ecki' + 'n'
url = 'https' + '://' + urlcore + '.hd' + 'u' + 'he' + 'lp.com'


def checkState():
    return ('今日已打卡' in driver.page_source)


driver.get(url)
login()

sleep(sleepTime)
driver.implicitly_wait(implicitWaitTime)
if urlcore not in driver.current_url:
    printTime()
    print("Error: Failed to login")
    exit(1)
else:
    printTime()
    print("Info: Login successed!")

if checkState():
    printTime()
    print("Error: Already check in")
    exit(1)
else:
    printTime()
    print("Info: Start")

printTime()
print("Info: Manual location")
manualXpath = '/html/body/div[1]/div[2]/div[3]/div[1]/div/div[1]/span[2]'
tryClickByXPath(manualXpath)
locationXpath = '/html/body/div[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div/input'
tryClickByXPath(locationXpath)

printTime()
print("Info: Selecting location")
for i in range(1, int(environ['MY_SECRET_PROVINCE']) + 1):
    XPath = '/html/body/div[1]/div[2]/div[3]/div[1]/div[3]/div/div[2]/div[1]/ul/li['
    XPath += str(i) + ']'
    tryClickByXPath(XPath)
for i in range(1, int(environ['MY_SECRET_CITY']) + 1):
    XPath = '/html/body/div[1]/div[2]/div[3]/div[1]/div[3]/div/div[2]/div[2]/ul/li['
    XPath += str(i) + ']'
    tryClickByXPath(XPath)
for i in range(1, int(environ['MY_SECRET_DISTRICT']) + 1):
    XPath = '/html/body/div[1]/div[2]/div[3]/div[1]/div[3]/div/div[2]/div[3]/ul/li['
    XPath += str(i) + ']'
    tryClickByXPath(XPath)

confirmXPath = '/html/body/div[1]/div[2]/div[3]/div[1]/div[3]/div/div[1]/button[2]'
tryClickByXPath(confirmXPath)

vaccineXPath = '/html/body/div[1]/div[2]/div[3]/div[2]/div[8]/div[2]/div/div[4]/div[2]'
tryClickByXPath(vaccineXPath)
dakaXPath = '/html/body/div[1]/div[2]/div[3]/p/button'
tryClickByXPath(dakaXPath)
sleep(sleepTime)
finalXPath = '/html/body/div[4]/div[3]/button[2]'
tryClickByXPath(finalXPath)

sleep(sleepTime)
driver.refresh()
sleep(sleepTime)
driver.implicitly_wait(implicitWaitTime)
if checkState() == False:
    printTime()
    print("Error: Failed to check in")
    exit(1)
else:
    printTime()
    print("Info: Successed!")