# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 17:29:08 2018

@author: shi.chao
"""

import time 
import pandas as pd
import datetime



# 增加季节天气（按照农历） 
def add_season(date):
    date = datetime.datetime.strptime(date, "%Y-%m-%d")  
    date_20150506 = datetime.datetime.strptime('2015-05-06','%Y-%m-%d')  
    date_20150507 = datetime.datetime.strptime('2015-05-07','%Y-%m-%d')  
    date_20150808 = datetime.datetime.strptime('2015-08-08','%Y-%m-%d')  
    date_20151108 = datetime.datetime.strptime('2015-11-08','%Y-%m-%d')  
    date_20160204 = datetime.datetime.strptime('2016-02-04','%Y-%m-%d')  
    date_20160505 = datetime.datetime.strptime('2016-05-05','%Y-%m-%d')  
    date_20160807 = datetime.datetime.strptime('2016-08-07','%Y-%m-%d')  
    date_20161107 = datetime.datetime.strptime('2016-11-07','%Y-%m-%d')  
    date_20170203 = datetime.datetime.strptime('2017-02-03','%Y-%m-%d')  
    date_20170505 = datetime.datetime.strptime('2017-05-05','%Y-%m-%d')  
    date_20170807 = datetime.datetime.strptime('2017-08-07','%Y-%m-%d')  
    date_20171107 = datetime.datetime.strptime('2017-11-07','%Y-%m-%d')  
    if(date<=date_20150506):
        return 1
    elif(date>=date_20150507) and (date<date_20150808):
        return 2
    elif(date>=date_20150808) and (date<date_20151108):
        return 3
    elif(date>=date_20151108) and (date<date_20160204) :
        return 4
    elif(date>=date_20160204) and (date<date_20160505) :
        return 1    
    elif(date>=date_20160505) and (date<date_20160807):
        return 2
    elif(date>=date_20160807) and (date<date_20161107) :
        return 3
    elif(date>=date_20161107) and (date<date_20170203) :
        return 4
    elif(date>=date_20170203) and (date<date_20170505) :
        return 1
    elif(date>=date_20170505) and (date<date_20170807) :
        return 2
    elif(date>=date_20170807) and (date<date_20171107) :
        return 3
    


if __name__ == '__main__':
    time_begin = time.time()
    
#    df_dish = df_dish.set_index('STAT_DATE')
    df_dish = pd.DataFrame()
    path_dish = '..//data//' + 'data_bj12_dish_82_3' + '.csv'
    file_dish = open(path_dish)
    #df_dish = pd.read_csv(file_dish, low_memory=False, parse_dates=['STAT_DATE'])
    df_dish = pd.read_csv(file_dish)
    df_dish['STAT_DATE'] = df_dish['STAT_DATE'].astype(str)
    df_dish['STAT_DATE'] = pd.to_datetime(df_dish['STAT_DATE'], format='%Y-%m-%d')
    df_dish = df_dish.astype(str)
    
    df_season = pd.DataFrame()
    
    df_season['STAT_DATE'] = df_dish['STAT_DATE']
    df_season['XMMC'] = df_dish['XMMC']
    

    season_list = []
    for date in list(df_dish['STAT_DATE']):
        season_value = add_season(date)
        season_list.append(season_value)
    df_season['season'] = season_list
    df_season.to_csv('.//' + 'season' + '.csv', encoding='gbk', index=False)
    print (df_season)
    
    
    time_end = time.time()
    print ("总共耗费了：%d  秒."%(time_end - time_begin))