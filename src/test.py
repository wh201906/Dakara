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
        print_exc(e)
        if i == 4:
            printTime()
            print("Error: Failed to open")
            exit(1)
        else:
            continue

    if login():
        break

sleep(sleepTime)
driver.implicitly_wait(pageWaitTime)
if urlcore not in driver.current_url:
    printTime()
    print("Error: Failed to login")
    exit(1)
else:
    printTime()
    print("Info: Login successed!")

# if checkState():
#     printTime()
#     print("Error: Already check in")
#     exit(1)
# else:
#     printTime()
#     print("Info: Start")

print('************')
print(driver.page_source)