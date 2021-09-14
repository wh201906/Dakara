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

manualFeature = [
    (By.CLASS_NAME, 'van-tag--warning'),
    (By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[3]/div/div[1]/span[2]'),
    (By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[1]/div/div[1]/span[2]')
]
locationFeature = [
    (By.CLASS_NAME, 'van-field__control--right'),
    (By.XPATH,
     '/html/body/div[1]/div[2]/div[3]/div[3]/div[1]/div[2]/div/input'),
    (By.XPATH,
     '/html/body/div[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div/input')
]
printTime()
print("Info: Manual location")
tryClick(manualFeature)
tryClick(locationFeature)

printTime()
print("Info: Selecting location")
popupFeature = [(By.CLASS_NAME, 'van-popup--bottom')]
popupElement = tryClick(popupFeature)
columnList = popupElement.find_elements(By.CLASS_NAME,
                                        'van-picker-column__wrapper')
print("Column:", len(columnList))
province = columnList[0].find_elements(By.CLASS_NAME,
                                       'van-picker-column__item')
for i in range(int(location['province'])):
    province[i].click()
    print(province[i].text)
city = columnList[1].find_elements(By.CLASS_NAME, 'van-picker-column__item')
for i in range(int(location['city'])):
    city[i].click()
    print(city[i].text)
district = columnList[2].find_elements(By.CLASS_NAME,
                                       'van-picker-column__item')
for i in range(int(location['district'])):
    district[i].click()
    print(district[i].text)

confirmFeature = [(By.CLASS_NAME, 'van-picker__confirm')]
tryClickFrom(popupElement, confirmFeature)
