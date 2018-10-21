# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 11:27:36 2018

@author: shi.chao
"""

import time
import pandas as pd




def get_dummies():
    path_dish = './/' + 'data_feature_11' + '.csv'
    file_dish = open(path_dish)
    df_dish = pd.read_csv(file_dish)
    df_dish['STAT_DATE'] = df_dish['STAT_DATE'].astype(str)
    df_dish['STAT_DATE'] = pd.to_datetime(df_dish['STAT_DATE'], format='%Y-%m-%d')
    
    df_dish['holiday'] = df_dish['holiday'].astype(int)
    
    df_get_dummies = pd.DataFrame()
    df_get_dummies['STAT_DATE'] = df_dish['STAT_DATE']
    df_get_dummies['XMMC'] = df_dish['XMMC']
    df_get_dummies['day_of_week'] = df_dish['day_of_week']
    df_get_dummies['month'] = df_dish['month']
    df_get_dummies['holiday'] = df_dish['holiday']
    df_get_dummies['season'] = df_dish['season']
    df_get_dummies['weather'] = df_dish['weather']
    
    # 量化星期(1-7)
    get_dummies_day_of_week = pd.get_dummies(df_dish['day_of_week'], prefix='Week')
    df_dish = df_dish.join(get_dummies_day_of_week)
    # 量化月份(1-12)
    get_dummies_month = pd.get_dummies(df_dish['month'], prefix='Month')
    df_dish = df_dish.join(get_dummies_month)
    # 量化节假日(0-2)
    get_dummies_holiday = pd.get_dummies(df_dish['holiday'], prefix='Holiday')
    df_dish = df_dish.join(get_dummies_holiday)
    # 量化季节(1-4)
    get_dummies_season = pd.get_dummies(df_dish['season'], prefix='Season')
    df_dish = df_dish.join(get_dummies_season)
    # 量化天气(1-6)
    get_dummies_weather = pd.get_dummies(df_dish['weather'], prefix='Weather')
    df_dish = df_dish.join(get_dummies_weather)
    
    df_dish.to_csv('.//' + 'data_feature_12' + '.csv', encoding='gbk', index=False)
    
    print ()
    
    

if __name__ == '__main__':
    time_begin = time.time()
   
    get_dummies()
    
    time_end = time.time()
    print ("总共耗费了：%d  秒."%(time_end - time_begin))