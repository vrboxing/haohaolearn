import pandas as pd

# 2019年全年日期域
dates = pd.date_range(start='20190101', end='20191231')
df = pd.DataFrame(dates, columns=['date'])
dategrp = df.groupby(pd.Grouper(key='date', freq='Q'))

quarterlst = list()
for name, group in dategrp:
    quarterlst.append(name)
    # print(type(name))
    # print('Group:', name)
    # print(group, end='\n')
# print(quarterlst)

quartername = ["第一季度", "第二季度", "第三季度", "第四季度"]

qlst = dict()
for qn, iq in zip(quartername, quarterlst):
    qlst[qn] = iq
    # print(dategrp.get_group(iq))

# for key, value in qlst.items():
#     print(key)
#     print(dategrp.get_group(value))

print(dategrp.get_group(qlst['第一季度']))
