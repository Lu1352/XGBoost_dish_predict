# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 16:49:56 2018

@author: shi.chao
"""

import time
import pandas as pd

# 增加年、月、日 特征
def add_year_month_day():
    path = '..//data//' + 'data_bj12_dish_82_3' + '.csv'
    file = open(path)
    df_dish = pd.read_csv(file)
    df_dish['STAT_DATE'] = df_dish['STAT_DATE'].astype(str)
    df_dish['STAT_DATE'] = pd.to_datetime(df_dish['STAT_DATE'], format='%Y-%m-%d')
    
    df_dish = df_dish.astype(str)
    
    year_list = []
    month_list = []
    day_list = []
    
    for date in df_dish['STAT_DATE']:
        year_list.append(date.split('-')[0])
        month_list.append(date.split('-')[1])
        day_list.append(date.split('-')[2])
        
     
    year_month_day = pd.DataFrame()
    year_month_day['STAT_DATE'] = df_dish['STAT_DATE']
    year_month_day['XMMC'] = df_dish['XMMC']
    year_month_day['year'] = year_list
    year_month_day['month'] = month_list
    year_month_day['day'] = day_list
    
    year_month_day['year'] = year_month_day['year'].astype(int)
    year_month_day['month'] = year_month_day['month'].astype(int)
    year_month_day['day'] = year_month_day['day'].astype(int)
    
    year_month_day.to_csv('.//' + 'year_month_day' + '.csv', index=False, encoding ='gbk')


if __name__ == '__main__':
    time_begin = time.time()
    
    add_year_month_day()
    
    time_end = time.time()
    print ("总共耗费了：%d  秒."%(time_end - time_begin))