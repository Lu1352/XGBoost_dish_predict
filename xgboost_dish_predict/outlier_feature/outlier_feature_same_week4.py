# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 16:31:50 2018

@author: shi.chao
"""

import time
import pandas as pd



def add_same_week4():
    path_dish = './/' + 'outlier_4_03' + '.csv'
    file_dish = open(path_dish)
    df_dish = pd.read_csv(file_dish)
    df_dish['STAT_DATE'] = df_dish['STAT_DATE'].astype(str)
    df_dish['STAT_DATE'] = pd.to_datetime(df_dish['STAT_DATE'], format='%Y-%m-%d')
    
    df_same_week4 = pd.DataFrame()
    df_same_week4['STAT_DATE'] = df_dish['STAT_DATE']
    df_same_week4['XMMC'] = df_dish['XMMC']
    df_same_week4['CMSL'] = df_dish['CMSL']
    df_same_week4['CMSL_outlier'] = df_dish['CMSL_outlier']
    df_same_week4['CMSL_outlier'] = df_same_week4['CMSL_outlier'].astype(float)
    
    same_week4_list_1 = []
    for i in range(82):
        same_week4_list = []
        for j in range(840-14):
            if(i*840 + 840 - 14 - 1 - 7*3 - j >= i * 840 ):
                outlier_week4_ave = (df_same_week4['CMSL_outlier'][i*840 + 840 - 14 - 1 - j] + df_same_week4['CMSL_outlier'][i*840 + 840 - 14 - 1 -7 - j] + df_same_week4['CMSL_outlier'][i*840 + 840 - 14 - 1 -7*2 - j] + df_same_week4['CMSL_outlier'][i*840 + 840 - 14 - 1 -7*3 - j])/4
                same_week4_list.append(outlier_week4_ave)
        for i in range(840-len(same_week4_list)):
            same_week4_list.append(0)
        same_week4_list.reverse()
        same_week4_list_1.extend(same_week4_list)
    df_same_week4['same_week4'] = same_week4_list_1
    
    df_same_week4.to_csv('.//' + 'outlier_same_week4' + '.csv', encoding='gbk', index=False)
    
    print ()
    
    
    
    
    
if __name__ == '__main__':
    time_begin = time.time()
     
    add_same_week4()
    
    time_end = time.time()
    print ("总共耗费了：%d  秒."%(time_end - time_begin))