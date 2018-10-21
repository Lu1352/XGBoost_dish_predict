# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 10:55:27 2018

@author: shi.chao
"""
import time
import pandas as pd



def add_same_week1():
    path_dish = './/' + 'outlier_4_03' + '.csv'
    file_dish = open(path_dish)
    df_dish = pd.read_csv(file_dish)
    df_dish['STAT_DATE'] = df_dish['STAT_DATE'].astype(str)
    df_dish['STAT_DATE'] = pd.to_datetime(df_dish['STAT_DATE'], format='%Y-%m-%d')
    
    df_same_week1 = pd.DataFrame()
    df_same_week1['STAT_DATE'] = df_dish['STAT_DATE']
    df_same_week1['XMMC'] = df_dish['XMMC']
    df_same_week1['CMSL'] = df_dish['CMSL']
    df_same_week1['CMSL_outlier'] = df_dish['CMSL_outlier']
    df_same_week1['CMSL_outlier'] = df_same_week1['CMSL_outlier'].astype(float)
    
    same_week1_list_1 = []
    for i in range(82):
        same_week1_list = []
        for j in range(840-14):
            same_week1_list.append(df_same_week1['CMSL_outlier'][i*840 + 840 - 14 - 1 - j])
        for i in range(14):
            same_week1_list.append(0)
        same_week1_list.reverse()
        same_week1_list_1.extend(same_week1_list)
    df_same_week1['same_week1'] = same_week1_list_1
    
    df_same_week1.to_csv('.//' + 'outlier_same_week1' + '.csv', encoding='gbk', index=False)
    
    print ()
    
    
    
    
    
if __name__ == '__main__':
    time_begin = time.time()
     
    add_same_week1()
    
    time_end = time.time()
    print ("总共耗费了：%d  秒."%(time_end - time_begin))