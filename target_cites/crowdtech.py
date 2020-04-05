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

target_name = 'crowdtech'

total_projects = settings.total_projects
total_projects_results = []
search_words = settings.target_programs_frameworks
search_results = []

print('start scraping : ' + target_name + ' ' + exec_date)
print('open browser : ' + target_name)

driver = webdriver.Chrome(chromedriver)
driver.get(settings.url_crowdtech)

time.sleep(1)

# 総案件数
total_projects_results.append(driver.find_element_by_xpath('/html/body/main/div[5]/div/div[1]/div[1]/span[2]').text)

# 総案件数 CSVに出力
with open(donwload_dir + '/' + target_name + '_total_projects_' + exec_date + '.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['sum', 'date']) # header
    for i, w in enumerate(total_projects):
        writer.writerow([total_projects_results[i], exec_date])

# 検索ワード毎の案件数取得
for w in search_words:
    search_input = driver.find_element_by_xpath('/html/body/main/div[4]/form/div[1]/div[4]/div[1]/div[6]/div/input')
    search_input.clear()
    search_input.send_keys(w)
    search_input.send_keys(Keys.ENTER)
    time.sleep(3)
    search_results.append(driver.find_element_by_xpath('/html/body/main/div[5]/div/div[1]/div[1]/span[2]').text)

# 検索ワード毎の案件数取得 CSVに出力
with open(donwload_dir + '/' + target_name + '_search_words_' + exec_date + '.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['search_word', 'sum', 'date']) # header
    for i, w in enumerate(search_words):
        writer.writerow([w, search_results[i], exec_date])

print('close browser : ' + target_name)

driver.quit()

print('finish scraping : ' + target_name)