from util import *
from os import environ
from login import login
from localstorage import *
from os import environ

for i in range(3):
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
            driver.quit()
            exit(1)
        else:
            driver.quit()
            driver = loadDriver()
            sleep(7 * 60)
            driver.get('about:blank')
            driver.implicitly_wait(implicitWaitTime)
            continue

    sleep(sleepTime)
    driver.implicitly_wait(pageWaitTime)
    if urlcore not in driver.current_url and login(driver) is False:
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
    print("Error: Already checked in")
    exit(0)
else:
    printTime()
    print("Info: Start")

ls_set(driver, "hd" + "uhe" + "lp_nc" + "ov_da" + "ilysi" + "gn_tok" + "en",
       environ['MY_SECRET_TOKEN'])
driver.get(url)
sleep(sleepTime)
driver.implicitly_wait(pageWaitTime)
sleep(sleepTime)

manualFeature = [(By.CLASS_NAME, 'van-tag--warning'),
                 (By.XPATH, "//*[contains(text(), '定位不准')]")]
locationFeature = [(By.CLASS_NAME, 'van-field__control--right'),
                   (By.XPATH, "//*[contains(@placeholder, '手动选择')]")]
hiddenLocationFeature = [(By.XPATH, "//*[contains(@label, '目前所在地址')]")]
popupFeature = [(By.CLASS_NAME, 'van-button--default')]

sleep(10)
sleep(sleepTime)

vaccineFeature = [(
    By.XPATH,
    "//span[contains(text(), '共二针') and contains(text(), '已完成第二针')]/../../div[contains(@class, 'van-radio')]"
)]
printTime()
print("Info: Selecting vaccine")
tryClick(driver, vaccineFeature)

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
tryClick(driver, dakaFeature)
sleep(sleepTime)
tryClick(driver, finalFeature)
sleep(10)

for i in range(3):
    printTime()
    print("Info: Checking state#" + str(i + 1))
    sleep(sleepTime)
    try:
        driver.refresh()
    except TimeoutException:
        sleep(sleepTime)
        printTime()
        print("Error: Failed to refresh")
        continue
    sleep(sleepTime)
    driver.implicitly_wait(implicitWaitTime)
    sleep(sleepTime)
    if checkState() == False:
        printTime()
        print("Error: Failed to check in")
        continue
    else:
        printTime()
        print("Info: Successed!")
        exit(0)
exit(1)