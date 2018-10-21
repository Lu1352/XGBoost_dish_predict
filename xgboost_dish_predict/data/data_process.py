# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 10:19:27 2018

@author: shi.chao
"""

import time
import pandas as pd
import numpy as np


'''
合并十四店的销量等其它字段
'''
def combine_sales_by_date(num):
    path_dish_1516 = './/' + 'dishdetail14d_1516' + '_' + str(num) + '.csv'
    file_dish_1516 = open(path_dish_1516)
    df_dish_1516 = pd.read_csv(file_dish_1516)
    del df_dish_1516['ZDBH']  #账单编号  
    del df_dish_1516['ZWBH']  #座位编号
    del df_dish_1516['WDBZ']  #备注
    del df_dish_1516['BBBC']  #早晚市
    # 按日期、店铺名、菜品进行聚合分组
    grouped = df_dish_1516.groupby([df_dish_1516['STAT_DATE'], df_dish_1516['STORE_NAME'], df_dish_1516['XMID'], df_dish_1516['XMMC']]) 
    
    group_date = grouped['STAT_DATE'].agg(np.unique)  # 日期
    group_store_name = grouped['STORE_NAME'].agg(np.unique)  # 店名
    group_dish_id = grouped['XMID'].agg(np.unique)  # 菜品编码
    
    
    group_cmsl = grouped['CMSL'].agg(np.sum)  # 销量
    
    group_dish_xmbh = grouped['XMBH'].agg(np.unique)  # 菜品编码
    
    group_dish_name = grouped['XMMC'].agg(np.unique)  # 菜品名称
    
    
#    group_dish_unit = grouped['DWBH'].apply(np.unique)  # 菜品单位
    group_dish_unit = grouped.DWBH.unique()  # 菜品单位
#    group_dish_unit = grouped['DWBH'].agg(np.unique)  # 菜品单位
    
    group_dish_kind = grouped['LBMC'].agg(np.unique)  # 菜品大类
    
    group_price = grouped['CMDJ'].agg(np.mean)  # 单价
    group_predict_money = grouped['CPJE'].agg(np.sum)  # 应收金额
    group_reality_money = grouped['SJJE'].agg(np.sum)  # 应收金额
    group_zkzt = grouped['ZKZT'].agg(np.unique)  # ZKZT字段
    group_zkl = grouped['ZKL'].agg(np.mean)  # 折扣率
    
    # 创建一个空的 DataFrame
    df_dish_value = pd.DataFrame(columns=['STAT_DATE',	'STORE_NAME',	'XMID','XMBH',	
                                          'XMMC',	'DWBH',	'CMSL',	'CMDJ',	
                                          'LBMC',	'CPJE',	'SJJE','ZKZT', 'ZKL'])
    df_dish_value['STAT_DATE'] = group_date
    df_dish_value['STORE_NAME'] = group_store_name
    df_dish_value['XMID'] = group_dish_id
    df_dish_value['XMBH'] = group_dish_xmbh
    df_dish_value['XMMC'] = group_dish_name
    df_dish_value['DWBH'] = group_dish_unit
    xmmc_list = []
    xmmc_unit = df_dish_value['DWBH']
    for i in range(len(df_dish_value)):
#        xmmc_unit[i] = str(xmmc_unit[i])
        xmmc_list.append(str(xmmc_unit[i]).split("'")[1])
    df_dish_value['DWBH'] = xmmc_list
        
    df_dish_value['CMSL'] = group_cmsl
    df_dish_value['CMDJ'] = group_price
    df_dish_value['LBMC'] = group_dish_kind
    df_dish_value['CPJE'] = group_predict_money
    df_dish_value['SJJE'] = group_reality_money
    df_dish_value['ZKZT'] = group_zkzt
    df_dish_value['ZKL'] = group_zkl
    
    df_dish_value.to_csv('.//' + 'dishdetail14d_1516_gruoupby_' + str(num) + '.csv', index=False, encoding='gbk')   
    
    print()

# 求字符串中子串的众数
def max_count_str(df, col):
    dwbh = df[col]
    mode = []
    arr_appear = dict((a, dwbh.count(a)) for a in dwbh)  # 统计各个元素出现的次数
    if max(arr_appear.values()) == 1:  # 如果最大的出现为1
        return  # 则没有众数
    else:
        for k, v in arr_appear.items():  # 否则，出现次数最大的数字，就是众数
            if v == max(arr_appear.values()):
                mode.append(k)
    return dwbh[0]


def  combine_sales_by_date_1617(num):
    path_dish_1617 = './/' + 'dishdetail14d_1617' + '_' + str(num) + '.csv'
    file_dish_1617 = open(path_dish_1617)
    df_dish_1617 = pd.read_csv(file_dish_1617)
    del df_dish_1617['ZDBH']  #账单编号  
    del df_dish_1617['ZWBH']  #座位编号
    del df_dish_1617['WDBZ']  #备注
    del df_dish_1617['BBBC']  #早晚市
    # 按日期、店铺名、菜品进行聚合分组
    grouped = df_dish_1617.groupby([df_dish_1617['STAT_DATE'], df_dish_1617['STORE_NAME'], df_dish_1617['XMID'], df_dish_1617['XMMC']]) 
    
    group_date = grouped['STAT_DATE'].agg(np.unique)  # 日期
    group_store_name = grouped['STORE_NAME'].agg(np.unique)  # 店名
    group_dish_id = grouped['XMID'].agg(np.unique)  # 菜品编码
    
    
    group_cmsl = grouped['CMSL'].agg(np.sum)  # 销量
    
    group_dish_xmbh = grouped['XMBH'].agg(np.unique)  # 菜品编码
    
    group_dish_name = grouped['XMMC'].agg(np.unique)  # 菜品名称
    group_dish_unit = grouped['DWBH'].agg(np.unique)  # 菜品单位
    group_dish_kind = grouped['LBMC'].agg(np.unique)  # 菜品大类
    
    group_price = grouped['CMDJ'].agg(np.mean)  # 单价
    group_predict_money = grouped['CPJE'].agg(np.sum)  # 应收金额
    group_reality_money = grouped['SJJE'].agg(np.sum)  # 应收金额
    group_zkzt = grouped['ZKZT'].agg(np.unique)  # ZKZT字段
    group_zkl = grouped['ZKL'].agg(np.mean)  # 折扣率
    
    # 创建一个空的 DataFrame
    df_dish_value = pd.DataFrame(columns=['STAT_DATE',	'STORE_NAME',	'XMID','XMBH',	
                                          'XMMC',	'DWBH',	'CMSL',	'CMDJ',	
                                          'LBMC',	'CPJE',	'SJJE','ZKZT', 'ZKL'])
    df_dish_value['STAT_DATE'] = group_date
    df_dish_value['STORE_NAME'] = group_store_name
    df_dish_value['XMID'] = group_dish_id
    df_dish_value['XMBH'] = group_dish_xmbh
    df_dish_value['XMMC'] = group_dish_name
    df_dish_value['DWBH'] = group_dish_unit
    df_dish_value['CMSL'] = group_cmsl
    df_dish_value['CMDJ'] = group_price
    df_dish_value['LBMC'] = group_dish_kind
    df_dish_value['CPJE'] = group_predict_money
    df_dish_value['SJJE'] = group_reality_money
    df_dish_value['ZKZT'] = group_zkzt
    df_dish_value['ZKL'] = group_zkl
    
    df_dish_value.to_csv('.//' + 'dishdetail14d_1617_gruoupby_' + str(num) + '.csv', index=False, encoding='gbk')   
    
    print()

'''
合并北京十二店的数据
'''
def combine_bj12_by_date_dish_name():
    path_dish_1516 = './/' + 'data_bj12' + '.csv'
    file_dish_1516 = open(path_dish_1516)
    df_dish_1516 = pd.read_csv(file_dish_1516)
    
    # 按日期、菜品名称进行聚合分组
    grouped = df_dish_1516.groupby([df_dish_1516['STAT_DATE'], df_dish_1516['XMMC']]) 
    
    group_date = grouped['STAT_DATE'].agg(np.unique)  # 日期
    group_store_name = grouped['STORE_NAME'].agg(np.unique)  # 店名
    ###########取众数
    group_dish_id = grouped['XMID'].agg(np.mean)  # 菜品编码
    
    group_cmsl = grouped['CMSL'].agg(np.sum)  # 销量
    ####取众数
    group_dish_xmbh = grouped['XMBH'].agg(np.mean)  # 菜品编码
    
    group_dish_name = grouped['XMMC'].agg(np.unique)  # 菜品名称
    
    group_dish_unit = grouped['DWBH'].agg(np.unique)  # 菜品单位
    ######取众数
    group_dish_kind = grouped['LBMC'].agg(np.unique)  # 菜品大类
    
    group_price = grouped['CMDJ'].agg(np.mean)  # 单价
    group_zkzt = grouped['ZKZT'].agg(np.unique)  # ZKZT字段
    group_zkl = grouped['ZKL'].agg(np.mean)  # 折扣率
    
    # 创建一个空的 DataFrame
    df_dish_value = pd.DataFrame(columns=['STAT_DATE',	'STORE_NAME',	'XMID','XMBH',	
                                          'XMMC',	'DWBH',	'CMSL',	'CMDJ',	
                                          'LBMC', 'ZKZT', 'ZKL'])
    df_dish_value['STAT_DATE'] = group_date
    df_dish_value['STORE_NAME'] = group_store_name
    df_dish_value['XMID'] = np.rint(group_dish_id)
    df_dish_value['XMBH'] = np.rint(group_dish_xmbh)
    df_dish_value['XMMC'] = group_dish_name
    df_dish_value['DWBH'] = group_dish_unit
    '''xmmc_list = []
    xmmc_unit = df_dish_value['DWBH']
    for i in range(len(df_dish_value)):
#        xmmc_unit[i] = str(xmmc_unit[i])
        xmmc_list.append(str(xmmc_unit[i]).split("'")[1])
    df_dish_value['DWBH'] = xmmc_list'''
        
    df_dish_value['CMSL'] = group_cmsl
    df_dish_value['CMDJ'] = group_price
    df_dish_value['LBMC'] = group_dish_kind
    df_dish_value['ZKZT'] = group_zkzt
    df_dish_value['ZKL'] = group_zkl
    
    df_dish_value.to_csv('.//' + 'data_bj12_dish_name' + '.csv', index=False, encoding='gbk')   
    
    print()


'''
再次合并北京十二店的数据
'''
def combine_bj12_by_date_dish_name_1():
    path_dish_1516 = './/' + 'data_bj12_dish_82' + '.csv'
    file_dish_1516 = open(path_dish_1516)
    df_dish_1516 = pd.read_csv(file_dish_1516)
    
    # 按日期、菜品名称进行聚合分组
    grouped = df_dish_1516.groupby([df_dish_1516['STAT_DATE'], df_dish_1516['XMMC']]) 
    
    group_date = grouped['STAT_DATE'].agg(zhong_shu)  # 日期
    group_store_name = grouped['STORE_NAME'].agg(zhong_shu)  # 店名
    ###########取众数
    group_dish_id = grouped['XMID'].agg(zhong_shu)  # 菜品编码
    
    group_cmsl = grouped['CMSL'].agg(np.sum)  # 销量
    ####取众数
    group_dish_xmbh = grouped['XMBH'].agg(zhong_shu)  # 菜品编码
    
    group_dish_name = grouped['XMMC'].agg(np.unique)  # 菜品名称
    
    group_dish_unit = grouped['DWBH'].agg(zhong_shu)  # 菜品单位
    ######取众数
    group_dish_kind = grouped['LBMC'].agg(zhong_shu)  # 菜品大类
    
    group_price = grouped['CMDJ'].agg(np.mean)  # 单价
    group_zkzt = grouped['ZKZT'].agg(zhong_shu)  # ZKZT字段
    group_zkl = grouped['ZKL'].agg(np.mean)  # 折扣率
    
    # 创建一个空的 DataFrame
    df_dish_value = pd.DataFrame(columns=['STAT_DATE',	'STORE_NAME',	'XMID','XMBH',	
                                          'XMMC',	'DWBH',	'CMSL',	'CMDJ',	
                                          'LBMC', 'ZKZT', 'ZKL'])
    df_dish_value['STAT_DATE'] = group_date
    df_dish_value['STORE_NAME'] = group_store_name
    df_dish_value['XMID'] = np.rint(group_dish_id)
    df_dish_value['XMBH'] = np.rint(group_dish_xmbh)
    df_dish_value['XMMC'] = group_dish_name
    df_dish_value['DWBH'] = group_dish_unit
    df_dish_value['CMSL'] = group_cmsl
    df_dish_value['CMDJ'] = group_price
    df_dish_value['LBMC'] = group_dish_kind
    df_dish_value['ZKZT'] = group_zkzt
    df_dish_value['ZKL'] = group_zkl
    
    df_dish_value.to_csv('.//' + 'data_bj12_dish_82_1' + '.csv', index=False, encoding='gbk')   
    
    print()
    
    
'''
再次合并北京十二店的数据，对 XMID 和  XMBH 字段进行处理
'''
def combine_bj12_by_date_dish_name_2():
    path_dish_1516 = './/' + 'data_bj12_dish_82_2' + '.csv'
    file_dish_1516 = open(path_dish_1516)
    df_dish_1516 = pd.read_csv(file_dish_1516)
    
    xmid_list = []
    xmid_z_list = []
    xmid_all_list = []  #菜品编码
    
    xmbh_list = []
    xmbh_z_list = []
    xmbh_all_list = []  #菜品编码 XMBH
    
    for i in range(82):
        
        xmid_list.clear()
        xmid_z_list.clear()
        
        xmbh_list.clear()
        xmbh_z_list.clear()
        
        for j in range(845):
            xmid_list.append(df_dish_1516['XMID'][j + i*845])
            xmbh_list.append(df_dish_1516['XMBH'][j + i*845])
        xmid_z = zhong_shu(xmid_list)
        xmid_z_list = add_same_element(xmid_z)
        xmid_all_list.extend(xmid_z_list)
        
        xmbh_z = zhong_shu(xmbh_list)
        xmbh_z_list = add_same_element(xmbh_z)
        xmbh_all_list.extend(xmbh_z_list)
        
    # 单价
    for i in range(len(df_dish_1516)):
        cha = np.abs(df_dish_1516['CMDJ'][i] - int(df_dish_1516['CMDJ'][i]))
        if(cha != 0):
            if(i+3<=len(df_dish_1516)-1):
                df_dish_1516['CMDJ'][i] = np.ceil((df_dish_1516['CMDJ'][i+1] + df_dish_1516['CMDJ'][i+2] + df_dish_1516['CMDJ'][i+3])/3)
    
    # 创建一个空的 DataFrame
    df_dish_value = pd.DataFrame(columns=['STAT_DATE','STORE_NAME',	'XMID','XMBH',	
                                          'XMMC',	'DWBH',	'CMSL',	'CMDJ',	
                                          'LBMC', 'ZKZT', 'ZKL'])
    
    df_dish_value['STAT_DATE'] = df_dish_1516['STAT_DATE']
    df_dish_value['STORE_NAME'] = df_dish_1516['STORE_NAME']
    
    df_dish_value['XMID'] = xmid_all_list
    
    df_dish_value['XMBH'] = xmbh_all_list
    
    df_dish_value['XMMC'] = df_dish_1516['XMMC']
    df_dish_value['DWBH'] = df_dish_1516['DWBH']
    df_dish_value['CMSL'] = df_dish_1516['CMSL']
    df_dish_value['CMDJ'] = df_dish_1516['CMDJ']
    df_dish_value['LBMC'] = df_dish_1516['LBMC']
    df_dish_value['ZKZT'] = df_dish_1516['ZKZT']
    df_dish_value['ZKL'] = np.rint(df_dish_1516['ZKL'])
    
    df_dish_value.to_csv('.//' + 'data_bj12_dish_82_3' + '.csv', index=False, encoding='gbk')   
    
    print()    


### 扩充相同元素
def add_same_element(element):
    element_list = []
    for i in range(845):
        element_list.append(element)
    return element_list


### 求一个序列中 出现次数最多的 元素
from collections import Counter
def zhong_shu(data_list):
    data_list = list(data_list)
    ele_counts = Counter(data_list)
    # 出现频率最高的 1 个元素
    top_one = ele_counts.most_common(1)
    
    return top_one[0][0]



'''
合并聚合后的df
'''
df_dish_1516_tmp = pd.DataFrame()
df_dish_1617_tmp = pd.DataFrame()
def combine_group(num):
    # 合并1516
    '''path_dish_1516 = './/' + 'dishdetail14d_1516_gruoupby' + '_' + str(num) + '.csv'
    file_dish_1516 = open(path_dish_1516)
    df_dish_1516 = pd.read_csv(file_dish_1516, index_col=0)
    global df_dish_1516_tmp
    df_dish_1516_tmp = pd.concat([df_dish_1516_tmp, df_dish_1516], axis=0)'''

    # 合并1617
    path_dish_1617 = './/' + 'dishdetail14d_1617_gruoupby' + '_' + str(num) + '.csv'
    file_dish_1617 = open(path_dish_1617)
    df_dish_1617 = pd.read_csv(file_dish_1617, index_col=0)
    global df_dish_1617_tmp
    df_dish_1617_tmp = pd.concat([df_dish_1617_tmp, df_dish_1617], axis=0)
    
    
'''
合并十四店2015~2016 和 2016~2017期间的销售数据
'''
def combine_data():
    # 20150501~20160531期间
    path_dish_1516 = './/' + 'dishdetail1516_groupby_all' + '.csv'
    file_dish_1516 = open(path_dish_1516)
    df_dish_1516 = pd.read_csv(file_dish_1516, index_col=0)
    # 20160601~20170828期间
    path_dish_1617 = './/' + 'dishdetail1617_groupby_all' + '.csv'
    file_dish_1617 = open(path_dish_1617)
    df_dish_1617 = pd.read_csv(file_dish_1617, index_col=0)
    # 合并
    df_dish_151617 = pd.concat([df_dish_1516, df_dish_1617], axis=0, sort=False)
    df_dish_151617.to_csv('.//' + 'data' + '.csv', encoding='gbk')
    print ()


if __name__ == '__main__':
    time_begin = time.time()
    
    
    # 合并14家店销量等其他原始字段1516
    '''for i in range(1, 5):
        i = 3
        combine_sales_by_date(i)
        break'''
#    combine_data()
    # 合并14家店销量等其他原始字段1617
#    for i in range(1, 8):
#        combine_sales_by_date_1617(i)
    '''for i in range(1, 5):
        combine_group(i)
    df_dish_1516_tmp.to_csv('.//' + 'dishdetail1516_groupby_all' + '.csv', encoding='gbk')'''
    
    '''for i in range(1, 8):
        combine_group(i)
    df_dish_1617_tmp.to_csv('.//' + 'dishdetail1617_groupby_all' + '.csv', encoding='gbk')'''
#    combine_bj12_by_date_dish_name()
    
    combine_bj12_by_date_dish_name_2()
    
    time_end = time.time()
    print ("总共耗费了：%d  秒."%(time_end - time_begin))