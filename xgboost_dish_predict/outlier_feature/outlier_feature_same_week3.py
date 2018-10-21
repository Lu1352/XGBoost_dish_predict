# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 16:22:52 2018

@author: shi.chao
"""

import time
import pandas as pd



def add_same_week3():
    path_dish = './/' + 'outlier_4_03' + '.csv'
    file_dish = open(path_dish)
    df_dish = pd.read_csv(file_dish)
    df_dish['STAT_DATE'] = df_dish['STAT_DATE'].astype(str)
    df_dish['STAT_DATE'] = pd.to_datetime(df_dish['STAT_DATE'], format='%Y-%m-%d')
    
    df_same_week3 = pd.DataFrame()
    df_same_week3['STAT_DATE'] = df_dish['STAT_DATE']
    df_same_week3['XMMC'] = df_dish['XMMC']
    df_same_week3['CMSL'] = df_dish['CMSL']
    df_same_week3['CMSL_outlier'] = df_dish['CMSL_outlier']
    df_same_week3['CMSL_outlier'] = df_same_week3['CMSL_outlier'].astype(float)
    
    same_week3_list_1 = []
    for i in range(82):
        same_week3_list = []
        for j in range(840-14):
            if(i*840 + 840 - 14 - 1 - 7*2 - j >= i * 840 ):
                outlier_week3_ave = (df_same_week3['CMSL_outlier'][i*840 + 840 - 14 - 1 - j] + df_same_week3['CMSL_outlier'][i*840 + 840 - 14 - 1 -7 - j] + df_same_week3['CMSL_outlier'][i*840 + 840 - 14 - 1 -7*2 - j])/3
                same_week3_list.append(outlier_week3_ave)
        for i in range(840-len(same_week3_list)):
            same_week3_list.append(0)
        same_week3_list.reverse()
        same_week3_list_1.extend(same_week3_list)
    df_same_week3['same_week3'] = same_week3_list_1
    
    df_same_week3.to_csv('.//' + 'outlier_same_week3' + '.csv', encoding='gbk', index=False)
    
    print ()
    
    
    
    
    
if __name__ == '__main__':
    time_begin = time.time()
     
    add_same_week3()
    
    time_end = time.time()
    print ("总共耗费了：%d  秒."%(time_end - time_begin))