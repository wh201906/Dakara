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
        my_print_exc(e)
        if i == 4:
            printTime()
            print("Error: Failed to open")
            exit(1)
        else:
            continue

    sleep(sleepTime)
    driver.implicitly_wait(pageWaitTime)
    if urlcore not in driver.current_url and login() is False:
        continue

    sleep(sleepTime)
    driver.implicitly_wait(pageWaitTime)
    sleep(sleepTime)
    print('Now at: ' + driver.current_url)
    if urlcore not in driver.current_url:
        printTime()
        print("Error: Failed to login")
        continue
    else:
        printTime()
        print("Info: Login successed!")
        break

if urlcore not in driver.current_url:
    exit(1)

# if checkState():
#     printTime()
#     print("Error: Already check in")
#     exit(1)
# else:
#     printTime()
#     print("Info: Start")

print('************')
print(driver.page_source)