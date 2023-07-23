# 导入必要的库
import pandas as pd
import numpy as np
import statsmodels.api as sm

# 读取数据集
data = pd.read_csv('预处理之后的数据集.csv')

# 按照需求选择自变量和因变量
# 这里选择 AQI、PM10、O3、SO2、NO2、CO、降水量、平均气压、平均2分钟风速、平均气温和平均相对湿度 作为自变量
# 并选择 PM2.5作为因变量
X = data[['AQI', 'PM10', 'O3', 'SO2', 'NO2', 'CO', '降水量', '平均气压', '平均2分钟风速', '平均气温', '平均相对湿度']]
Y = data['PM2.5']

# 添加常数项
X = sm.add_constant(X)

# 构建线性回归模型
model = sm.OLS(Y, X).fit()

# 输出回归结果
print(model.summary())
