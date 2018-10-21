# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 09:34:48 2018

@author: shi.chao
"""

import time
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


goal = 'CMSL_outlier'
#goal = 'CMSL'

# 加载数据，设定数值型和非数值型数据
def merge_same_week():
    path_outlier = './/' + 'outlier_4_03' + '.csv'
    file_outlier = open(path_outlier)
    df_outlier = pd.read_csv(file_outlier)
    df_outlier['STAT_DATE'] = df_outlier['STAT_DATE'].astype(str)
    df_outlier['STAT_DATE'] = pd.to_datetime(df_outlier['STAT_DATE'], format='%Y-%m-%d')
    df_outlier = df_outlier.astype(str)
    del df_outlier['CMSL']
    del df_outlier['day_of_week']
    del df_outlier['holiday']
         
    path_outlier_same_week1 = './/' + 'outlier_same_week1' + '.csv'
    file_outlier_same_week1 = open(path_outlier_same_week1)
    df_outlier_same_week1 = pd.read_csv(file_outlier_same_week1)
    df_outlier_same_week1['STAT_DATE'] = df_outlier_same_week1['STAT_DATE'].astype(str)
    df_outlier_same_week1['STAT_DATE'] = pd.to_datetime(df_outlier_same_week1['STAT_DATE'], format='%Y-%m-%d')
    df_outlier_same_week1 = df_outlier_same_week1.astype(str)
    del df_outlier_same_week1['STAT_DATE']
    del df_outlier_same_week1['XMMC']
    del df_outlier_same_week1['CMSL']
    del df_outlier_same_week1['CMSL_outlier']
    
    path_outlier_same_week2 = './/' + 'outlier_same_week2' + '.csv'
    file_outlier_same_week2 = open(path_outlier_same_week2)
    df_outlier_same_week2 = pd.read_csv(file_outlier_same_week2)
    df_outlier_same_week2['STAT_DATE'] = df_outlier_same_week2['STAT_DATE'].astype(str)
    df_outlier_same_week2['STAT_DATE'] = pd.to_datetime(df_outlier_same_week2['STAT_DATE'], format='%Y-%m-%d')
    df_outlier_same_week2 = df_outlier_same_week2.astype(str)
    del df_outlier_same_week2['STAT_DATE']
    del df_outlier_same_week2['XMMC']
    del df_outlier_same_week2['CMSL']
    del df_outlier_same_week2['CMSL_outlier']
    
    path_outlier_same_week3 = './/' + 'outlier_same_week3' + '.csv'
    file_outlier_same_week3 = open(path_outlier_same_week3)
    df_outlier_same_week3 = pd.read_csv(file_outlier_same_week3)
    df_outlier_same_week3['STAT_DATE'] = df_outlier_same_week3['STAT_DATE'].astype(str)
    df_outlier_same_week3['STAT_DATE'] = pd.to_datetime(df_outlier_same_week3['STAT_DATE'], format='%Y-%m-%d')
    df_outlier_same_week3 = df_outlier_same_week3.astype(str)
    del df_outlier_same_week3['STAT_DATE']
    del df_outlier_same_week3['XMMC']
    del df_outlier_same_week3['CMSL']
    del df_outlier_same_week3['CMSL_outlier']
    
    path_outlier_same_week4 = './/' + 'outlier_same_week4' + '.csv'
    file_outlier_same_week4 = open(path_outlier_same_week4)
    df_outlier_same_week4 = pd.read_csv(file_outlier_same_week4)
    df_outlier_same_week4['STAT_DATE'] = df_outlier_same_week4['STAT_DATE'].astype(str)
    df_outlier_same_week4['STAT_DATE'] = pd.to_datetime(df_outlier_same_week4['STAT_DATE'], format='%Y-%m-%d')
    df_outlier_same_week4 = df_outlier_same_week4.astype(str)
    del df_outlier_same_week4['STAT_DATE']
    del df_outlier_same_week4['XMMC']
    del df_outlier_same_week4['CMSL']
    del df_outlier_same_week4['CMSL_outlier']
    
    path_outlier_same_week1_sales_percent = './/' + 'outlier_same_week1_sales_percent' + '.csv'
    file_outlier_same_week1_sales_percent = open(path_outlier_same_week1_sales_percent)
    df_outlier_same_week1_sales_percent = pd.read_csv(file_outlier_same_week1_sales_percent)
    df_outlier_same_week1_sales_percent['STAT_DATE'] = df_outlier_same_week1_sales_percent['STAT_DATE'].astype(str)
    df_outlier_same_week1_sales_percent['STAT_DATE'] = pd.to_datetime(df_outlier_same_week1_sales_percent['STAT_DATE'], format='%Y-%m-%d')
    df_outlier_same_week1_sales_percent = df_outlier_same_week1_sales_percent.astype(str)
    del df_outlier_same_week1_sales_percent['STAT_DATE']
    del df_outlier_same_week1_sales_percent['XMMC']
    del df_outlier_same_week1_sales_percent['CMSL']
    del df_outlier_same_week1_sales_percent['CMSL_outlier']
    
    df_feature = pd.concat([df_outlier, df_outlier_same_week1, df_outlier_same_week2, df_outlier_same_week3, df_outlier_same_week4 , df_outlier_same_week1_sales_percent], axis=1)
    
    df_feature.to_csv('.//' + 'feature_same_week_line_regression' + '.csv', index=False, encoding ='gbk')    
    print ()
    
    

# 线性回归
def line_regression():
    
    path = ".//" + "feature_same_week_line_regression" + ".csv"
    train_f = open(path)
    data = pd.read_csv(train_f, low_memory=False, parse_dates=['STAT_DATE'])
    
    train_1 = data[data['STAT_DATE']>='2015-06-10'] 
    data_bj_dish_name_train = train_1[train_1['STAT_DATE']<='2017-08-14']
    data_train = data_bj_dish_name_train
    
    train = data_train.reset_index(drop=True)
    
    line_features = ['same_week1', 'same_week2', 'same_week3', 'same_week4', 'same_week1_sales_percent']
    
    coef_list = []
    for i in range(82):
        train_y = train.loc[i*791:i*791+791-1, goal].as_matrix(columns=None)
        train_y = np.array([train_y]).T
        train_x = train.loc[i*791:i*791+791-1, line_features].as_matrix(columns=None)
        lr = LinearRegression()
        lr.fit(train_x, train_y)
        coef_list.extend(lr.coef_.tolist())

#    print (coef_list)
    
    train_2 = data[data['STAT_DATE']>='2015-06-10'] 
    data_train_2 = train_2[train_2['STAT_DATE']<='2017-08-28']
    
    data_train_2 = data_train_2.reset_index(drop=True)
    
    same_week_line_regression_list_1 = []    
    for i in range(82):
        same_week_line_regression_list = []    
        for j in range(805):
            same_week_line_regression = coef_list[i][0]*data_train_2['same_week1'][i*805 + 805 -1 - j] + coef_list[i][1]*data_train_2['same_week2'][i*805 + 805 -1 - j] + coef_list[i][2]*data_train_2['same_week3'][i*805 + 805 -1 - j] + coef_list[i][3]*data_train_2['same_week4'][i*805 + 805 -1 - j] + coef_list[i][4]*data_train_2['same_week1_sales_percent'][i*805 + 805 -1 - j]
            same_week_line_regression_list.append(same_week_line_regression)
        for i in range(35):
            same_week_line_regression_list.append(0)
        same_week_line_regression_list.reverse()
        same_week_line_regression_list_1.extend(same_week_line_regression_list)
        
    df_same_week_line_regression = pd.DataFrame()
    df_same_week_line_regression['STAT_DATE'] = data['STAT_DATE']
    df_same_week_line_regression['XMMC'] = data['XMMC']
    df_same_week_line_regression['CMSL_outlier'] = data['CMSL_outlier']
    df_same_week_line_regression['same_week1'] = data['same_week1']
    df_same_week_line_regression['same_week2'] = data['same_week2']
    df_same_week_line_regression['same_week3'] = data['same_week3']
    df_same_week_line_regression['same_week4'] = data['same_week4']
    df_same_week_line_regression['same_week1_sales_percent'] = data['same_week1_sales_percent']
    df_same_week_line_regression['same_week_line_regression'] = same_week_line_regression_list_1
    
    df_same_week_line_regression.to_csv('.//' + 'outlier_feature_same_week_line_regression' + '.csv', encoding='gbk', index=False)
    
    print (same_week_line_regression_list)



if __name__ == '__main__':
    # 计算耗时
    time_begin = time.time()
    
    # 合并同星期销量均值维度
    merge_same_week()
    
    print('=>线性回归...')
    line_regression()
    
    
    time_end = time.time()
    print ("总共耗费了：%d  秒."%(time_end - time_begin))