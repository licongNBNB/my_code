# %% figure函数
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# plt.figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None, frameon=True)
# num : 图像编号或名称，数字为编号，字符串为名称
# figsize : 指定figure的宽和高，单位为英寸
# dpi : 指定绘图对象的分辨率，即每英寸多少个像素，缺省值为80
# facecolor : 背景的颜色
# edgecolor : 边框颜色
# frameon : 是否显示边框
plt.figure(figsize=(4, 3), facecolor='blue')
plt.show()

# %% 给横纵坐标设置名称
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y = x * 2
plt.xlabel("x'slabel")  # x轴上的名字
plt.ylabel("y's;abel")  # y轴上的名字
plt.plot(x, y, color='green', linewidth=3)
plt.show()

# %%把坐标轴换成不同的单位：

plt.xticks(np.linspace(-1, 2, 5))
# 在对应坐标处更换名称
plt.yticks([-2, -1, 0, 1, 2], ['really bad', 'b', 'c', 'd', 'good'])
plt.show()
# %%多图
# subplot()方法里面传入的三个数字 前两个数字代表要生成几行几列的子图矩阵,第三个数字代表选中的子图位置
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.suptitle('我的滑板吧标题', fontsize=16, fontweight='bold')

plt.subplot(2, 1, 1)  # 第1个图
plt.plot([1, 2, 3, 4], [11, 22, 33, 44], 'o-r')  # "o-r"中r表示红色，o表示实点，-表示连接线
plt.title('画板1', color='r')

plt.subplot(2, 2, 3)  # 第2个图
plt.plot([2, 2, 2, 2])

plt.subplot(2, 2, 4)  # 第3个图
plt.plot([3, 2, 3, 4])

plt.show()
# %%plot风格
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

style = plt.style.available  # 获取所有风格
plt.style.use('grayscale')  # 使用风格
# plt.grid(axis="y")  # y坐标网格
# plt.grid(axis="x")  # x坐标网格
x = np.linspace(-1, 1, 50)
y = x ** 3
plt.xlabel("x'slabel")  # x轴上的名字
plt.ylabel("y's;abel")  # y轴上的名字
plt.plot(x, y)
plt.show()
# %% 美化
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

x = np.linspace(-10, 10)
y1 = x * 3 + 30
y2 = x ** 2
# "o-r"中r表示红色，o表示实点，-表示连接线
plt.plot(x, y1,'*:r', x, y2,  '^:m')
# 坐标网格
plt.grid(True, linestyle=':')
# 画横线
# plt.axhline(y=之前的代码)
# 画纵线
# plt.axvline(x=之前的代码)
# 画线段
# plt.axhline(y=0.5, xmin=0.25, xmax=0.75)
plt.show()

# %% 面积
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

fig, ax = plt.subplots()
ax.plot(x, y1, x, y2, color='black')
ax.fill_between(x, y1, y2, where=y2 > y1, facecolor='green')
ax.fill_between(x, y1, y2, where=y2 <= y1, facecolor='red')
ax.set_title('fill between where')
plt.show()

# %%


# %%


# %%


# %%

# %%


# %% 画一个图
plt.figure(1)
x = np.linspace(1, 0.1, 10)
y = x
plt.plot(x, y)
plt.show()

# %% 画多个图
plt.figure(num='love')
x = np.linspace(1, 0.1, 10)
y1 = 1 * x
y2 = 2 * x
y3 = 3 * x
y4 = 4 * x
plt.plot(x, y, color='green', linewidth=1.0, linestyle=':')
plt.plot(x, y2, color='red', linewidth=1.0, linestyle='-')
plt.plot(x, y3, color='green', linewidth=1.0, linestyle=':')
plt.plot(x, y4, color='red', linewidth=1.0, linestyle='-')
plt.show()
