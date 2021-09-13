from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

from secret import *

yiban = 'Mozilla/5.0 yiban_android/5.0.1'

profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", yiban)

options = Options()
options.headless = True

driver = webdriver.Firefox(firefox_profile=profile, options=options)
driver.get("https://healthcheckin.hduhelp.com")


def tryClickById(itemId):
    global driver
    locator = (By.ID, itemId)
    WebDriverWait(driver, 5,
                  0.5).until(EC.presence_of_element_located(locator))
    element = driver.find_element_by_id(itemId)
    try:
        element.click()
    except ElementClickInterceptedException:
        driver.execute_script("arguments[0].click();", element)


def tryClickByXPath(itemXPath):
    global driver
    locator = (By.XPATH, itemXPath)
    WebDriverWait(driver, 5,
                  0.5).until(EC.presence_of_element_located(locator))
    element = driver.find_element_by_xpath(itemXPath)
    try:
        element.click()
    except ElementClickInterceptedException:
        driver.execute_script("arguments[0].click();", element)


sleep(3)
usernameId = 'oauth_uname_w'
tryClickById(usernameId)
driver.find_element_by_id(usernameId).send_keys(userName)
passwordId = 'oauth_upwd_w'
tryClickById(passwordId)
driver.find_element_by_id(passwordId).send_keys(password)
authXPath = '/html/body/main/section[1]/div/div[4]/button[1]'
tryClickByXPath(authXPath)

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