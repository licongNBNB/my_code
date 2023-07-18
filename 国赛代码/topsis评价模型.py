import numpy as np
import pandas as pd


# %%
def normalize_min_max(data):
    """极小型正向化,值越小结果越接近1"""
    normalized = 1 - (data - np.min(data)) / (np.max(data) - np.min(data))
    return normalized


def normalize_max_min(data):
    """极大型正向化,值越大结果越接近1"""
    normalized = (data - np.min(data)) / (np.max(data) - np.min(data))
    return normalized


def normalize_range(data, min_val, max_val):
    """区间型正向化,在指定区间内为1,否则为0"""
    normalized = np.where((data >= min_val) & (data <= max_val), 1, 0)
    return normalized


def normalize_median_01(data, median):
    normalized = 1 - np.abs(data - median) / median

    # 映射到0-1区间
    normalized = (normalized - np.min(normalized)) / (np.max(normalized) - np.min(normalized))

    return normalized


# %%标准化（极大型，极小型，中间型，区间型）
data = pd.read_excel(r"D:\Study\py\国赛数据集\测试topsis.xlsx")
data = data.set_index("风景地点")
# 指定每一列的正向化类型
col_types = {
    '风景': 'max_min',
    '人文': 'max_min',
    '拥挤程度': 'min_max',
    '票价': 'min_max'
}

for col, tp in col_types.items():
    if tp == 'min_max':
        data[col] = normalize_min_max(data[col])
    elif tp == 'max_min':
        data[col] = normalize_max_min(data[col])
    elif tp == 'range':
        data[col] = normalize_range(data[col], min_val=0, max_val=100)
    elif tp == 'median':
        median = 7  # 自己给定的中间值
        data[col] = normalize_median_01(data[col], median)
# %%topsis建模

# 假设权重已确定，存储在一个权重向量中
weights = [0.25, 0.25, 0.25, 0.25]  # 示例权重
# 计算正理想解和负理想解
pis = np.max(data)
nis = np.min(data)
# 计算指标与正负理想解的距离
distance_to_pis = np.sqrt(np.sum((data - pis) ** 2, axis=1))
distance_to_nis = np.sqrt(np.sum((data - nis) ** 2, axis=1))
# 计算综合评价指数
closeness_coefficient = distance_to_nis / (distance_to_pis + distance_to_nis)
# 添加综合评价指数到DataFrame中
data['Closeness Coefficient'] = closeness_coefficient

# 根据综合评价指数排序
ranked_df = data.sort_values('Closeness Coefficient', ascending=False)
