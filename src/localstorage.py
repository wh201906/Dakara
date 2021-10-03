from util import *


def ls_dump():
    global driver
    return driver.execute_script("var ls = window.localStorage, items = {}; " +
                                 "for (var i = 0, k; i < ls.length; ++i) " +
                                 "  items[k = ls.key(i)] = ls.getItem(k); " +
                                 "return items; ")

def ls_load(driver, storageDict):
    for k, v in storageDict.items():
        driver.execute_script("window.localStorage.setItem(arguments[0], arguments[1]);", k, v)