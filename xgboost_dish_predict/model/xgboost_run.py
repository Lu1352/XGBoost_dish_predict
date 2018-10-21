# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 17:04:56 2018

@author: shi.chao
"""
import time
import pandas as pd


import pandas as pd
import os
import time
import operator
import shutil
import numpy as np
import xgboost as xgb
from sklearn.preprocessing import StandardScaler
from sklearn.base import TransformerMixin
from sklearn import cross_validation
from matplotlib import pylab as plt
from matplotlib.dates import DayLocator,DateFormatter
import seaborn as sns
from sklearn.linear_model import LinearRegression



# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei'] 
# 用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False


goal = 'CMSL_outlier'
#goal = 'CMSL'

#定义一些变换和评判标准
'''
使用不同的loss function的时候要特别注意这个
'''
def ToWeight(y):
    w = np.zeros(y.shape, dtype=float)
    ind = y != 0
    w[ind] = 1. / (y[ind]**2)
    return w

def rmspe(yhat, y):
    w = ToWeight(y)
    rmspe = np.sqrt(np.mean(w * (y - yhat)**2))
    return rmspe

def rmspe_xg(yhat, y):
    # y是log平滑后的结果
    y = y.get_label()
    y = np.exp(y) - 1
    yhat = np.exp(yhat) - 1
    w = ToWeight(y)
    rmspe = np.sqrt(np.mean(w * (y - yhat)**2))

    return 'rmspe', rmspe


# 加载数据，设定数值型和非数值型数据
def load_data(data):
    # 'same_week1', 'same_week2', 'same_week3', 'same_week4',
    '''features = ['XMID', 'XMBH', 'XMMC_NUM','DWBH_NUM', 'CMDJ', 'LBMC_NUM', 'ZKZT_NUM', 'ZKL', 'holiday',
       'day_of_week', 'year', 'month', 'day', 'weather', 'ssd', 'season',
       'same_week1_sales_percent',
       'same_week_line_regression']'''
    features = ['XMID', 'XMBH', 'XMMC_NUM','DWBH_NUM', 'CMDJ', 'LBMC_NUM', 'ZKZT_NUM', 'ZKL',
       'year', 'day', 'ssd', 
       'same_week1_sales_percent',
       'same_week_line_regression',
       'Week_0','Week_1','Week_2','Week_3','Week_4','Week_5','Week_6',
       'Month_1','Month_2','Month_3','Month_4','Month_5','Month_6','Month_7','Month_8','Month_9','Month_10','Month_11','Month_12',
       'Weather_1','Weather_2','Weather_3','Weather_4','Weather_5','Weather_6',
       'Holiday_0','Holiday_1','Holiday_2',
       'Season_1','Season_2','Season_3','Season_4',
       'date']
    
    train_1 = data[data['STAT_DATE']>='2015-06-10'] 
    data_bj_dish_name_train = train_1[train_1['STAT_DATE']<='2017-08-14']
#    data_bj_dish_name_train.set_index('STAT_DATE', inplace=True)
    data_train = data_bj_dish_name_train
#    data_bj_dish_name_train.to_csv('.//' + 'data_feature_train' + '.csv', encoding='gbk')
    
    test_1 = data[data['STAT_DATE']>='2017-08-15'] 
    data_bj_dish_name_test = test_1[test_1['STAT_DATE']<='2017-08-19']
#    data_bj_dish_name_test.set_index('STAT_DATE', inplace=True)
#    data_bj_dish_name_test.to_csv('.//' + 'data_feature_test' + '.csv', encoding='gbk')
    
    data_test = data_bj_dish_name_test
   

    return (data_train,data_test,features)
    

    

# 训练与分析
def XGB_native(train, test, features):
    # TODO 格点搜索
    '''depth = 13
    eta = 0.01
    ntrees = 8000
    mcw = 3'''
    depth = 18
    eta = 0.01
    ntrees = 1000000
    mcw = 3
    params = {
        'objective': 'reg:linear',
        'booster': 'gbtree',
        'eta': eta,
        'max_depth': depth,
        'min_child_weight': mcw,
        'subsample': 1,
        'colsample_bytree': 1,
        'silent': 1,
        'scale_pos_weight':1
    }
    ''''ntrees = 100
    params = {
        'objective': 'reg:linear',
        'booster': 'gbtree',
        'eta': 0.13,
        'max_depth': 3,
        'min_child_weight': 2,
        'seed':0,
        'subsample': 0.7,
        'colsample_bytree': 0.6,
        'gamma':0.5,
        'alpha':50,
        'lambda':0,
        'silent': 1
    }'''
    print('Running with params: ' + str(params))
    print('Running with ntrees: ' + str(ntrees))
    print('Running with features: ' + str(features))

    # train model with local split  tsize=0.05  0.008
    tsize = 0.03
    X_train, X_test = cross_validation.train_test_split(train, test_size=tsize)
    dtrain = xgb.DMatrix(X_train[features], np.log(X_train[goal] + 1))
    dvaild = xgb.DMatrix(X_test[features], np.log(X_test[goal] + 1))
   
    watchlist = [(dvaild, 'eval'), (dtrain, 'train')]
    gbm = xgb.train(params, dtrain, ntrees, watchlist, early_stopping_rounds=100,
                    feval=rmspe_xg, verbose_eval=True)
    # eval 放评价数据,可观察
    train_probs = gbm.predict(xgb.DMatrix(X_test[features]))
    indices = train_probs < 0
    #TODO 看下这个数据结构
    train_probs[indices] = 0
    error = rmspe(np.exp(train_probs) - 1, X_test[goal].values)
    print(error)

    # predict and export
    test_probs = gbm.predict(xgb.DMatrix(test[features]))
    indices = test_probs < 0
    test_probs[indices] = 0

    y_pre = np.exp(test_probs) - 1
    y_pre = np.rint(y_pre) # 预测值四舍五入
    '''for i in y_pre:
        print (i)'''
    
    test = test.reset_index(drop=True)
    
    df_result = pd.DataFrame()
    df_result['日期'] = test['STAT_DATE']
    df_result['菜品名称'] = test['XMMC']
    df_result['销量真实值'] = np.rint(test[goal])
    df_result['销量预测值'] = y_pre
    
    test_truth_y = np.rint(test[goal])
    absolute_err_list = []
    relative_err_list = []
    accuracy_list = []
    for i in range(len(test)):
        absolute_err =  y_pre[i] - test_truth_y[i]  # 绝对误差
        relative_err1 = absolute_err / test_truth_y[i]   
        relative_err = "%.2f%%" % (relative_err1 * 100) # 相对误差
        accuracy1 = 1 - np.abs(relative_err1)   
        accuracy = "%.2f%%" % (accuracy1 * 100) #准确率
        
        absolute_err_list.append(absolute_err)
        relative_err_list.append(relative_err)
        accuracy_list.append(accuracy)
    
    df_result['绝对误差'] = absolute_err_list
    df_result['相对误差'] = relative_err_list
    df_result['准确率'] = accuracy_list
#    df_result['绝对误差绝对值'] = np.abs(absolute_err_list)
#    df_result['绝对值之和'] = np.sum(np.abs(absolute_err_list))
    absolute_err_mean = np.sum(np.abs(absolute_err_list))/82/5
    df_result['平均绝对误差'] = absolute_err_mean
    for i in range(1, len(test)):
        df_result['平均绝对误差'][i] = ''
    
    result_name = 'result_30_' + str(int(absolute_err_mean*1000))
    
    df_result.to_csv('.//result//' + result_name + '.csv', encoding='gbk', index=False)
    # 保存模型
    save_model(gbm, absolute_err_mean)
    # 保存特征重要性图
    save_feature_importance(gbm, absolute_err_mean)



# 保存模型
def save_model(gbm, absolute_err_mean):
    path_name = './/result_model//' 
    absolute_err_mean = str(int(absolute_err_mean*1000))
    path_save_model = path_name + absolute_err_mean + ".model"
    if(os.path.isfile(path_save_model)):
        os.remove(path_save_model)
    gbm.save_model(path_name + absolute_err_mean + '.model')

# 保存特征重要性图
def save_feature_importance(gbm, absolute_err_mean):
    # feature importance
    #这里要先写xgb.map然后把编码改一下再读画图
    path_name = './/result_feature_importance//' 
    absolute_err_mean = str(int(absolute_err_mean*1000))
    path_save_feature_importance = path_name + absolute_err_mean + ".fmap"
    outfile = open(path_save_feature_importance, 'w')
    for i, feat in enumerate(features):
        outfile.write('{0}\t{1}\tq\n'.format(i, feat))
    outfile.close()
    importance = gbm.get_fscore(fmap=path_save_feature_importance)
    importance = sorted(importance.items(), key=operator.itemgetter(1))
    df = pd.DataFrame(importance, columns=['feature', 'fscore'])
    df['fscore'] = df['fscore'] / df['fscore'].sum()
    featp = df.plot(kind='barh', x='feature', y='fscore', legend=False, figsize=(16, 20))
    plt.title('Feature Importance')
    plt.xlabel('relative importance')
    fig_featp = featp.get_figure()
    path_feature = path_name + 'Feature_Importance_xgb_' + absolute_err_mean + '.png' 
    if (os.path.exists(path_feature)):
        os.remove(path_feature)
    fig_featp.savefig(path_feature)


# 选出 73 种菜品和平均绝对误差指标
def select_dish_73(result_name):
    path_select = './/result//' + result_name 
    path_name = '.csv'
    file_select = open(path_select + path_name)
    df_select = pd.read_csv(file_select)
    df_select = df_select.reset_index(drop=True)
    dish_73_list = ['(B)贝柱滑(半)', '(B)笋片(半)', '木耳', '大白菜', '(B)红薯粉带(半)', '宽苕粉', '西式牛肉滑', '(B)红薯(半)', '红薯', '青笋', '(B)白萝卜(半)', '(B)捞派麻辣滑牛(半)', '牛栏山二锅头42度500ml（白瓶）', '五常米饭', '娃娃菜', '娃娃菜(半)', '菠菜', '捞派麻辣滑牛', '澳洲肥牛(和牛)', '腐竹', '血旺', '油豆皮', '(B)包心生菜(半)', '(B)冻豆腐(半)', '(B)香菇(半)', '(B)魔芋丝(半)', '1.25L可口可乐', '(B)腐竹(半)', '(B)水晶粉丝(半)', '(B)血旺(半)', '茼蒿', '豆腐', '(B)精品肥牛(半)', '鹌鹑蛋(半)', '水晶粉丝', '(B)蟹味棒(半)', '(B)冻虾(半)', '包心生菜', '笋片', '(B)捞派豆花(半)', '鹌鹑蛋', '鸭舌', '宽苕粉(半)', '(B)海带(半)', '(B)金针菇(半)', '山药', '(B)鸭舌(半)', '精品肥牛', '自选调料(无)', '(B)豆腐皮(半)', '红薯粉带', '蟹味棒', '(B)大白菜(半)', '澳洲肥牛(和牛)(半)', '(B)西式牛肉滑(半)', '(B)山药(半)', '冻豆腐', '(B)豆腐(半)', '蒿子秆', '金银馒头', '(B)蒿子秆(半)', '(B)油豆皮(半)', '海带', '(B)冬瓜(半)', '白萝卜', '豆腐皮', '黄糖糍粑', '(B)菠菜(半)', '金针菇', '(B)青笋(半)', '长寿面', '(B)木耳(半)', '(B)竹笋(半)']
    df_select_73 = pd.DataFrame()
    for dish in dish_73_list:
        df_select_73_1 = pd.DataFrame()
        df_select_73_1 = df_select[df_select['菜品名称']==dish]
        df_select_73 = pd.concat([df_select_73, df_select_73_1], axis=0)
    df_select_73 = df_select_73.reset_index(drop=True)
    absolute_err_list = df_select_73['绝对误差']
    absolute_err_mean = np.sum(np.abs(absolute_err_list))/len(dish_73_list)/5
    df_select_73['平均绝对误差'] = absolute_err_mean
    for i in range(1, len(df_select_73)):
        df_select_73['平均绝对误差'][i] = ''
    df_select_73.to_csv(path_select + '_73' + path_name, encoding='gbk', index=False)  
    print ()
    
    


if __name__ == '__main__':
    # 计算耗时
    time_begin = time.time()
    
    path = "..//outlier_feature//" + "data_feature_12" + ".csv"
    train_f = open(path)
    data = pd.read_csv(train_f, low_memory=False, parse_dates=['STAT_DATE'])
    
    print('=>载入数据中...')
    train, test, features = load_data(data)
    
    print ('=>加载模型中...')
    XGB_native(train, test, features)   
    
#    select_dish_73('result_30_7904')
    
    time_end = time.time()
    print ("总共耗费了：%d  秒."%(time_end - time_begin))