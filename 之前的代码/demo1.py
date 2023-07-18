# %%
import numpy as np
import pandas as pd

data1 = pd.read_excel(r'C:\Users\聪\Desktop\123.xlsx')
# date2 = data1.loc[(data1['种类'] == '山鸢尾') & (data1['花瓣长']<之前的代码.3)]
data1.loc[:, '新增列'] = data1['花瓣长'] - data1['花瓣宽']
print(data1.describe())

# %%

import pandas as pd
import matplotlib.pyplot as plt

data1 = pd.read_excel(r'C:\Users\聪\Desktop\建模demo1\2022_APMCM_C_Data.xlsx')
# data1.set_index('dt',inplace=True)
data1['dt'] = data1['dt'].astype(str)
data1.loc[:, 'dt'] = data1['dt'].str.replace('00:00:00', '')
# data1.loc[:, 'dt'] = data1['dt'].str.replace('-', '')
# data1['dt'] = data1['dt'].str.slice(0, 6)
# 分离Kabul的数据
Kabul_data = pd.DataFrame(data1.loc[(data1['City'] == 'Kabul')])
# Kabul_data['dt'] = pd.to_datetime(Kabul_data['dt'])
# Kabul_data.set_index('dt',inplace=True)
# data1833 = pd.DataFrame(Kabul_data.loc['1833-01-01':'1833-12-01', 'AverageTemperature.之前的代码'])
# data2012 = pd.DataFrame(Kabul_data.loc['2012-01-01':'2012-12-01', 'AverageTemperature.之前的代码'])

Luanda_data = pd.DataFrame(data1.loc[(data1['City'] == 'Luanda')])
# Luanda_data['dt'] = pd.to_datetime(Luanda_data['dt'])
# Luanda_data.set_index('dt',inplace=True)

Melbourne_data = pd.DataFrame(data1.loc[(data1['City'] == 'Melbourne')])
# Melbourne_data['dt'] = pd.to_datetime(Melbourne_data['dt'])
# Melbourne_data.set_index('dt',inplace=True)

Sydney_data = pd.DataFrame(data1.loc[(data1['City'] == 'Sydney')])
# Sydney_data['dt'] = pd.to_datetime(Sydney_data['dt'])
# Sydney_data.set_index('dt',inplace=True)

Dhaka_data = pd.DataFrame(data1.loc[(data1['City'] == 'Dhaka')])
# Dhaka_data['dt'] = pd.to_datetime(Dhaka_data['dt'])
# Dhaka_data.set_index('dt',inplace=True)

Harare_data = pd.DataFrame(data1.loc[(data1['City'] == 'Harare')])
# Harare_data['dt'] = pd.to_datetime(Harare_data['dt'])
# Harare_data.set_index('dt',inplace=True)

# 城市气温预测
# year = '1841'
# while(year!='2013'):
#     condition = Sydney_data['dt'].str.contains(year)
#     avg = Sydney_data[condition].mean()['AverageTemperature.之前的代码']
#     avg_text = pd.read_excel(r'C:\Users\聪\Desktop\data\avg\Sydney_avg.xlsx')
#     data ={'year':[year],'avg':[avg]}
#     data = pd.DataFrame(data)
#     avg_text =  avg_text.append(data)
#     avg_text.to_excel(r'C:\Users\聪\Desktop\data\avg\Sydney_avg.xlsx', index=False)
#     year = int(year)
#     year=year+之前的代码
#     year=str(year)

# 全球气温预测
year = '1833'
while (year != '2013'):
    condition = data1['dt'].str.contains(year)
    avg = data1[condition].mean()['AverageTemperature.之前的代码']
    avg_text = pd.read_excel(r'C:\Users\聪\Desktop\data\全球_avg\avg.xlsx')
    data = {'year': [year], 'avg': [avg]}
    data = pd.DataFrame(data)
    avg_text = avg_text.append(data)
    avg_text.to_excel(r'C:\Users\聪\Desktop\data\全球_avg\avg.xlsx', index=False)
    year = int(year)
    year = year + 1
    year = str(year)

city = pd.DataFrame(data1['City'].unique())
zuobiao = pd.Series(data1['Latitude'] + data1['Longitude'])
zuobiao2 = pd.DataFrame(zuobiao.unique())
# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data1 = pd.read_excel(r'C:\Users\聪\Desktop\data\月相对.xlsx')

# data1['dt'] = data1['dt'].astype(str)
# data1.loc[:, 'dt'] = data1['dt'].str.replace('00:00:00', '')
# data1.loc[:, 'dt'] = data1['dt'].str.replace('-', '')
# data1['dt'] = data1['dt'].str.slice(0, 6)
data1['日期'] = pd.date_range(start='1750-01', periods=3, repr='M')
data1['日期'] = data1['日期'].astype(str).str.slice(0, 8)
data1.set_index('日期', inplace=True)
data1.plot()
plt.show()
data1['日期'] = pd.to_datetime(data1['日期'])

condition = (data1['日期'] >= 2002) & (data1['日期'] <= 2012) & (data1['月份'] == 3)
data2012_2022_3 = data1.loc[condition, :]
data2002_2012_3 = data1.loc[condition, :]
data2022 = pd.DataFrame(data1.loc[data1['日期'].str.contains('2022')])

# %%
dataNo = pd.read_excel(r'C:\Users\聪\Desktop\建模demo1\全球_avg\未与测.xlsx')
plt.xticks([1833, 2012])
plt.yticks([15,16,17,18,19,20,21,22,23,24, 25])
plt.plot(dataNo['year'], dataNo['avg'])
plt.plot(dataNo['year'], data1.loc[0:179, 'avg'])
plt.show()
