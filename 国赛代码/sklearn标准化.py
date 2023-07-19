# %%行标准化
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# 读取数据
data = pd.read_excel(r"D:\Study\py\国赛数据集\测试topsis.xlsx")
data = data.set_index("风景地点")

# 指定每一列的正向化类型
col_types = {
    '风景': 'min_max',
    '人文': 'min_max',
    '拥挤程度': 'max_min',
    '票价': 'max_min',
    'PH值': 'median'
}

# 转置数据，将特征列放在行上
data_transposed = data.T
# 标准化每一列
for col, tp in col_types.items():
    if tp == 'min_max':
        scaler = MinMaxScaler()
    elif tp == 'max_min':
        scaler = StandardScaler()
    elif tp == 'median':
        median = 7  # 自己给定的中间值
        scaler = StandardScaler(with_mean=median, with_std=False)
    else:
        raise ValueError(f"Invalid normalization type for column '{col}'.")

    data[[col]] = scaler.fit_transform(data[[col]])

# 将数据转置回原来的形式
data_normalized = data_transposed.T
# %%对列标准化
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# 读取数据
data = pd.read_csv(r"D:\数学建模\代码课件\正课配套的课件和代码\第12讲.预测模型\代码和例题数据\12.csv")
data = data.set_index("年份")

# 指定每一列的正向化类型
col_types = {
    '单产': 'min_max',
    '种子费': 'min_max',
    '化肥费': 'min_max',
    '农药费': 'min_max',
    '机械费': 'min_max',
    '灌溉费': 'min_max'
}

# 标准化每一列
for col, tp in col_types.items():
    if tp == 'min_max':
        scaler = MinMaxScaler()
    elif tp == 'max_min':
        scaler = StandardScaler()
    else:
        raise ValueError(f"Invalid normalization type for column '{col}'.")

    data[[col]] = scaler.fit_transform(data[[col]])
