import sys, time
from os import environ

import httpx
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

runner = ""


def isLocal():
    global runner
    return runner == "Local"


def getRunner():
    global runner
    try:
        runner = str(environ['DAKA_RUNNER'])
        if runner != "GitHub" and runner != "Gitee":
            runner = "Local"
    except KeyError:
        runner = "Local"


def check(sessionid: str):
    headers = {
        'Content-Type':
        'application/json',
        'X-Auth-Token':
        sessionid,
        'User-Agent':
        'Mozilla/5.0 (Linux; Android 11; Pixel 4 XL Build/RQ3A.210705.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 Al'
        + 'iApp(Din' + 'gTa' + 'lk/6.5.45) com.al' + 'iba' + 'ba.android.rim' +
        'et/26284409 Channel/700159 language/zh-CN UT4' +
        'Aplus/0.2.25 colorScheme/light'
    }
    url = "https://sk" + "l.h" + "du.edu.cn/api/pun" + "ch"
    data = {
        "currentLocation": "浙江省杭州市钱塘区",
        "city": "杭州市",
        "districtAdcode": "330114",
        "province": "浙江省",
        "district": "钱塘区",
        "health" + "Code": 0,
        "health" + "Report": 0,
        "current" + "Living": 0,
        "last1" + "4days": 0
    }

    for i in range(3):
        try:
            res = httpx.post(url, json=data, headers=headers, timeout=30)
            if isLocal():
                print(res.status_code, res.text)
            if res.status_code == 200:
                return True
            elif res.status_code == 400 and "已经打卡" in res.text:
                print("Already checked in")
                return True
            else:
                print(f"#{i + 1} Failed")
        except Exception as e:
            print(f"#{i + 1} Failed")
            if isLocal():
                print(repr(e))
    return False


def getSessionId(username: str, password: str):
    print("Getting session ID")
    options = Options()
    options.headless = not isLocal()
    if runner == "GitHub":
        options.set_preference('network.trr.mode', 2)
        options.set_preference('network.trr.uri',
                               'https://dns.google/dns-query')
    driver = webdriver.Firefox(options=options)
    wait = WebDriverWait(driver, 10, 0.5)
    try:
        driver.get("https://ca" + "s.hd" + "u.edu.cn/c" + "as/login")
        wait.until(EC.presence_of_element_located((By.ID, "un")))
        wait.until(EC.presence_of_element_located((By.ID, "pd")))
        wait.until(
            EC.presence_of_element_located((By.ID, "index_log" + "in_btn")))
        print("Login page loaded")
        driver.find_element(By.ID, "un").clear()
        driver.find_element(By.ID, "un").send_keys(username)
        driver.find_element(By.ID, "pd").clear()
        driver.find_element(By.ID, "pd").send_keys(password)
        driver.find_element(By.ID, "index_log" + "in_btn").click()
    except Exception as e:
        print("Cannot access ca" + "s.hdu.edu.cn")
        if isLocal():
            print(repr(e))
        return ""

    loginFailed = False
    time.sleep(2)
    try:
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@id='total_num' or @id='errormsg']")))
        if len(driver.find_elements(By.ID, "errormsg")) > 0:
            loginFailed = True
        else:
            loginFailed = False
    except Exception as e: # timeout
        print("Warning: Cannot detect login state by element")
        if isLocal():
            print(repr(e), driver.current_url)
        # Try to get the session id anyway
        loginFailed = False

    if loginFailed:
        driver.quit()
        print("Failed to log in")
        return ""
    else:
        sessionId = readSessionId(driver, wait)
        if sessionId is not None and sessionId != "":
            result = sessionId
        else:
            print("Cannot get SessionId")
            result = ""
        driver.quit()
        return result


def readSessionId(driver, wait):
    driver.get("https://sk" + "l.h" + "duhe" + "lp.com/pas" +
               "scard.html#/pas" + "scard")
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "nucleic-acid")))
    print("Passcard page loaded")

    for retryCnt in range(10):
        time.sleep(1)
        sessionId = driver.execute_script(
            "return window.localStorage.getItem('sessionId')")
        if sessionId is not None and sessionId != "":
            return sessionId
    return ""


if __name__ == "__main__":

    getRunner()
    print("Runner:", runner)

    if isLocal():
        from secret import *

    sessionId = getSessionId(environ['MY_SECRET_USERNAME'],
                             environ['MY_SECRET_PASSWORD'])
    if sessionId == "":
        sys.exit(1)
    if isLocal():
        print("Session Id:", sessionId)

    if not check(sessionId):
        sys.exit(1)
    else:
        print("OK")
        sys.exit(0)
