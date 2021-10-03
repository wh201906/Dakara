from util import *
from os import environ
from login import login
from ast import literal_eval
from localstorage import *

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
            driver.get('about:blank')
            driver.implicitly_wait(implicitWaitTime)
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
        for j in range(5):
            if 'auth' in driver.current_url:
                print('Waiting login....')
                driver.implicitly_wait(pageWaitTime)
            else:
                break
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

manualFeature = [(By.CLASS_NAME, 'van-tag--warning'),
                 (By.XPATH, "//*[contains(text(), '定位不准')]")]
locationFeature = [(By.CLASS_NAME, 'van-field__control--right'),
                   (By.XPATH, "//*[contains(@placeholder, '手动选择')]")]

print(ls_getKeys())

sleep(10)
printTime()
print("Info: Manual location")
tryClick(manualFeature)
tryClick(locationFeature)

popupFeature = [(By.CLASS_NAME, 'van-popup--bottom')]
printTime()
print("Info: Selecting location")
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

confirmFeature = [(By.CLASS_NAME, 'van-picker__confirm'),
                  (By.XPATH, ".//button[contains(text(), '确认')]")]
tryClickFrom(popupElement, confirmFeature)

vaccineFeature = [(
    By.XPATH,
    "//span[contains(text(), '共二针') and contains(text(), '已完成第二针')]/../../div[contains(@class, 'van-radio')]"
)]
printTime()
print("Info: Selecting vaccine")
tryClick(vaccineFeature)

dakaFeature = [
    (By.CLASS_NAME, 'van-button--info'),
    (By.XPATH,
     "//span[contains(text(), '立即打卡') and contains(@class, 'van-button__text')]/../.."
     )
]
finalFeature = [
    (By.CLASS_NAME, 'van-dialog__confirm'),
    (By.XPATH,
     "//span[contains(text(), '确认') and contains(@class, 'van-button__text')]/../.."
     )
]
printTime()
print("Info: Confirming")
tryClick(dakaFeature)
sleep(sleepTime)
# tryClick(finalFeature)

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