# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import random

from config import *

waitTime = random.randint(0,60)
print('wait: ', waitTime, 'min')
time.sleep(waitTime*60)

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument("--no-sandbox")

chromedriver = r'C:\tools\selenium\chromedriver.exe'
# driver = webdriver.Chrome(executable_path=chromedriver)
driver = webdriver.Chrome(executable_path=chromedriver,options=options)


driver.get('https://my.keiba.rakuten.co.jp/')

try:
    # 楽天競馬へログイン
    driver.find_element_by_id('loginInner_u').send_keys(RakutenKeiba_ID)
    driver.find_element_by_id('loginInner_p').send_keys(RakutenKeiba_PW)
    driver.find_element_by_class_name('loginButton').click()
    time.sleep(3)

    # 入金ページに遷移
    driver.get('https://bet.keiba.rakuten.co.jp/bank/deposit/')

    # 100円入金
    driver.find_element_by_id('depositingInputPrice').send_keys(RakutenKeiba_DEP)
    driver.find_element_by_class_name('confirm').click()
    time.sleep(3)

    # 暗証番号入力画面
    driver.find_element_by_class_name('tealeaf_masking').send_keys(RakutenKeiba_PIN)
    driver.find_element_by_class_name('credit').click()
    time.sleep(3)

except:
    print("error")

# 終了
driver.save_screenshot('results.png')
driver.quit()
