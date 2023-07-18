# %%导入库
import pandas as pd
import numpy as np
from pylab import mpl
import matplotlib.pyplot as plt

# %% 标准化
# 指定CSV文件的绝对路径
file_path = 'D:\\数学建模\\代码课件\\正课配套的课件和代码\\第12讲.预测模型\\代码和例题数据\\12.csv'

# 读取CSV文件
df = pd.read_csv(file_path)
df = df.set_index("年份")
# 按列进行标准化
for col in df.columns:
    df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())


# %% 建模
def gray_relational_degree(seq1, seq2):
    return 1 - (np.abs(seq1 - seq2) / np.max(np.abs(seq1 - seq2)))


gray_rels = []
for col in df.columns[1:]:
    # 母序列的选取“单产”
    gray_rel = gray_relational_degree(df['单产'], df[col]).mean()
    gray_rels.append((col, gray_rel))
print(gray_rels)
# %% 画图


mpl.rcParams['font.sans-serif'] = ['STZhongsong']  # 指定默认字体：解决plot不能显示中文问题
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

# 可视化
plt.figure()
plt.plot(df.index, df['单产'], color='black')
for i, rel in enumerate(gray_rels):
    plt.plot(df.index, df[rel[0]], linestyle='--', color='black', alpha=0.5)

plt.xlabel('年份')
plt.ylabel('标准化指标')
plt.tight_layout()

# 显示图像
plt.show()
