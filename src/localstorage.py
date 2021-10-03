from util import *


def ls_dump(driver):
    return driver.execute_script("var ls = window.localStorage, items = {}; " +
                                 "for (var i = 0, k; i < ls.length; ++i) " +
                                 "  items[k = ls.key(i)] = ls.getItem(k); " +
                                 "return items; ")

def ls_set(driver, key, value):
    driver.execute_script("window.localStorage.setItem(arguments[0], arguments[1]);", key, value)

def ls_load(driver, storageDict):
    for k, v in storageDict.items():
        ls_set(driver, k, v)