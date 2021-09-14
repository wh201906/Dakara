from util import *
from os import environ

usernameFeature = [(By.ID, 'oau' + 'th_una' + 'me_w'), (By.CLASS_NAME, 'user')]
passwordFeature = [(By.ID, 'oau' + 'th_up' + 'wd_w'), (By.CLASS_NAME, 'pwd')]
authFeature = [(By.CLASS_NAME, 'oau' + 'th_ch' + 'eck_log' + 'in'),
               (By.XPATH, '/html/body/main/section[1]/div/div[4]/button[1]')]


def login():
    try:
        printTime()
        print("Info: Start login")
        tryClick(usernameFeature).send_keys(environ['MY_SECRET_USERNAME'])
        tryClick(passwordFeature).send_keys(environ['MY_SECRET_PASSWORD'])
        tryClick(authFeature)
    except BaseException as e:
        my_print_exc(e)
        return False
    return True