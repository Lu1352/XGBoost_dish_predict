# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 14:31:11 2018

@author: shi.chao
"""

import pandas as pd

'''
添加星期特征
'''
def day_of_week(date):
    date_result = pd.to_datetime(date).dayofweek
    return list(date_result)


if __name__=='__main__':
    path_dish = '..//data//' + 'data_bj12_dish_82_3' + '.csv'
    file_dish = open(path_dish)
    df_dish = pd.read_csv(file_dish)
    df_dish['STAT_DATE'] = df_dish['STAT_DATE'].astype(str)
    df_dish['STAT_DATE'] = pd.to_datetime(df_dish['STAT_DATE'], format='%Y-%m-%d')
    df_dish = df_dish.astype(str)
    
    df_day_of_week = pd.DataFrame()
    day_of_week_list = day_of_week(list(df_dish['STAT_DATE']))
    
    df_day_of_week['STAT_DATE'] = df_dish['STAT_DATE']
    df_day_of_week['XMMC'] = df_dish['XMMC']
    df_day_of_week['day_of_week'] = day_of_week_list
    
    df_day_of_week.to_csv('.//' + 'day_of_week' + '.csv', index=False, encoding ='gbk')
    
    
   