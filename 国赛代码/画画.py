# %%
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['STZhongsong']  # 指定默认字体：解决plot不能显示中文问题
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

# %% 热力图
data = pd.read_excel("")

fig, ax = plt.subplots(figsize=(10, 8), facecolor='none')
ax.set_facecolor("none")

heatmap = sns.heatmap(data, cmap="gray_r", ax=ax)
ax.axis('off')
plt.savefig('heatmaps.png', transparent=True)

# %%
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 假设data是一个pandas DataFrame对象，列名为'x', 'y', 'z'
# 如果data中的列名不是'x', 'y', 'z'，请将下面的代码中的列名替换为实际的列名

fig = plt.figure(figsize=(8, 6))  # 设置图形大小
ax = fig.add_subplot(111, projection='3d')
ax.set_title('3D Scatter Plot')  # 设置图形标题

# 自定义点的颜色和样式
ax.plot(result4['x/m'], result4['y/m'], result4['z/m'], c='blue', label='Result 4')


# 添加图例和坐标轴标签
ax.legend()
ax.set_xlabel('X轴')
ax.set_ylabel('Y轴')
ax.set_zlabel('Z轴')


# 设置三个坐标轴的相等纵横比
ax.set_box_aspect([1, 1, 1])

# 显示图形
plt.show()

