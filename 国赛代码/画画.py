# %%
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['STZhongsong']    # 指定默认字体：解决plot不能显示中文问题
mpl.rcParams['axes.unicode_minus'] = False           # 解决保存图像是负号'-'显示为方块的问题

# %% 热力图
data = pd.read_excel("")

fig, ax = plt.subplots(figsize=(10, 8), facecolor='none')
ax.set_facecolor("none")

heatmap = sns.heatmap(data, cmap="gray_r", ax=ax)
ax.axis('off')
plt.savefig('heatmaps.png', transparent=True)
