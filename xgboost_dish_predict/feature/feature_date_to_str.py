# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 11:33:49 2018

@author: shi.chao
"""

import time
import pandas as pd
import datetime



def date_to_str():
    path_dish = './/' + 'data_feature_11' + '.csv'
    file_dish = open(path_dish)
    df_dish = pd.read_csv(file_dish)
    df_dish['STAT_DATE'] = df_dish['STAT_DATE'].astype(str)
    df_dish['STAT_DATE'] = pd.to_datetime(df_dish['STAT_DATE'], format='%Y-%m-%d')
    
    df_date_to_str = pd.DataFrame()
    df_date_to_str['STAT_DATE'] = df_dish['STAT_DATE']
    df_date_to_str['XMMC'] = df_dish['XMMC']
    df_date_to_str['date'] = df_dish['STAT_DATE']
    
#    df_date_to_str['date'] = pd.to_datetime(df_date_to_str['date'], format='%Y%m%d')
    date_list = []
    for date in df_date_to_str['date']:
        date_list.append(date.strftime('%Y%m%d'))
        
    df_date_to_str['date'] = date_list
    
    df_date_to_str.to_csv('.//' + 'feature_date_to_str' + '.csv', encoding='gbk', index=False)
    
    print ()
    
    

if __name__ == '__main__':
    time_begin = time.time()
   
    date_to_str()
    
    time_end = time.time()
    print ("总共耗费了：%d  秒."%(time_end - time_begin))