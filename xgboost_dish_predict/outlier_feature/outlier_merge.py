# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 19:09:23 2018

@author: shi.chao
"""

import time
import pandas as pd

# 合并 特征
def merge_feature():
    path_feature_1 = './/' + 'data_feature_1' + '.csv'
    file_feature_1 = open(path_feature_1)
    df_feature_1 = pd.read_csv(file_feature_1)
    df_feature_1['STAT_DATE'] = df_feature_1['STAT_DATE'].astype(str)
    df_feature_1['STAT_DATE'] = pd.to_datetime(df_feature_1['STAT_DATE'], format='%Y-%m-%d')
    df_feature_1 = df_feature_1.astype(str)
    
    
    path_outlier = './/' + 'outlier_4_03' + '.csv'
    file_outlier = open(path_outlier)
    df_outlier = pd.read_csv(file_outlier)
    df_outlier['STAT_DATE'] = df_outlier['STAT_DATE'].astype(str)
    df_outlier['STAT_DATE'] = pd.to_datetime(df_outlier['STAT_DATE'], format='%Y-%m-%d')
    df_outlier = df_outlier.astype(str)
    del df_outlier['STAT_DATE']
    del df_outlier['XMMC']
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
    
    path_outlier_outlier_feature_same_week_line_regression = './/' + 'outlier_feature_same_week_line_regression' + '.csv'
    file_outlier_outlier_feature_same_week_line_regression = open(path_outlier_outlier_feature_same_week_line_regression)
    df_outlier_outlier_feature_same_week_line_regression = pd.read_csv(file_outlier_outlier_feature_same_week_line_regression)
    df_outlier_outlier_feature_same_week_line_regression['STAT_DATE'] = df_outlier_outlier_feature_same_week_line_regression['STAT_DATE'].astype(str)
    df_outlier_outlier_feature_same_week_line_regression['STAT_DATE'] = pd.to_datetime(df_outlier_outlier_feature_same_week_line_regression['STAT_DATE'], format='%Y-%m-%d')
    df_outlier_outlier_feature_same_week_line_regression = df_outlier_outlier_feature_same_week_line_regression.astype(str)
    del df_outlier_outlier_feature_same_week_line_regression['STAT_DATE']
    del df_outlier_outlier_feature_same_week_line_regression['XMMC']
    del df_outlier_outlier_feature_same_week_line_regression['CMSL_outlier']
    del df_outlier_outlier_feature_same_week_line_regression['same_week1']
    del df_outlier_outlier_feature_same_week_line_regression['same_week2']
    del df_outlier_outlier_feature_same_week_line_regression['same_week3']
    del df_outlier_outlier_feature_same_week_line_regression['same_week4']
    del df_outlier_outlier_feature_same_week_line_regression['same_week1_sales_percent']
    
    path_date_to_str = './/' + 'feature_date_to_str' + '.csv'
    file_date_to_str = open(path_date_to_str)
    df_date_to_str = pd.read_csv(file_date_to_str)
    df_date_to_str['STAT_DATE'] = df_date_to_str['STAT_DATE'].astype(str)
    df_date_to_str['STAT_DATE'] = pd.to_datetime(df_date_to_str['STAT_DATE'], format='%Y-%m-%d')
    df_date_to_str = df_date_to_str.astype(str)
    del df_date_to_str['STAT_DATE']
    del df_date_to_str['XMMC']


    df_feature = pd.concat([df_feature_1, df_outlier, df_outlier_same_week1, df_outlier_same_week2, df_outlier_same_week3, df_outlier_same_week4 , df_outlier_same_week1_sales_percent,
                             df_outlier_outlier_feature_same_week_line_regression, df_date_to_str], axis=1)
    
    df_feature.to_csv('.//' + 'data_feature_11' + '.csv', index=False, encoding ='gbk')    
    print ()

if __name__ == '__main__':
    time_begin = time.time()
   
    merge_feature()
    
    time_end = time.time()
    print ("总共耗费了：%d  秒."%(time_end - time_begin))