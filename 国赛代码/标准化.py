import numpy as np
import pandas as pd

# %%    对行标准化（极大型，极小型，中间型，区间型）

# 以下为需要更改的参数
# 以下为需要更改的参数
data = pd.read_excel(r"D:\Study\py\国赛数据集\测试topsis.xlsx")
data = data.set_index("风景地点")
# 指定每一列的正向化类型
col_types = {
    '风景': 'max_min',
    '人文': 'max_min',
    '拥挤程度': 'min_max',
    '票价': 'min_max',
    'PH值': 'median'
}


# 以上为需要更改的参数
# 以上为需要更改的参数

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
    normalized = (normalized - np.min(normalized)) / (np.max(normalized) - np.min(normalized))

    return normalized


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

# %%    对列标准化（极大型，极小型，中间型，区间型）
import numpy as np
import pandas as pd

# 读取数据
data = pd.read_csv(r"D:\数学建模\代码课件\正课配套的课件和代码\第12讲.预测模型\代码和例题数据\12.csv")
data = data.set_index("年份")

# 指定每一列的正向化类型
col_types = {
    '单产': 'max_min',
    '种子费': 'max_min',
    '化肥费': 'max_min',
    '农药费': 'max_min',
    '机械费': 'max_min',
    '灌溉费': 'max_min'
}


# 定义标准化函数
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
    normalized = (normalized - np.min(normalized)) / (np.max(normalized) - np.min(normalized))
    return normalized


# 标准化每一列
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
    else:
        raise ValueError(f"Invalid normalization type for column '{col}'.")
