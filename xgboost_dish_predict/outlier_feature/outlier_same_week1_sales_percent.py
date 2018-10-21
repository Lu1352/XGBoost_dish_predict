# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 14:12:13 2018

@author: shi.chao
"""

import time
import pandas as pd



def add_week1_sales_percent():
    path_dish = './/' + 'outlier_4_03' + '.csv'
    file_dish = open(path_dish)
    df_dish = pd.read_csv(file_dish)
    df_dish['STAT_DATE'] = df_dish['STAT_DATE'].astype(str)
    df_dish['STAT_DATE'] = pd.to_datetime(df_dish['STAT_DATE'], format='%Y-%m-%d')
    
    df_same_week1_sales_percent = pd.DataFrame()
    df_same_week1_sales_percent['STAT_DATE'] = df_dish['STAT_DATE']
    df_same_week1_sales_percent['XMMC'] = df_dish['XMMC']
    df_same_week1_sales_percent['CMSL'] = df_dish['CMSL']
    df_same_week1_sales_percent['CMSL_outlier'] = df_dish['CMSL_outlier']
    df_same_week1_sales_percent['CMSL_outlier'] = df_same_week1_sales_percent['CMSL_outlier'].astype(float)
    
    same_week1_sales_percent_list_1 = []
    for i in range(82): # i*840
        same_week1_sales_percent_list = []
        for j in range(118): # j*7
            week_sum = 0
            for k in range(1, 8):
                if(i*840 + 840 - 14 - k - j*7>=0):
                    week_sum += df_same_week1_sales_percent['CMSL_outlier'][i*840 + 840 - 14 - k - j*7]
            for k in range(1, 8):
                if(i*840 + 840 - 14 - k - j*7>=0):
                    same_week1_sales_percent_list.append(df_same_week1_sales_percent['CMSL_outlier'][i*840 + 840 - 14 - k - j*7]/week_sum)
        for i in range(14):
            same_week1_sales_percent_list.append(0)
        same_week1_sales_percent_list.reverse()
        same_week1_sales_percent_list_1.extend(same_week1_sales_percent_list)
            
    df_same_week1_sales_percent['same_week1_sales_percent'] = same_week1_sales_percent_list_1
    
    df_same_week1_sales_percent.to_csv('.//' + 'outlier_same_week1_sales_percent' + '.csv', encoding='gbk', index=False)
    
    print ()
    
    
    
    
    
if __name__ == '__main__':
    time_begin = time.time()
     
    add_week1_sales_percent()
    
    time_end = time.time()
    print ("总共耗费了：%d  秒."%(time_end - time_begin))