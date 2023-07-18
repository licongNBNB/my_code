# %%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# %%
df = pd.read_csv('Automobile.csv')
# %%
print(df.head())  # 输出前5行数据
print(df.info())  # 输出数据概览，包括数据类型和缺失值情况
print(df.describe())  # 输出数据的统计描述
# %%9
df = df.replace('?', np.nan)  # 将'?'替换为缺失值
df = df.dropna()  # 删除缺失值所在的行
# %%8
df['horsepower'] = df['horsepower'].astype('float')  # 将horsepower字段转换为float类型
# %%7
sns.pairplot(df[['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration']])
plt.show()
# %%6
corr_table = df.corr()  # 计算相关系数矩阵
plt.show()
sns.heatmap(corr_table, annot=True)  # 绘制相关系数矩阵的热力图
plt.show()
# %%5
brand_mpg = df[['name', 'mpg']].groupby('name', as_index=False).mean()
brand_mpg = brand_mpg.sort_values(by='mpg', ascending=False).head(10)  # 按mpg降序排序，取前10个
sns.barplot(x='name', y='mpg', data=brand_mpg)  # 绘制柱状图
plt.show()
# %%4
plt.hist(df['mpg'], bins=20)
plt.xlabel('mpg')
plt.ylabel('frequency')
plt.title('Distribution of mpg')
plt.show()
# %%3
sns.boxplot(df['weight'])
plt.xlabel('weight')
plt.title('Boxplot of weight')
plt.show()
# %%2
sns.kdeplot(df['horsepower'], shade=True)
plt.xlabel('horsepower')
plt.title('Density plot of horsepower')
plt.show()
# %%之前的代码
origin_counts = df['origin'].value_counts()
origin_counts.plot(kind='pie', autopct='%之前的代码.1f%%')
plt.title('Pie chart of origin counts')
plt.show()
