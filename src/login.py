from util import *
from os import environ

def login():
    sleep(3)
    usernameId = 'oauth_una' + 'me_w'
    tryClickById(usernameId)
    driver.find_element_by_id(usernameId).send_keys(environ['MY_SECRET_USERNAME'])
    passwordId = 'oauth_up' + 'wd_w'
    tryClickById(passwordId)
    driver.find_element_by_id(passwordId).send_keys(environ['MY_SECRET_PASSWORD'])
    authXPath = '/html/body/main/section[1]/div/div[4]/button[1]'
    tryClickByXPath(authXPath)