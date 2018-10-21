# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 18:04:20 2018

@author: shi.chao
"""

import time
import pandas as pd
from sklearn.preprocessing import LabelEncoder 


# 将类别进行数值化处理（店铺名称、菜品编码、XMBH、菜品名称、菜品单位、单价、类别、ZKZT）
def catogroy_to_num():
    path = '..//data//' + 'data_bj12_dish_82_3' + '.csv'
    file = open(path)
    df_dish = pd.read_csv(file)
    df_dish['STAT_DATE'] = df_dish['STAT_DATE'].astype(str)
    df_dish['STAT_DATE'] = pd.to_datetime(df_dish['STAT_DATE'], format='%Y-%m-%d')
    df_dish = df_dish.astype(str)
    
    # 店铺名称
    store_name_num_list = []
    store_name_num = LabelEncoder()
    store_name_num_list = store_name_num.fit_transform(df_dish['STORE_NAME'].values)  
    
    # 菜品名称
    xmmc_num_list = []
    xmmc_num = LabelEncoder()
    xmmc_num_list = xmmc_num.fit_transform(df_dish['XMMC'].values)  
    
    # 菜品单位
    dwbh_num_list = []
    dwbh_num = LabelEncoder()
    dwbh_num_list = dwbh_num.fit_transform(df_dish['DWBH'].values)  
    
    # 菜品类别
    lbmc_num_list = []
    lbmc_num = LabelEncoder()
    lbmc_num_list = lbmc_num.fit_transform(df_dish['LBMC'].values)  
    
    # ZKZT
    zkzt_num_list = []
    zkzt_num = LabelEncoder()
    zkzt_num_list = zkzt_num.fit_transform(df_dish['ZKZT'].values)  
    
    catogroy_num = pd.DataFrame()
    catogroy_num['STAT_DATE'] = df_dish['STAT_DATE']
    catogroy_num['XMMC'] = df_dish['XMMC']
    
    catogroy_num['STORE_NAME_NUM'] = store_name_num_list 
    catogroy_num['XMID'] = df_dish['XMID']
    catogroy_num['XMBH'] = df_dish['XMBH']
    catogroy_num['XMMC_NUM'] = xmmc_num_list
    catogroy_num['DWBH_NUM'] = dwbh_num_list
    catogroy_num['CMSL'] = df_dish['CMSL']
    catogroy_num['CMDJ'] = df_dish['CMDJ']
    catogroy_num['LBMC_NUM'] = lbmc_num_list
    catogroy_num['ZKZT_NUM'] = zkzt_num_list
    catogroy_num['ZKL'] = df_dish['ZKL']
    
    catogroy_num.to_csv('.//' + 'catogroy_num' + '.csv', index=False, encoding ='gbk')
    print ()


if __name__ == '__main__':
    time_begin = time.time()
   
    catogroy_to_num()
    
    time_end = time.time()
    print ("总共耗费了：%d  秒."%(time_end - time_begin))