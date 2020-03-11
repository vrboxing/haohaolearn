#! /usr/bin/python3

# 参考
# - https://stackabuse.com/converting-strings-to-datetime-in-python/

import numpy as np
import datetime
from dateutil.parser import parse
import dateparser
import pandas as pd
import inspect
import os

date_time_str = '2020-03-07 06:27:44'
date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
print('Date:', date_time_obj.date())
print('Date:', date_time_obj.time())
print('Date-time:', date_time_obj)
print('Date-time:', date_time_obj.hour())
s = dateparser.parse(date_time_str)

date_array = [
    '2018-06-29 08:15:27.243860', '07', 'Jun 28 2018  7:40AM',
    'Jun 28 2018 at 7:40AM', 'September 18, 2017, 22:19:55',
    'Sun, 05/12/1999, 12:30PM', 'Mon, 21 March, 2015', '2018-03-12T10:12:45Z',
    '2018-06-29 17:08:00.586525+00:00', '2018-06-29 17:08:00.586525+05:00',
    'Tuesday , 6th September, 2017 at 4:30pm'
]

for date in date_array:
    print('Parsing: ' + date)
    dt = parse(date)
    print(dt.date())
    print(dt.time())
    print(dt.tzinfo)
    print('\n')

fpath = os.path.dirname(inspect.getfile(lambda: None))
os.chdir(fpath)

columns = ['pos', 'value', 'datetime']

d = pd.read_csv('data.csv', usecols=columns, parse_dates=['datetime'])
# print(d['datetime'].

d.dtypes
d.head()

day = datetime.datetime.today()
npday = np.datetime64(day)
print(npday)
str(npday)
np.arange('2005-02', '2005-03', dtype='datetime64[D]')

# Pandas详解六之Timestamp、Period、Timedelta时间对象
# https://blog.csdn.net/weixin_38168620/article/details/79596526
now = pd.Timestamp.now()
now
now_day.start_time
now_day.end_time

now_day = pd.Period.now(freq="D")
now_day
now_day.start_time
now_day.end_time

now_hour = pd.Period.now(freq="H")
now_hour.start_time
now_hour.end_time

td = pd.Timedelta(weeks=2, days=10, hours=12, minutes=2.4, seconds=10.3)
td = pd.Timedelta(weeks=2)
td

index = pd.date_range("2018-03-17", "2018-03-30", freq="2H")
loc = np.random.choice(np.arange(len(index)), size=4,
                       replace=False)  #随机选取4个互不相同的数
loc.sort()
loc
ts_index = index[loc]
ts_index

pd_index=ts_index.to_period("D")
pd_index

i = pd.date_range('20110101','20150101',freq='B')
s = pd.Series(1,index=i)
s
pd.Series(range(3), index=pd.date_range('2000', freq='D', periods=3))

# 可以生成理论上的时间轴
stamps = pd.date_range('2012-10-08 18:15:05', periods=4, freq='D')
stamps 