from bs4 import BeautifulSoup#bs4をimport
from selenium import webdriver#seleniumをimport
import os
import pandas as pd#pandasをimport
from datetime import datetime, timedelta
import sched
import time
import re
import sqlite3
from contextlib import closing
#sql
dbname = 'sss.db'
with closing(sqlite3.connect(dbname)) as connection:
    cursor = connection.cursor()
    sql = 'create table rea(time REAL,tmp REAL,max REAL,min REAL)'
    cursor.execute(sql)###この分消すか１から作るならデータベースファイルけす
    connection.commit()
    now = datetime.now()
    driver = webdriver.Chrome(executable_path='C:\\Users\ynish\Desktop\gitpractice\chromedriver_win32\chromedriver.exe')
    driver.get("https://www.nhk.or.jp/kishou-saigai/city/status/13109001310900/")
    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, "html.parser")
    p=""
    pmax=""
    pmin=""
    p=soup.select_one("#app > main > div > div.theMain > div > div.theWeatherLv3_container > div > div.weatherLv3Status_info > div > div.weatherLv3Status_info_data > div.weatherLv3Status_info_data_block.temp > span.dataBlock_value")
    pmax=soup.select_one("#app > main > div > div.theMain > div > div.theWeatherLv3_container > div > div.weatherLv3Status_info > div > div.weatherLv3Status_info_data > div.weatherLv3Status_info_data_block.temp > div.dataBlock_subBlock.pastTemp > span.maxTemp > span.dataBlock_value")
    pmin=soup.select_one("#app > main > div > div.theMain > div > div.theWeatherLv3_container > div > div.weatherLv3Status_info > div > div.weatherLv3Status_info_data > div.weatherLv3Status_info_data_block.temp > div.dataBlock_subBlock.pastTemp > span.minTemp > span.dataBlock_value")
    driver.close()
    columns = ["number","tempelture","max","min"]
    sql = 'insert into rea (time,tmp,max,min) values (?,?,?,?)'
    data = (float(str('0')),float(str(p.string)),float(str(pmax.string)),float(str(pmin.string)))
    cursor.execute(sql,data)
    connection.commit()
    df = pd.DataFrame(columns=columns) # 列名を指定する
    ##行を増やす
    count=1
    se = pd.Series(["0",p.string,pmax.string,pmin.string], columns) 
    df = df.append(se, columns)
    #####5分　一時間なら12 三時間なら36
    while count<2:
        comp = datetime.now()
        diff = comp.minute - now.minute
        if diff>=count*5:
            p=""
            count=count+1
            ####2回目
            driver = webdriver.Chrome(executable_path='C:\\Users\ynish\Desktop\gitpractice\chromedriver_win32\chromedriver.exe')###chroedriver.exeを入れた場所を指定
            driver.get("https://www.nhk.or.jp/kishou-saigai/city/status/13109001310900/")
            html = driver.page_source.encode('utf-8')
            # BeautifulSoupで扱えるようにパースします
            soup = BeautifulSoup(html, "html.parser")
            # idがheikinの要素を表示
            p=""
            pmax=""
            pmin=""
            p=soup.select_one("#app > main > div > div.theMain > div > div.theWeatherLv3_container > div > div.weatherLv3Status_info > div > div.weatherLv3Status_info_data > div.weatherLv3Status_info_data_block.temp > span.dataBlock_value")
            pmax=soup.select_one("#app > main > div > div.theMain > div > div.theWeatherLv3_container > div > div.weatherLv3Status_info > div > div.weatherLv3Status_info_data > div.weatherLv3Status_info_data_block.temp > div.dataBlock_subBlock.pastTemp > span.maxTemp > span.dataBlock_value")
            pmin=soup.select_one("#app > main > div > div.theMain > div > div.theWeatherLv3_container > div > div.weatherLv3Status_info > div > div.weatherLv3Status_info_data > div.weatherLv3Status_info_data_block.temp > div.dataBlock_subBlock.pastTemp > span.minTemp > span.dataBlock_value")
            driver.close()
            se = pd.Series([diff,p.string,pmax.string,pmin.string], columns) 
            df = df.append(se, columns)
            sql = 'insert into rea (time,tmp,max,min) values (?,?,?,?)'
            data = (float(str(diff)),float(str(p.string)),float(str(pmax.string)),float(str(pmin.string)))
            cursor.execute(sql,data)
            connection.commit()
    # 行を作成
    cursor.execute('SELECT * FROM rea')
    data = cursor.fetchall()
    print(data)
    df.to_csv("df1.csv")
