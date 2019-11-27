#! /usr/bin/python3
# -*- coding: utf-8 -*-

# https://github.com/iamseancheney/python_for_data_analysis_2nd_chinese_version/blob/master/%E7%AC%AC05%E7%AB%A0%20pandas%E5%85%A5%E9%97%A8.md
import numpy as np
import pandas as pd

obj = pd.Series([4, 7, -5, 3])
obj.values
obj.index
obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
obj2
obj2['a']
obj2['d'] = 6
obj2[obj2 > 0]
obj2 * 2
obj2
np.exp(obj2)

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(sdata)
obj3
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = pd.Series(sdata, index=states)
obj4

# 数据缺失判断
pd.isnull(obj4)  # 函数
pd.notnull(obj4)
obj4.isnull()  # 实例方法
obj3

obj4
# 数据对齐
obj3 + obj4
# pd属性
obj4.name = 'population'
obj4.index.name = 'state'

# DataFrame
data = {
    'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
    'year': [2000, 2001, 2002, 2001, 2002, 2003],
    'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]
}
frame = pd.DataFrame(data)
frame.head()
# 如果指定了列序列，则DataFrame的列就会按照指定顺序进行排列
pd.DataFrame(data, columns=['year', 'state', 'pop'])

# 如果传入的列在数据中找不到，就会在结果中产生缺失值
frame2 = pd.DataFrame(data,
                      columns=['year', 'state', 'pop', 'debt'],
                      index=['one', 'two', 'three', 'four', 'five', 'six'])

frame2.columns

# 通过类似字典标记的方式或属性的方式，可以将DataFrame的列获取为一个Series
frame2['state']
frame2.year
frame2.loc['three']
frame2['debt'] = 16.5
frame2