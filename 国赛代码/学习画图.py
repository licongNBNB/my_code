import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['STZhongsong']  # 指定默认字体：解决plot不能显示中文问题
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
# 创建图表和子图
fig, ax = plt.subplots()
# 设置背景透明
fig.patch.set_alpha(0)
# 应用黑白风格
plt.style.use('grayscale')

# %% 折线图
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# 创建折线图
plt.plot(x, y)
# 添加标题和坐标轴标签
plt.title("简单折线图")
plt.xlabel("X轴")
plt.ylabel("Y轴")
# 显示图例
plt.legend(["折线"])
# 显示网格线
plt.grid(True)
# 显示图表

plt.savefig('plot.png', transparent=True)

plt.show()
# %% 散点图
import matplotlib.pyplot as plt

# 创建数据
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# 创建散点图
plt.scatter(x, y, c='red', label='散点')

# 添加标题和坐标轴标签
plt.title("散点图示例")
plt.xlabel("X轴")
plt.ylabel("Y轴")

# 显示图例
plt.legend()

plt.savefig('plot.png', transparent=True)

plt.show()

# %% 条形图
import matplotlib.pyplot as plt

# 创建数据
categories = ['A', 'B', 'C', 'D']
values = [15, 30, 25, 40]

# 创建条形图
plt.bar(categories, values)

# 添加标题和坐标轴标签
plt.title("条形图示例")
plt.xlabel("分类")
plt.ylabel("值")

plt.savefig('plot.png', transparent=True)

plt.show()


# %%饼图
import matplotlib.pyplot as plt

# 创建数据
sizes = [30, 20, 40, 10]
labels = ['A', 'B', 'C', 'D']

# 创建饼图
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

# 添加标题
plt.title("饼图示例")

plt.savefig('plot.png', transparent=True)

plt.show()


# %%使用imshow函数绘制热力图
import numpy as np
import matplotlib.pyplot as plt

# 创建数据
data = np.random.rand(10, 10)

# 绘制热力图
plt.imshow(data, cmap='hot', interpolation='nearest')

# 添加颜色条
plt.colorbar()

plt.savefig('plot.png', transparent=True)

plt.show()

# %% 使用pcolormesh函数绘制热力图：
import numpy as np
import matplotlib.pyplot as plt

# 创建数据
x = np.linspace(0, 1, 10)
y = np.linspace(0, 1, 10)
X, Y = np.meshgrid(x, y)
data = np.sin(2 * np.pi * X) * np.cos(2 * np.pi * Y)

# 绘制热力图
plt.pcolormesh(X, Y, data, cmap='coolwarm')

# 添加颜色条
plt.colorbar()

plt.savefig('plot.png', transparent=True)

plt.show()

# %%雷达图
categories = ['A', 'B', 'C', 'D', 'E']
values = [4, 3, 5, 2, 1]

# 创建角度
angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
angles += angles[:1]

# 创建数据点
values += values[:1]

# 绘制雷达图
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.fill(angles, values, color='skyblue', alpha=0.7)

# 设置刻度标签
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)

# 设置极坐标角度的范围
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

# 添加标题
plt.title("雷达图示例")

plt.savefig('plot.png', transparent=True)

plt.show()




















