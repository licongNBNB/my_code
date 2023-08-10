import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


#%%
data = pd.read_excel('./模拟数据/附件3-弹性模量与压力.xlsx')

x = data['压力(MPa)']
y = data['密度(mg/mm3)']

# 定义三次多项式函数
def fit_function(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d

# 进行三次多项式拟合
params, _ = curve_fit(fit_function, x, y)
a_fit, b_fit, c_fit, d_fit = params

# 构建拟合函数的表达式
fit_expression = f'{a_fit:.4f} * x^3 + {b_fit:.4f} * x^2 + {c_fit:.4f} * x + {d_fit:.4f}'

# 计算拟合后的弹性模量数据
y_fit = fit_function(x, a_fit, b_fit, c_fit, d_fit)

# 计算决定系数
y_mean = np.mean(y)
ssr = np.sum((y_fit - y_mean) ** 2)
sst = np.sum((y - y_mean) ** 2)
r_squared = ssr / sst
print(r_squared)
# 绘图
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'k-', label='原始数据')
fit_x = np.linspace(min(x), max(x), num=100)
fit_y = fit_function(fit_x, a_fit, b_fit, c_fit, d_fit)
plt.plot(fit_x, fit_y, 'r-', label='拟合曲线')
plt.xlabel('压力(MPa)')
plt.ylabel('密度(mg/mm3)')
plt.text(0.2, 0.1, f'拟合函数: {fit_expression}', transform=plt.gca().transAxes, fontsize=12)
print(f'拟合函数: {fit_expression}')

plt.legend()
plt.tight_layout()
plt.show()
#%%
