# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 17:49:41 2018

@author: shi.chao
"""

import time
import pandas as pd

# 合并 特征
def merge_feature():
    path_catogroy_num = './/' + 'catogroy_num' + '.csv'
    file_catogroy_num = open(path_catogroy_num)
    df_catogroy_num = pd.read_csv(file_catogroy_num)
    df_catogroy_num['STAT_DATE'] = df_catogroy_num['STAT_DATE'].astype(str)
    df_catogroy_num['STAT_DATE'] = pd.to_datetime(df_catogroy_num['STAT_DATE'], format='%Y-%m-%d')
    df_catogroy_num = df_catogroy_num.astype(str)
    
    path_holiday = './/' + 'holiday_1' + '.csv'
    file_holiday = open(path_holiday)
    df_holiday = pd.read_csv(file_holiday)
    df_holiday['STAT_DATE'] = df_holiday['STAT_DATE'].astype(str)
    df_holiday['STAT_DATE'] = pd.to_datetime(df_holiday['STAT_DATE'], format='%Y-%m-%d')
    df_holiday = df_holiday.astype(str)
    del df_holiday['STAT_DATE']
    del df_holiday['XMMC']
    
    path_day_of_week = './/' + 'day_of_week' + '.csv'
    file_day_of_week = open(path_day_of_week)
    df_day_of_week = pd.read_csv(file_day_of_week)
    df_day_of_week['STAT_DATE'] = df_day_of_week['STAT_DATE'].astype(str)
    df_day_of_week['STAT_DATE'] = pd.to_datetime(df_day_of_week['STAT_DATE'], format='%Y-%m-%d')
    df_day_of_week = df_day_of_week.astype(str)
    del df_day_of_week['STAT_DATE']
    del df_day_of_week['XMMC']
    
    path_year_month_day = './/' + 'year_month_day' + '.csv'
    file_year_month_day = open(path_year_month_day)
    df_year_month_day = pd.read_csv(file_year_month_day)
    df_year_month_day['STAT_DATE'] = df_year_month_day['STAT_DATE'].astype(str)
    df_year_month_day['STAT_DATE'] = pd.to_datetime(df_year_month_day['STAT_DATE'], format='%Y-%m-%d')
    df_year_month_day = df_year_month_day.astype(str)
    del df_year_month_day['STAT_DATE']
    del df_year_month_day['XMMC']
    
    path_weather_ssd_2 = './/' + 'weather_ssd_2' + '.csv'
    file_weather_ssd_2 = open(path_weather_ssd_2)
    df_weather_ssd_2 = pd.read_csv(file_weather_ssd_2)
    df_weather_ssd_2['STAT_DATE'] = df_weather_ssd_2['STAT_DATE'].astype(str)
    df_weather_ssd_2['STAT_DATE'] = pd.to_datetime(df_weather_ssd_2['STAT_DATE'], format='%Y-%m-%d')
    df_weather_ssd_2 = df_weather_ssd_2.astype(str)
    del df_weather_ssd_2['STAT_DATE']
    del df_weather_ssd_2['XMMC']
    
    path_season = './/' + 'season' + '.csv'
    file_season = open(path_season)
    df_season = pd.read_csv(file_season)
    df_season['STAT_DATE'] = df_season['STAT_DATE'].astype(str)
    df_season['STAT_DATE'] = pd.to_datetime(df_season['STAT_DATE'], format='%Y-%m-%d')
    df_season = df_season.astype(str)
    del df_season['STAT_DATE']
    del df_season['XMMC']
    
    path_outlier = './/outlier_detection_and_feature//' + 'outlier' + '.csv'
    file_outlier = open(path_outlier)
    df_outlier = pd.read_csv(file_outlier)
    df_outlier['STAT_DATE'] = df_outlier['STAT_DATE'].astype(str)
    df_outlier['STAT_DATE'] = pd.to_datetime(df_outlier['STAT_DATE'], format='%Y-%m-%d')
    df_outlier = df_outlier.astype(str)
    del df_outlier['STAT_DATE']
    del df_outlier['XMMC']
    del df_outlier['CMSL']

    

    df_feature = pd.concat([ df_catogroy_num, df_holiday, df_day_of_week, df_year_month_day, 
                            df_weather_ssd_2, df_season, df_outlier], axis=1)
    df_feature.to_csv('.//' + 'data_feature' + '.csv', index=False, encoding ='gbk')    
    print ()

if __name__ == '__main__':
    time_begin = time.time()
   
    merge_feature()
    
    time_end = time.time()
    print ("总共耗费了：%d  秒."%(time_end - time_begin))