import pandas as pd

dates = pd.data_range(start='20190101', end='20191231')
df = pd.DataFrame(dates, columns=['date'])
dategrp = df.groupby(pd.Grouper(key='date', freq='Q'))

s = list()
for name, group in dategrp:
    s.append(name)
    print(type(name))
    print('Group:', name)
    print(group, end='\n')
print(s)
dategrp.get_group(s[0])
dategrp.get_group('2019-12-31 00:00:00')

gp = dategrp.get_group(s[0])
type(gp)
gp.shape

for i in range(len(gp)):
    str_date = gp.iloc[i][0].strftime('%Y-%m-%d')
    print(str_date)