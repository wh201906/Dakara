from util import *
from login import login

login()

sleep(3)
manualXpath = '/html/body/div[1]/div[2]/div[3]/div[1]/div/div[1]/span[2]'
tryClickByXPath(manualXpath)
locationXpath = '/html/body/div[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div/input'
tryClickByXPath(locationXpath)

province = 7
city = 9
area = 4
for i in range(1, province + 1):
    XPath = '/html/body/div[1]/div[2]/div[3]/div[1]/div[3]/div/div[2]/div[1]/ul/li['
    XPath += str(i) + ']'
    tryClickByXPath(XPath)
for i in range(1, city + 1):
    XPath = '/html/body/div[1]/div[2]/div[3]/div[1]/div[3]/div/div[2]/div[2]/ul/li['
    XPath += str(i) + ']'
    tryClickByXPath(XPath)
for i in range(1, area + 1):
    XPath = '/html/body/div[1]/div[2]/div[3]/div[1]/div[3]/div/div[2]/div[3]/ul/li['
    XPath += str(i) + ']'
    tryClickByXPath(XPath)

confirmXPath = '/html/body/div[1]/div[2]/div[3]/div[1]/div[3]/div/div[1]/button[2]'
tryClickByXPath(confirmXPath)

vaccineXPath = '/html/body/div[1]/div[2]/div[3]/div[2]/div[8]/div[2]/div/div[4]/div[2]'
tryClickByXPath(vaccineXPath)
dakaXPath = '/html/body/div[1]/div[2]/div[3]/p/button'
tryClickByXPath(dakaXPath)
sleep(2)
finalXPath = '/html/body/div[4]/div[3]/button[2]'
tryClickByXPath(finalXPath)