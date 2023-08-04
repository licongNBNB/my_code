import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# 当处理异常值时，一种常见且有效的方法是使用箱线图（Box Plot）和四分位数（Quartiles）来识别异常值，
# 并使用IQR（四分位数间距）来确定异常值的阈值
# 箱线图是一种可视化工具，用于显示数据的分布情况和异常值的存在。它由一个箱体和两个“触须”组成。
# 箱体表示数据的中间50%（第二四分位数，Q2，即中位数），上下触须分别表示数据的上25%（第三四分位数，Q3）
# 和下25%（第一四分位数，Q1）的范围。箱体的长度称为IQR，即IQR = Q3 - Q1。
# 异常值的识别：
# 根据箱线图的构造，异常值通常被定义为在数据的范围之外的数据点。
# 具体来说，异常值是低于Q1 - 1.5 * IQR或高于Q3 + 1.5 * IQR的数据点
#
# 线性插值法是一种简单且常用的插值方法。
# 对于一维情况，假设有两个已知数据点：(x1, y1)和(x2, y2)，
# 其中x1和x2为自变量，y1和y2为对应的因变量。要估计在x0位置的缺失值y0，
# 其中x0介于x1和x2之间，可以使用线性插值公式：
# y0 = y1 + (x0 - x1) * (y2 - y1) / (x2 - x1)

# 缺失值的填充可能会引入噪声和偏差
data = pd.read_excel(r"C:\Users\25800\Desktop\project\my_code\国赛数据集\1.xlsx", sheet_name=0)
data['层数'].fillna(method='ffill', inplace=True)
data = data.set_index("层数")
# data = data.drop('年', axis=1)
# data = data.drop('月', axis=1)
# data = data.drop('日', axis=1)
# data = data.drop('质量等级', axis=1)


# 定义异常值处理函数
def handle_outliers(column):
    Q1 = np.percentile(column, 25)
    Q3 = np.percentile(column, 75)
    IQR = Q3 - Q1
    threshold = 1.5 * IQR
    column[(column < Q1 - threshold) | (column > Q3 + threshold)] = np.nan
# 定义异常值处理函数，并返回处理后的异常值数量
def handle_outliers(column):
    Q1 = np.percentile(column, 25)
    Q3 = np.percentile(column, 75)
    IQR = Q3 - Q1
    threshold = 1.5 * IQR
    outliers_count = ((column < Q1 - threshold) | (column > Q3 + threshold)).sum()
    column[(column < Q1 - threshold) | (column > Q3 + threshold)] = np.nan
    return outliers_count

# 对所有列进行异常值处理，并统计异常值数量
outliers_count_total = 0
for col in data.columns:
    outliers_count_total += handle_outliers(data[col])


# 输出异常值数量
print("处理后的异常值数量：", outliers_count_total)


# 对所有列进行异常值处理
for col in data.columns:
    handle_outliers(data[col])


# 使用线性插值进行缺失值处理
data = data.interpolate(method='slinear', axis=0)


# 绘制箱型图
fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(12, 6), dpi=150)  # 调整figsize适应三张图
axs = axs.ravel()
for i, col in enumerate(['x/m', 'y/m', 'z/m']):
    axs[i].boxplot(data[col].dropna().values, sym='k.')
    axs[i].set_title(col, fontsize=10)
    axs[i].set_ylabel('Concentration', fontsize=8)
    axs[i].tick_params(axis='both', labelsize=8)
    axs[i].spines['top'].set_visible(False)
    axs[i].spines['right'].set_visible(False)
    axs[i].spines['bottom'].set_linewidth(0.5)
    axs[i].spines['left'].set_linewidth(0.5)
    axs[i].spines['bottom'].set_color('black')
    axs[i].spines['left'].set_color('black')
    axs[i].set_axisbelow(True)
    axs[i].grid(axis='y', linestyle='-', alpha=0.4, linewidth=0.5, color='gray')
    axs[i].set_facecolor('white')

# 保存图片并设置背景透明
fig.savefig('boxplot.png', bbox_inches='tight', pad_inches=0, format='png')

# 展示生成的三张图
plt.show()

description = data.describe()
