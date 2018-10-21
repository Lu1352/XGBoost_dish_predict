# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 14:57:47 2018

@author: shi.chao
"""

import urllib.request
import re
import pandas as pd
import time


df_weather = pd.DataFrame()
date_list = []
max_tem_list = []
min_tem_list = []
weather_list = []
wind_list = []
wind_level_list = []
air_list = []
air_kind_list = []
air_level_list = []

#year_num = [y_n for y_n in range(2016, 2018)]
#month_num = [m_n for m_n in range(3, 13)]
# ['3','4','5','6','7','8','9','10','11','12']
# 爬虫获取天气
def crawler():
    year_2015_5_12 = [2015]
    month_2015_5_12 = ['5','6','7','8','9','10','11','12']
    
    year_2016_1_2 = [2016]
    month_2016_1_2 = ['1','2']
    
    year_2016_3_12 = [2016]
    month_2016_3_12 = ['03','04','05','06','07','08','09','10','11','12']
    
    year_2017_1_8 = [2017]
    month_2017_1_8 = ['01','02','03','04','05','06','07','08']
    '''for i in month_num:
        if(i/10.0<1):
             month_num[i-2-1] = str(i).zfill(2)'''
    
    for year_n in year_2017_1_8:
    #    year_n = 2015
        for month_n in month_2017_1_8:
            year_month = str(year_n) + str(month_n)
            city = '54511'  # 北京的代码
    #        year_month = '201608'
            # http://tianqi.2345.com/t/wea_history/js/201609/54511_201609.js
            request=urllib.request.Request("http://tianqi.2345.com/t/wea_history/js/{m}/{c}_{m}.js".format(m=year_month,c=city))
            # http://tianqi.2345.com/t/wea_history/js/54511_20162.js
    #        request=urllib.request.Request("http://tianqi.2345.com/t/wea_history/js/{c}_{m}.js".format(m=year_month,c=city))
            
            request.add_header("Referer","http://tianqi.2345.com/wea_history/{c}.htm".format(c=city))
            response=urllib.request.urlopen(request)
            html=response.read().decode("gbk")
            content=str.split(html,"=")[1].split("]")[0].split("tqInfo:[")[1]
            re_object=re.findall("{.*?}",content)
    
            for item in re_object:
                item = re.findall(r"'(.+?)'", item)
                if len(item)>=1:
                    date_list.append(item[0])
                    max_tem_list.append(item[1])
                    min_tem_list.append(item[2])
                    weather_list.append(item[3])
                    wind_list.append(item[4])
                    wind_level_list.append(item[5])
                    '''air_list.append(item[6])
                    air_kind_list.append(item[7])
                    air_level_list.append(item[8])'''
    #    break
    
    df_weather['date'] = date_list
    df_weather['date'] = pd.to_datetime(df_weather['date'], format='%Y-%m-%d')
    df_weather['max_tem'] = max_tem_list
    df_weather['min_tem'] = min_tem_list
    df_weather['weather'] = weather_list
    df_weather['wind'] = wind_list
    df_weather['wind_level'] = wind_level_list
    '''df_weather['air'] = air_list
    df_weather['air_kind'] = air_kind_list
    df_weather['air_level'] = air_level_list'''
            
    df_weather.to_csv('.//weather//' + 'weather_2017_1_8' + '.csv', index=False, encoding='gbk')              
    print (df_weather) 

# 合并天气
def concat_weather():
    path_2015_5_12 = './/weather//' + 'weather_2015_5_12' + '.csv'
    file_2015_5_12 = open(path_2015_5_12)
    df_2015_5_12 = pd.read_csv(file_2015_5_12)
             
    path_2016_1_2 = './/weather//' + 'weather_2016_1_2' + '.csv'
    file_2016_1_2 = open(path_2016_1_2)
    df_2016_1_2 = pd.read_csv(file_2016_1_2)     
             
    path_2016_3_12 = './/weather//' + 'weather_2016_3_12' + '.csv'
    file_2016_3_12 = open(path_2016_3_12)
    df_2016_3_12 = pd.read_csv(file_2016_3_12)    
    
    path_2017_1_8 = './/weather//' + 'weather_2017_1_8' + '.csv'
    file_2017_1_8 = open(path_2017_1_8)
    df_2017_1_8 = pd.read_csv(file_2017_1_8)    
    
    df_weather_all_no_fog = pd.concat([df_2015_5_12,df_2016_1_2,df_2016_3_12,df_2017_1_8], axis=0)
#    df_weather_all_no_fog.to_csv('.//weather//' + 'weather_all_no_fog' + '.csv', index=False, encoding='gbk')
                   
    print (df_weather_all_no_fog)
#    df_weather_all_no_fog['wind_level'].nunique()
    

# 计算体感指数 和  天气类型  
def cal_ssd():
    path_2017_1_8 = './/weather//' + 'weather_all_no_fog' + '.csv'
    file_2017_1_8 = open(path_2017_1_8)
    df_weather_all_no_fog = pd.read_csv(file_2017_1_8)   
    
    df_weather_ssd = pd.DataFrame()
    df_weather_ssd['date'] = df_weather_all_no_fog['date']
    wind_level_list = []
    max_tem_list = []
    
    
    df_weather_all_no_fog['wind_level'] = df_weather_all_no_fog['wind_level'].astype(str)
    for i in range(len(df_weather_all_no_fog['wind_level'])):
        wind_1 = df_weather_all_no_fog['wind_level'][i]
        if(wind_1.find('-')>=0):
            wind_2 = wind_1.split('-')[1]
            wind_level_list.extend(max(re.findall("\d+",wind_2)))
        else:
            wind_level_list.extend('1')
        # 获取最高温度数值
        max_tem_list.extend(re.findall("\d+",df_weather_all_no_fog['max_tem'][i]))
            
     # 获取风力大小字段数字       
    df_weather_ssd['wind_level'] = wind_level_list    
    df_weather_ssd['max_tem'] = max_tem_list
    
    df_weather_ssd['max_tem'] = df_weather_ssd['max_tem'].astype(float)
    df_weather_ssd['wind_level'] = df_weather_ssd['wind_level'].astype(float)
    
    # 计算体感指数字段
    ssd_list = []
    for i in range(len(df_weather_ssd['wind_level'])):
        ssd = (1.818*df_weather_ssd['max_tem'][i] + 18.18)*0.88 + (df_weather_ssd['max_tem'][i]-32)/(45-df_weather_ssd['max_tem'][i]) - 3.2*df_weather_ssd['wind_level'][i] + 18.2
        ssd_list.append(ssd)
    df_weather_ssd['ssd'] = ssd_list
    # 获取 天气类型 数值（共 6 类）
    df_weather_ssd['weather'] = df_weather_all_no_fog['weather'] 
    df_weather_ssd['weather'] = df_weather_ssd['weather'].astype(str)
    for i in range(len(df_weather_ssd['weather'])):
        if(df_weather_ssd['weather'][i]=='晴~阵雨'):
            df_weather_ssd['weather'][i] = '3'
        if(df_weather_ssd['weather'][i]== '雷阵雨~大到暴雨'):
            df_weather_ssd['weather'][i] = '6'
        if(df_weather_ssd['weather'][i]== '中雨~小到中雨'):
            df_weather_ssd['weather'][i] = '4'
        if(df_weather_ssd['weather'][i]== '阴~雷阵雨'):
            df_weather_ssd['weather'][i] = '3'
        
        if(df_weather_ssd['weather'][i]== '阵雨~阴'):
            df_weather_ssd['weather'][i] = '3'
        if(df_weather_ssd['weather'][i]== '雨夹雪~大雪'):
            df_weather_ssd['weather'][i] = '5'
        if(df_weather_ssd['weather'][i]== '中到大雨~阴'):
            df_weather_ssd['weather'][i] = '4'
            
        if(df_weather_ssd['weather'][i]== '霾~雷阵雨'):
            df_weather_ssd['weather'][i] = '3'
        if(df_weather_ssd['weather'][i]== '小雨~小到中雨'):
            df_weather_ssd['weather'][i] = '4'
        if(df_weather_ssd['weather'][i]== '阵雨~晴'):
            df_weather_ssd['weather'][i] = '2'
            
        if(df_weather_ssd['weather'][i] == '小雪~多云'):
            df_weather_ssd['weather'][i] = '2'
        if(df_weather_ssd['weather'][i] == '小雨~多云'):
            df_weather_ssd['weather'][i] = '2'
        if(df_weather_ssd['weather'][i] == '阴~小到中雨'):
            df_weather_ssd['weather'][i] = '3'
            
        if(df_weather_ssd['weather'][i] == '多云~晴'):
            df_weather_ssd['weather'][i] = '1'
        if(df_weather_ssd['weather'][i] == '雾~小雨'):
            df_weather_ssd['weather'][i] = '3'
        if(df_weather_ssd['weather'][i] == '阵雨~雷雨'):
            df_weather_ssd['weather'][i] = '3'
        
        if(df_weather_ssd['weather'][i] == '中雨~阵雨'):
            df_weather_ssd['weather'][i] = '3'
        if(df_weather_ssd['weather'][i] == '小雪'):
            df_weather_ssd['weather'][i] = '3'
        if(df_weather_ssd['weather'][i] == '霾~阴'):
            df_weather_ssd['weather'][i] = '2'
        
        if(df_weather_ssd['weather'][i] == '多云~雷雨'):
            df_weather_ssd['weather'][i] = '3'
        if(df_weather_ssd['weather'][i] == '雷阵雨~阴'):
            df_weather_ssd['weather'][i] = '3'
        if(df_weather_ssd['weather'][i] == '小雪~晴'):
            df_weather_ssd['weather'][i] = '2'
            
        if(df_weather_ssd['weather'][i] == '大雨'):
            df_weather_ssd['weather'][i] = '5'
        if(df_weather_ssd['weather'][i] == '扬沙~晴'):
            df_weather_ssd['weather'][i] = '3'
        if(df_weather_ssd['weather'][i] == '雷阵雨~晴'):
            df_weather_ssd['weather'][i] = '3'
        
        if(df_weather_ssd['weather'][i]=='小到中雨~阴'):
            df_weather_ssd['weather'][i] = '3'
        if(df_weather_ssd['weather'][i]==  '阴~多云'):
            df_weather_ssd['weather'][i] = '2'
        if(df_weather_ssd['weather'][i]== '雨夹雪'):
            df_weather_ssd['weather'][i] = '4'
        if(df_weather_ssd['weather'][i]== '多云~小雪'):
            df_weather_ssd['weather'][i] = '3'
            
        if(df_weather_ssd['weather'][i]=='小雨'):
            df_weather_ssd['weather'][i] = '3'
        if(df_weather_ssd['weather'][i]==  '雷雨~晴'):
            df_weather_ssd['weather'][i] = '2'
        if(df_weather_ssd['weather'][i]== '霾~小雨'):
            df_weather_ssd['weather'][i] = '3'
        if(df_weather_ssd['weather'][i]==  '雷阵雨~多云'):
            df_weather_ssd['weather'][i] = '2'
        if(df_weather_ssd['weather'][i]==  '小到中雨~小雨'):
            df_weather_ssd['weather'][i] = '3'
        if(df_weather_ssd['weather'][i]==  '小到中雨'):
            df_weather_ssd['weather'][i] = '4'
            
        if(df_weather_ssd['weather'][i]=='霾~多云'):
            df_weather_ssd['weather'][i] = '2'
        if(df_weather_ssd['weather'][i]== '阵雨~小雨'):
            df_weather_ssd['weather'][i] = '3'
        if(df_weather_ssd['weather'][i]== '阴~小雨'):
            df_weather_ssd['weather'][i] = '3'
        if(df_weather_ssd['weather'][i]== '小雪~阴'):
            df_weather_ssd['weather'][i] = '2'
        if(df_weather_ssd['weather'][i]== '雷阵雨'):
            df_weather_ssd['weather'][i] = '3'
        if(df_weather_ssd['weather'][i]== '小雨~晴'):
            df_weather_ssd['weather'][i] = '1'
            
        if(df_weather_ssd['weather'][i]=='晴~阴'):
            df_weather_ssd['weather'][i] = '2'
        if(df_weather_ssd['weather'][i]== '霾~雾'):
            df_weather_ssd['weather'][i] = '2'
        if(df_weather_ssd['weather'][i]== '小雨~阴'):
            df_weather_ssd['weather'][i] = '2'
        if(df_weather_ssd['weather'][i]== '雷雨'):
            df_weather_ssd['weather'][i] = '3'
        if(df_weather_ssd['weather'][i]== '霾'):
            df_weather_ssd['weather'][i] = '2'
        if(df_weather_ssd['weather'][i]== '阵雨~多云'):
            df_weather_ssd['weather'][i] = '2'
        if(df_weather_ssd['weather'][i]== '多云~雷阵雨'):
            df_weather_ssd['weather'][i] = '3'
        
        if(df_weather_ssd['weather'][i]==  '小到中雨~中到大雨'):
            df_weather_ssd['weather'][i] = '4'
        if(df_weather_ssd['weather'][i]== '阵雨'):
            df_weather_ssd['weather'][i] = '3'
        if(df_weather_ssd['weather'][i]== '霾~小雪'):
            df_weather_ssd['weather'][i] = '3'
        if(df_weather_ssd['weather'][i]== '多云~小雨'):
            df_weather_ssd['weather'][i] = '3'
        if(df_weather_ssd['weather'][i]== '阴~雨夹雪'):
            df_weather_ssd['weather'][i] = '3'
            
        if(df_weather_ssd['weather'][i]==  '小到中雨~中到大雨'):
            df_weather_ssd['weather'][i] = '4'
        if(df_weather_ssd['weather'][i]== '阵雨'):
            df_weather_ssd['weather'][i] = '3'
        if(df_weather_ssd['weather'][i]== '霾~小雪'):
            df_weather_ssd['weather'][i] = '3'
        if(df_weather_ssd['weather'][i]== '多云~小雨'):
            df_weather_ssd['weather'][i] = '3'
        if(df_weather_ssd['weather'][i]== '阴~雨夹雪'):
            df_weather_ssd['weather'][i] = '3'    
        
        if(df_weather_ssd['weather'][i]=='雷阵雨~阵雨'):
            df_weather_ssd['weather'][i] = '3'
        if(df_weather_ssd['weather'][i]=='小雨~雨夹雪'):
            df_weather_ssd['weather'][i] = '3'
        if(df_weather_ssd['weather'][i]== '多云~阴'):
            df_weather_ssd['weather'][i] = '2'
        if(df_weather_ssd['weather'][i]==  '阴~阵雨'):
            df_weather_ssd['weather'][i] = '3'
        if(df_weather_ssd['weather'][i]== '小雨~阵雨'):
            df_weather_ssd['weather'][i] = '3'    
        
        if(df_weather_ssd['weather'][i]=='大雪~小雪'):
            df_weather_ssd['weather'][i] = '3'
        if(df_weather_ssd['weather'][i]=='雷阵雨~中雨'):
            df_weather_ssd['weather'][i] = '4'
        if(df_weather_ssd['weather'][i]== '雷阵雨~大雨'):
            df_weather_ssd['weather'][i] = '5'
        if(df_weather_ssd['weather'][i]== '阴~小雪'):
            df_weather_ssd['weather'][i] = '3'
        if(df_weather_ssd['weather'][i]=='雷雨~多云'):
            df_weather_ssd['weather'][i] = '2' 
        
        if(df_weather_ssd['weather'][i]== '暴雨~小到中雨'):
            df_weather_ssd['weather'][i] = '4'
        if(df_weather_ssd['weather'][i]=='霾~雨夹雪'):
            df_weather_ssd['weather'][i] = '3'
        if(df_weather_ssd['weather'][i]== '多云~霾'):
            df_weather_ssd['weather'][i] = '3'
        if(df_weather_ssd['weather'][i]== '多云'):
            df_weather_ssd['weather'][i] = '2'
        if(df_weather_ssd['weather'][i]=='雨夹雪~中雪'):
            df_weather_ssd['weather'][i] = '4' 
        
        if(df_weather_ssd['weather'][i]== '雷阵雨~小到中雨'):
            df_weather_ssd['weather'][i] = '3'
        if(df_weather_ssd['weather'][i]=='大雨~阵雨'):
            df_weather_ssd['weather'][i] = '3'
        if(df_weather_ssd['weather'][i]== '雷阵雨~中到大雨'):
            df_weather_ssd['weather'][i] = '5'
        if(df_weather_ssd['weather'][i]== '多云~阵雨'):
            df_weather_ssd['weather'][i] = '3'
        if(df_weather_ssd['weather'][i]=='雨夹雪~阴'):
            df_weather_ssd['weather'][i] = '2' 
        
        if(df_weather_ssd['weather'][i]=='霾~阵雨'):
            df_weather_ssd['weather'][i] = '3'
        if(df_weather_ssd['weather'][i]==  '阵雨~中雨'):
            df_weather_ssd['weather'][i] = '4'
        if(df_weather_ssd['weather'][i]==  '晴'):
            df_weather_ssd['weather'][i] = '1'
        if(df_weather_ssd['weather'][i]== '阴~晴'):
            df_weather_ssd['weather'][i] = '1'
        if(df_weather_ssd['weather'][i]== '阵雨~小到中雨'):
            df_weather_ssd['weather'][i] = '3'
        if(df_weather_ssd['weather'][i]== '阴'):
            df_weather_ssd['weather'][i] = '2'
        if(df_weather_ssd['weather'][i]== '晴~多云'):
            df_weather_ssd['weather'][i] = '2'
            
        if(df_weather_ssd['weather'][i]=='晴~霾'):
            df_weather_ssd['weather'][i] = '3'
        if(df_weather_ssd['weather'][i]== '雾~晴'):
            df_weather_ssd['weather'][i] = '1'
        if(df_weather_ssd['weather'][i]=='小雨~小雪'):
            df_weather_ssd['weather'][i] = '3'
        if(df_weather_ssd['weather'][i]=='小雪~中雪'):
            df_weather_ssd['weather'][i] = '4'
        if(df_weather_ssd['weather'][i]=='雷雨~阴'):
            df_weather_ssd['weather'][i] = '2'
        if(df_weather_ssd['weather'][i]=='霾~晴'):
            df_weather_ssd['weather'][i] = '1'
        
    df_weather_ssd_1 = pd.DataFrame()
    df_weather_ssd_1['date'] = df_weather_ssd['date']
    df_weather_ssd_1['weather'] = df_weather_ssd['weather']    
    df_weather_ssd_1['ssd'] = df_weather_ssd['ssd']
    df_weather_ssd_1.to_csv('.//weather//' + 'weather_ssd_1' + '.csv',index=False,encoding='gbk')

# 日期和天气匹配
def date_match():
    path_date_match = './/weather//' + 'date_match' + '.csv'
    file_date_match = open(path_date_match)
    df_date_match = pd.read_csv(file_date_match)
    df_date_match['date'] = df_date_match['date'].astype(str)
    df_date_match['date'] = pd.to_datetime(df_date_match['date'], format='%Y-%m-%d')
    df_date_match = df_date_match.astype(str)

    path_weather_ssd_1 = './/weather//' + 'weather_ssd_1' + '.csv'
    file_weather_ssd_1 = open(path_weather_ssd_1)
    df_weather_ssd_1 = pd.read_csv(file_weather_ssd_1)
    df_weather_ssd_1['date'] = df_weather_ssd_1['date'].astype(str)
    df_weather_ssd_1['date'] = pd.to_datetime(df_weather_ssd_1['date'], format='%Y-%m-%d')
    df_weather_ssd_1 = df_weather_ssd_1.astype(str)
    
    df_date_mathch_ssd_1 = pd.merge(df_date_match, df_weather_ssd_1, on='date')
    df_date_mathch_ssd_1.to_csv('.//weather//' + 'date_mathch_ssd_1' + '.csv',index=False,encoding='gbk')
    
# 将一个菜的天气扩充到82种菜
def copy_weather():
    path_catogroy_num = './/' + 'catogroy_num' + '.csv'
    file_catogroy_num = open(path_catogroy_num)
    df_catogroy_num = pd.read_csv(file_catogroy_num)
    df_catogroy_num['STAT_DATE'] = df_catogroy_num['STAT_DATE'].astype(str)
    df_catogroy_num['STAT_DATE'] = pd.to_datetime(df_catogroy_num['STAT_DATE'], format='%Y-%m-%d')
    df_catogroy_num = df_catogroy_num.astype(str)
    
    path_date_mathch_ssd_1 = './/weather//' + 'date_mathch_ssd_1' + '.csv'
    file_date_mathch_ssd_1 = open(path_date_mathch_ssd_1)
    df_date_mathch_ssd_1 = pd.read_csv(file_date_mathch_ssd_1)
    df_date_mathch_ssd_1['date'] = df_date_mathch_ssd_1['date'].astype(str)
    df_date_mathch_ssd_1['date'] = pd.to_datetime(df_date_mathch_ssd_1['date'], format='%Y-%m-%d')
    df_date_mathch_ssd_1 = df_date_mathch_ssd_1.astype(str)
    
    df_weather_ssd_2 = pd.DataFrame()
    df_weather_ssd_2['STAT_DATE'] = df_catogroy_num['STAT_DATE']
    df_weather_ssd_2['XMMC'] = df_catogroy_num['XMMC']
    df_weather_ssd_2['weather'] = holiday(df_date_mathch_ssd_1['weather'])
    df_weather_ssd_2['ssd'] = holiday(df_date_mathch_ssd_1['ssd'])
    
    df_weather_ssd_2.to_csv('.//weather//' + 'weather_ssd_2' + '.csv', index=False, encoding='gbk')
    
    
    
def holiday(holiday):
    holiday = list(holiday)
    holiday_list = []
    for i in range(82):
        holiday_list.extend(holiday)
    return holiday_list   
    



if __name__ == '__main__':
    time_begin = time.time()
       
#    concat_weather()
#    cal_ssd()
#    date_match()
    copy_weather()
    
    time_end = time.time()
    print ("总共耗费了：%d  秒."%(time_end - time_begin))                      
                        
                        
                        
                        
                        
                        
                        