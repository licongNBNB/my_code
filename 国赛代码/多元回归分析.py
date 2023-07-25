# 导入必要的库
import pandas as pd
import numpy as np
import statsmodels.api as sm

# 读取数据集
data = pd.read_csv(r'C:\Users\聪\Desktop\新建文件夹\新数据集\预处理之后的数据集 - 副本.csv')

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

# 画图
import matplotlib.pyplot as plt

# Coefficients of each feature
coefficients = {
    'AQI': 0.0928,
    'PM10': 0.4187,
    'O3': -0.0227,
    'SO2': -0.0617,
    'NO2': -0.1262,
    'CO': 16.3342,
    '降水量': -0.3385,
    '平均气压': 0.0386,
    '平均2分钟风速': -0.7417,
    '平均气温': -0.6484,
    '平均相对湿度': 0.1493
}

# Get absolute values of the coefficients
abs_coefficients = {feature: abs(coef) for feature, coef in coefficients.items()}

# Create a bar plot with black-and-white style
plt.figure(figsize=(10, 6))
bars = plt.bar(abs_coefficients.keys(), abs_coefficients.values(), edgecolor='black', linewidth=1.5, color='white')
plt.xlabel('Features')
plt.ylabel('Absolute Coefficient')
plt.title('Impact of Features on PM2.5')

# Set the font color to black for better visibility in a white background
plt.xticks(color='black')
plt.yticks(color='black')

plt.xticks(rotation=45)
plt.axhline(0, color='gray', linewidth=0.5, linestyle='dashed')  # Add a horizontal line at y=0
plt.grid(axis='y', linestyle='dotted', linewidth=0.5)

# Set the background to white
plt.gca().set_facecolor('white')

# Save the plot with transparent background
# plt.savefig('pm2.5_impact.png', dpi=300, bbox_inches='tight', transparent=True)
plt.show()
