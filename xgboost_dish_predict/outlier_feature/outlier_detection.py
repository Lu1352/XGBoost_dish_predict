# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 15:20:24 2018

@author: shi.chao
"""

import time
import pandas as pd
import numpy as np

# 划分数据
def load_data(data):
    data_bj_dish_name_train = data[data['STAT_DATE']>='2015-05-06'] 
#    data_bj_dish_name_train = train_1[train_1['STAT_DATE']<='2017-08-14']
    data_bj_dish_name_train.set_index('STAT_DATE', inplace=True)
    data_bj_dish_name_train.to_csv('.//' + 'data_feature_1' + '.csv', encoding='gbk')

## 异常值检测处理
def check_outlier():
    path_dish = './/' + 'data_feature_1' + '.csv'
    file_dish = open(path_dish)
    df_dish = pd.read_csv(file_dish)
    df_dish['STAT_DATE'] = df_dish['STAT_DATE'].astype(str)
    df_dish['STAT_DATE'] = pd.to_datetime(df_dish['STAT_DATE'], format='%Y-%m-%d')
#    df_dish = df_dish.astype(str)
    
    df_outlier_detection = pd.DataFrame()
    df_outlier_detection['STAT_DATE'] = df_dish['STAT_DATE']
    df_outlier_detection['XMMC'] = df_dish['XMMC']
    df_outlier_detection['CMSL'] = df_dish['CMSL']
    df_outlier_detection['CMSL_outlier'] = df_dish['CMSL']
    
    ### 用两周内异常处理
    for i in range(82):
        for j in range(60):
            df_temp = pd.DataFrame()
            df_temp['a'] = df_outlier_detection['CMSL'][i*840+j*14:i*840+j*14+14]
            Percentile = np.percentile(df_temp['a'],[0,25,50,75,100])
            IQR = Percentile[3] - Percentile[1]
            UpLimit = Percentile[3] + IQR*1.5
            DownLimit = Percentile[1] - IQR*1.5
            for k in range(14):
                '''if (i*840+j*14+k==6471-2):
                    print (111)
#                print (i*840+j*14+k)'''
                if(df_outlier_detection['CMSL_outlier'][i*840+j*14+k]>=UpLimit or df_outlier_detection['CMSL_outlier'][i*840+j*14+k]<=DownLimit):
#                    df_outlier_detection['CMSL_outlier'][i*840+j*14+k] = df_outlier_detection['CMSL'][i*840+j*14+k-7]
#                    df_outlier_detection['CMSL_outlier'][i*840+j*14+k] = (df_outlier_detection['CMSL'][i*840+j*14+k-7]+df_outlier_detection['CMSL'][i*840+j*14+k-7*2])/2.0
#                if():
#                    df_outlier_detection['CMSL_outlier'][i*840+j*14+k] = df_outlier_detection['CMSL'][i*840+j*14+k-7]
#                    df_outlier_detection['CMSL_outlier'][i*840+j*14+k] = (df_outlier_detection['CMSL'][i*840+j*14+k-7]+df_outlier_detection['CMSL'][i*840+j*14+k-7*2])/2.0
                    if(i*840+j*14+k-7>=i*840+j*14): 
                        df_outlier_detection['CMSL_outlier'][i*840+j*14+k] = df_outlier_detection['CMSL'][i*840+j*14+k-7]
                    else:
                        if(df_outlier_detection['CMSL'][i*840+j*14+k+7]>=UpLimit or df_outlier_detection['CMSL'][i*840+j*14+k+7]<=DownLimit):
                            df_outlier_detection['CMSL'][i*840+j*14+k+7] = Percentile[3]
                        df_outlier_detection['CMSL_outlier'][i*840+j*14+k] = df_outlier_detection['CMSL'][i*840+j*14+k+7]
            
    df_outlier_detection.to_csv('.//' + 'outlier' + '.csv', encoding='gbk', index=False)      


'''
重新规划调整：异常值处理
   以四个星期 为一个单位故有 30 个 4*7 滑动窗口。
   每个 4个 7天的 数据分为 两部分，一部分为周一到周五的20个周内数据做异常检测：
   第二部分的周末的 8 个数据为异常检测：
    Percentile = np.percentile(df['a'],[0,25,50,75,100])
    IQR = Percentile[3] - Percentile[1]
    UpLimit = Percentile[3] + IQR*1.5
    DownLimit = Percentile[1] - IQR*1.5
   异常处理：小于 下限 的用 下四分位数Percentile[1] 替换 ；大于 上限 的用上四分位数 Percentile[3] 代替。
   做完 星期 异常值之后，再做 节假日异常处理，取出所有节假日销量数据，（holiday==2），做异常处理（手动）'''
def check_outlier_30_7():
    path_dish = './/' + 'data_feature_1' + '.csv'
    file_dish = open(path_dish)
    df_dish = pd.read_csv(file_dish)
    df_dish['STAT_DATE'] = df_dish['STAT_DATE'].astype(str)
    df_dish['STAT_DATE'] = pd.to_datetime(df_dish['STAT_DATE'], format='%Y-%m-%d')
    
    df_outlier_detection = pd.DataFrame()
    df_outlier_detection['STAT_DATE'] = df_dish['STAT_DATE']
    df_outlier_detection['XMMC'] = df_dish['XMMC']
    df_outlier_detection['CMSL'] = df_dish['CMSL']
    df_outlier_detection['CMSL_outlier'] = df_dish['CMSL']
    df_outlier_detection['CMSL_outlier'] = df_outlier_detection['CMSL_outlier'].astype(float)
    df_outlier_detection['day_of_week'] = df_dish['day_of_week']
    df_outlier_detection['holiday'] = df_dish['holiday']
    
    ### 处理周内和周末销量异常的数据
    for i in range(82):
        for j in range(30):
            work_day = []
            week_end = []
            for k in range(28):
                if(df_outlier_detection['day_of_week'][i*840+j*28+k]==1 or df_outlier_detection['day_of_week'][i*840+j*28+k]==2 or df_outlier_detection['day_of_week'][i*840+j*28+k]==3 or df_outlier_detection['day_of_week'][i*840+j*28+k]==4 or df_outlier_detection['day_of_week'][i*840+j*28+k]==0):
                    work_day.append(df_outlier_detection['CMSL_outlier'][i*840+j*28+k])
                if(df_outlier_detection['day_of_week'][i*840+j*28+k]==5 or df_outlier_detection['day_of_week'][i*840+j*28+k]==6):
                    week_end.append(df_outlier_detection['CMSL_outlier'][i*840+j*28+k])
            
            df_work_day = pd.DataFrame()
            df_work_day['a'] = work_day
            Percentile_work_day = np.percentile(df_work_day['a'], [0,25,50,75,100])
            IQR_work_day = Percentile_work_day[3] - Percentile_work_day[1]
            UpLimit_work_day = Percentile_work_day[3] + IQR_work_day*0.3
            DownLimit_work_day = Percentile_work_day[1] - IQR_work_day*0.3
            
            df_week_end = pd.DataFrame()
            df_week_end['a'] = week_end
            Percentile_week_end = np.percentile(df_week_end['a'], [0,25,50,75,100])
            IQR_week_end = Percentile_week_end[3] - Percentile_week_end[1]
            UpLimit_week_end = Percentile_week_end[3] + IQR_week_end*0.3
            DownLimit_week_end = Percentile_week_end[1] - IQR_week_end*0.3
            
            for k in range(28):
                if(df_outlier_detection['day_of_week'][i*840+j*28+k]==1 or df_outlier_detection['day_of_week'][i*840+j*28+k]==2 or df_outlier_detection['day_of_week'][i*840+j*28+k]==3 or df_outlier_detection['day_of_week'][i*840+j*28+k]==4 or df_outlier_detection['day_of_week'][i*840+j*28+k]==0):
                    if(df_outlier_detection['CMSL_outlier'][i*840+j*28+k]>=UpLimit_work_day):
                        df_outlier_detection['CMSL_outlier'][i*840+j*28+k] = Percentile_work_day[3]
                    if(df_outlier_detection['CMSL_outlier'][i*840+j*28+k]<=DownLimit_work_day):
                        df_outlier_detection['CMSL_outlier'][i*840+j*28+k] = Percentile_work_day[1]
                if(df_outlier_detection['day_of_week'][i*840+j*28+k]==5 or df_outlier_detection['day_of_week'][i*840+j*28+k]==6):
                    if(df_outlier_detection['CMSL_outlier'][i*840+j*28+k]>=UpLimit_week_end):
                        df_outlier_detection['CMSL_outlier'][i*840+j*28+k] = Percentile_week_end[3]
                    if(df_outlier_detection['CMSL_outlier'][i*840+j*28+k]<=DownLimit_week_end):
                        df_outlier_detection['CMSL_outlier'][i*840+j*28+k] = Percentile_week_end[1]
    # 处理法定节假日的异常销量数据
    for i in range(82):
        for m in range(2):
            holiday_outlier = []
            for n in range(420):
                if(df_outlier_detection['holiday'][i*840+m*420+n]==2):
                    holiday_outlier.append(df_outlier_detection['CMSL'][i*840+m*420+n])  
            df_holiday_outlier = pd.DataFrame()
            df_holiday_outlier['a'] = holiday_outlier
            Percentile_holiday_outlier = np.percentile(df_holiday_outlier['a'], [0,25,50,75,100])
            IQR_holiday_outlier = Percentile_holiday_outlier[3] - Percentile_holiday_outlier[1]
            UpLimit_holiday_outlier = Percentile_holiday_outlier[3] + IQR_holiday_outlier*0.3
            DownLimit_holiday_outlier = Percentile_holiday_outlier[1] - IQR_holiday_outlier*0.3
            for n in range(420):
                if(df_outlier_detection['holiday'][i*840+m*420+n]==2):
                    if(df_outlier_detection['CMSL'][i*840+m*420+n]>=UpLimit_holiday_outlier):
                        df_outlier_detection['CMSL_outlier'][i*840+m*420+n] = Percentile_holiday_outlier[3]
                    if(df_outlier_detection['CMSL'][i*840+m*420+n]<=DownLimit_holiday_outlier):
                        df_outlier_detection['CMSL_outlier'][i*840+m*420+n] = Percentile_holiday_outlier[1]
            
    df_outlier_detection.to_csv('.//' + 'outlier_4_03' + '.csv', encoding='gbk', index=False)      


### 处理节假日异常
def check_outlier_holiday():
    path_dish = './/' + 'data_feature_1' + '.csv'
    file_dish = open(path_dish)
    df_dish = pd.read_csv(file_dish)
    df_dish['STAT_DATE'] = df_dish['STAT_DATE'].astype(str)
    df_dish['STAT_DATE'] = pd.to_datetime(df_dish['STAT_DATE'], format='%Y-%m-%d')
    
    df_tem = pd.DataFrame()
    df_tem = df_dish[df_dish['XMMC']=='(B)冬瓜(半)']
    
    df_outlier_holiday = pd.DataFrame()
    df_outlier_holiday = df_tem[df_tem['holiday']==2]
    
    print (df_outlier_holiday)





if __name__ == '__main__':
    time_begin = time.time()
    ## 划分成 60个 *14 的时间段，进行处理，整星期方便处理
    '''path = ".//" + "data_feature" + ".csv"
    train_f = open(path)
    data = pd.read_csv(train_f, low_memory=False, parse_dates=['STAT_DATE'])
    print('=>载入数据中...')
    load_data(data)'''
    
    ### 异常值检测处理
#    check_outlier()
    
    check_outlier_30_7()
    
#    check_outlier_holiday()
    
    
    time_end = time.time()
    print ("总共耗费了：%d  秒."%(time_end - time_begin))