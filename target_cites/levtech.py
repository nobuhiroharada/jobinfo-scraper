# coding:utf-8
import os
import sys
import csv
import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

sys.path.append(str(Path(__file__).parent.parent))

import settings
from functions import Functions

chromedriver = os.getcwd() + '/chromedriver80'
donwload_dir = os.getcwd()+'/download_csv'

functions = Functions()

exec_date = functions.get_exec_date()
search_words = ['php', 'java']
search_results = []

print('start scraping : levtech ' + exec_date)
print('open browser : levtech')

driver = webdriver.Chrome(chromedriver)
driver.get("https://freelance.levtech.jp/project/search/")

time.sleep(1)

# 検索ワード毎の案件数取得
for w in search_words:
    search_input = driver.find_element_by_xpath('//*[@id="activeCount"]/div[1]/div[1]/div/input')
    search_input.clear()
    search_input.send_keys(w)
    search_input.send_keys(Keys.ENTER)
    time.sleep(1)
    search_results.append(driver.find_element_by_xpath('//*[@id="activeCount"]/div[2]/div/p/span').text)

# csvに出力
with open(donwload_dir + '/levtech_' + exec_date + '.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['search_word', 'sum', 'date']) # header
    for i, w in enumerate(search_words):
        writer.writerow([w, search_results[i], exec_date])

print('close browser : levtech')

driver.quit()

print("finish scraping : levtech")