#! /usr/bin/python3
# -*- coding: utf-8 -*-

# https://github.com/iamseancheney/python_for_data_analysis_2nd_chinese_version/blob/master/%E7%AC%AC05%E7%AB%A0%20pandas%E5%85%A5%E9%97%A8.md
import numpy as np
import pandas as pd

# https://blog.csdn.net/qq_19528953/article/details/79348929
# https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html
#
# 5.1 pandas的数据结构介绍

# 初始化空的系列
s = pd.Series()
print(s)

# 用列表初始化系列
obj = pd.Series([4, 7, -5, 3])
obj

# 系列有两个属性：index和values
obj.index
obj.values

# 对各数据点做标记，赋值index
obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
obj2.index
obj2.values
obj2[['a', 'd']]
obj2[['a', 'd']] = [1, 2]

obj2
obj2[obj2 > 0]
obj2 * 2

data = np.array(['a', 'b', 'c', 'd'])
s = pd.Series(data, index=[100, 101, 102, 103])
print(s)
data = {'a': 0., 'b': 1., 'c': 2.}
s = pd.Series(data)
df = pd.DataFrame()
print(df)
df = [1, 2, 3, 4, 5]
print(df)
data = [['Alex', 10], ['Bob', 12], ['Clarke', 13]]

obj = pd.Series([4, 7, -5, 3])
obj.values
obj.index

obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
obj2
obj2['a']
obj2['d'] = 6
obj2
obj2[obj2 > 0]
obj2 * 2
obj2
np.exp(obj2)

# 查询索引是否在系列中
'b' in obj2
'e' in obj2

# 用字典初始化系列
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
sdata
obj3 = pd.Series(sdata)
obj3

# 用排好序的列表初始化原来的系列
# 注意：'California'对应的值为NaN，表示Not a Number
# 而原来的Utah因为没有键值对应而被除去
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = pd.Series(sdata, index=states)
obj4

# 数据缺失判断
pd.isnull(obj4)  # 函数
pd.notnull(obj4)
obj4.isnull()  # 实例方法
obj3

# 找出非空的元素
obj4[obj4.notnull().values]

obj4
# 根据运算的索引标签自动对齐数据
obj3 + obj4

# 系列属性，名字，索引名字
obj4.name = 'population'
obj4.index.name = 'state'
obj4

obj
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
obj

# DataFrame
# 用字典初始化数据框
data = {
    'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
    'year': [2000, 2001, 2002, 2001, 2002, 2003],
    'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]
}
frame = pd.DataFrame(data)
frame
frame.head()
# 如果指定了列序列，则DataFrame的列就会按照指定顺序进行排列
pd.DataFrame(data, columns=['year', 'state', 'pop'])

# 如果传入的列在数据中找不到，就会在结果中产生缺失值
frame2 = pd.DataFrame(data,
                      columns=['year', 'state', 'pop', 'debt'],
                      index=['one', 'two', 'three', 'four', 'five', 'six'])

frame2.columns
frame2

# 通过类似字典标记的方式或属性的方式，可以将DataFrame的列获取为一个Series
frame2['state']
frame2.state
frame2.year
frame2.loc['three']
frame2['debt'] = 16.5
frame2
frame2['debt'] = np.arange(6.)
frame2
val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
val
frame2['debt'] = val
frame2
frame2['eastern'] = frame2.state == 'Ohio'
frame2
# del方法，很不理解
del frame2['eastern']
frame2
frame2.columns
# 定义一个字典
pop = {
    'Nevada': {
        2001: 2.4,
        2002: 2.9
    },
    'Ohio': {
        2000: 1.5,
        2001: 1.7,
        2002: 3.6
    }
}
# 用字典初始化数据框
frame3 = pd.DataFrame(pop)
frame3
# 转置
frame3.T
# 内层字典的键会被合并、排序以形成最终的索引。如果明确指定了索引，则不会这样
pd.DataFrame(pop, index=[2001, 2002, 2003])

# list(range(3))
# list(np.arange(4))
obj = pd.Series(range(3), index=['a', 'b', 'c'])
obj
index = obj.index
# index是一个Index对象 labels对象
index
index[1:]
labels = pd.Index(np.arange(3))
labels
obj2 = pd.Series([1.5, -2.5, 0], index=labels)
obj2
obj2.index is labels

## 5.2 基本功能

# 重新索引 reindex
obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
obj
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
obj2
obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
obj3
# 插值处理
obj3.reindex(range(6), method='ffill')

# 丢弃指定轴上的项
obj = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
new_obj = obj.drop('c')
new_obj
obj.drop(['d', 'c'])
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
# 用标签序列调用drop会从行标签（axis 0）删除值
data.drop(['Colorado', 'Ohio'])
data.drop('two', axis=1)
data.drop(['two', 'four'], axis='columns')
# 修改obj本身，而不是返回新对象, inplace=True
obj.drop('c', inplace=True)
obj
# 索引、选取和过滤
obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
obj
obj['b']
obj[1]
# 利用整数作索引，不含末端
obj[1:2]
# 利用标签的切片运算与普通的Python切片运算不同，其末端是包含的
obj['b':'c']

# 用切片可以对Series的相应部分进行设置
obj['b':'c'] = 5
obj
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
data
# 通过切片或布尔型数组选取数据
data['two']
data[['three', 'one']]
data[:2]
data[data['three'] > 5]

# 通过布尔型DataFrame（比如下面这个由标量比较运算得出的）进行索引
data < 5
data[data < 5] = 0
data
# 用loc和iloc进行选取
# 对于DataFrame的行的标签索引，我引入了特殊的标签运算符loc和iloc
