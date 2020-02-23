from bs4 import BeautifulSoup#bs4をimport
from selenium import webdriver#seleniumをimport
import os
import pandas as pd#pandasをimport
from datetime import datetime, timedelta
import sched
import time
import re

now = datetime.now()
driver = webdriver.Chrome(executable_path='C:\\Users\ynish\Desktop\gitpractice\chromedriver_win32\chromedriver.exe')
driver.get("https://www.nhk.or.jp/kishou-saigai/city/status/13109001310900/")
html = driver.page_source.encode('utf-8')
soup = BeautifulSoup(html, "html.parser")
p=""
p=soup.select_one("#app > main > div > div.theMain > div > div.theWeatherLv3_container > div > div.weatherLv3Status_info > div > div.weatherLv3Status_info_data > div.weatherLv3Status_info_data_block.temp > span.dataBlock_value")
driver.close()
columns = ["number","tempelture"]
df = pd.DataFrame(columns=columns) # 列名を指定する
##行を増やす
count=1
se = pd.Series([0,p.string], columns) 
df = df.append(se, columns)
while count<3:
    comp = datetime.now()
    diff = comp.minute - now.minute
    if diff>=count*5:
        p=""
        count=count+1
        ####2回目
        driver = webdriver.Chrome(executable_path='C:\\Users\ynish\Desktop\djyagopractice\chromedriver_win32\chromedriver.exe')###chroedriver.exeを入れた場所を指定
        driver.get("https://www.nhk.or.jp/kishou-saigai/city/status/13109001310900/")
        html = driver.page_source.encode('utf-8')
        # BeautifulSoupで扱えるようにパースします
        soup = BeautifulSoup(html, "html.parser")
        # idがheikinの要素を表示
        print(soup.select_one("#app > main > div > div.theMain > div > div.theWeatherLv3_container > div > div.weatherLv3Status_info > div > div.weatherLv3Status_info_data > div.weatherLv3Status_info_data_block.temp > span.dataBlock_value"))
        p=""
        p=soup.select_one("#app > main > div > div.theMain > div > div.theWeatherLv3_container > div > div.weatherLv3Status_info > div > div.weatherLv3Status_info_data > div.weatherLv3Status_info_data_block.temp > span.dataBlock_value")
        driver.close()
        se = pd.Series([diff,p.string], columns) 
        df = df.append(se, columns)
# 行を作成
df.to_csv("df1.csv")
from google.colab import files#google.colabをimport
files.download('df1.csv')