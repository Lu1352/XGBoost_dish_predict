# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 16:28:35 2018

@author: shi.chao
"""

import pandas as pd

'''
添加 节假日 特征（上班为0，周末为1，法定节假日为2）
'''
def holiday(holiday):
    holiday_list = []
    for i in range(82):
        holiday_list.extend(holiday)
    return holiday_list



if __name__ == '__main__':
    path_dish = './/' + 'holiday' + '.csv'
    file_dish = open(path_dish)
    df_dish = pd.read_csv(file_dish)
    df_dish['STAT_DATE'] = df_dish['STAT_DATE'].astype(str)
    df_dish['STAT_DATE'] = pd.to_datetime(df_dish['STAT_DATE'], format='%Y-%m-%d')
    df_dish = df_dish.astype(str)
    
    holiday_1 = pd.DataFrame()
    holiday_1_list = holiday(list(df_dish['holiday'][:845]))
    
    holiday_1['STAT_DATE'] = df_dish['STAT_DATE']
    holiday_1['XMMC'] = df_dish['XMMC']
    holiday_1['holiday'] = holiday_1_list
    
    holiday_1.to_csv('.//' + 'holiday_1' + '.csv', index=False, encoding ='gbk')
    
    
    
    
