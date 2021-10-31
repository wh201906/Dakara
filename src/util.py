from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, WebDriverException, TimeoutException, ElementNotInteractableException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from os import environ
from datetime import datetime, timezone, timedelta
from traceback import print_exc

pageWaitTime = 300
implicitWaitTime = 60
sleepTime = 30

driver = None
options = None

# override the existing driver
def setAgent(agent):
    global driver, options
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.user" + "agent.override", agent)
    profile.set_preference("geo.prompt.testing", True)
    profile.set_preference("geo.prompt.testing.allow", False)

    return webdriver.Firefox(firefox_profile=profile, options=options)

try:
    if bool(environ['CI']) == True:
        print("Env: Github")
        isRemote = True
    else:
        print("Env: Local")
        isRemote = False
except KeyError:
    print("Env: Local")
    isRemote = False

if isRemote == False:
    from secret import *
    pageWaitTime = 30
    implicitWaitTime = 30
    sleepTime = 5

options = Options()
options.headless = isRemote

yi__b_an = 'Mozilla/5.0 yi' + 'b' + 'an_and' + 'roid/5.0.1'
w_echa_t = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 Micro' + 'Mess' + 'enger/6.5.2.501 NetType/WIFI WindowsW' + 'echat Q' + 'BCore/3.43.884.400 QQB' + 'rowser/9.0.2524.400'
urlcore = 'heal' + 'thch' + 'ecki' + 'n'
url = 'https' + '://' + urlcore + '.hd' + 'u' + 'he' + 'lp.com'

driver = setAgent(yi__b_an)


def tryClickFrom(driver, start, lis):
    targetList = []
    element = None
    for by, feature in lis:
        locator = (by, feature)
        print("Current locator:", '(' + by + ', ' + feature + ')', end=', ')
        try:
            sleep(sleepTime)
            WebDriverWait(driver, implicitWaitTime, 0.5).until(
                EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            continue
        targetList = start.find_elements(by, feature)
        break
    print('num:', len(targetList))

    for element in targetList:
        if element.is_displayed() == False:
            continue
        try:
            element.click()
        except ElementClickInterceptedException:
            print("ElementClickInterceptedException")
            driver.execute_script("arguments[0].click();", element)
            return element
        except ElementNotInteractableException:
            print("ElementNotInteractableException")
        else:
            return element


# [(by, feature), (by, feature), ....]
# xpath consisting of absolute nodes is not stable
def tryClick(driver, lis):
    return tryClickFrom(driver, driver, lis)


def printTime():
    print(datetime.now(timezone(
        timedelta(hours=0))).strftime('%Y-%m-%d %H:%M:%S'),
          end=' ')


def my_print_exc(e):
    try:
        print_exc(e)
    except TypeError:
        print(repr(e))


def checkState():
    return ('已打卡' in driver.page_source)

