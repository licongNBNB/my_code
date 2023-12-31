# 对比两个表格，假设全介质表格和真实时间数据表格，自定误差率来确定无空洞的直线连接
import pandas as pd

# 读取原始表格和标准表格
rs_raw = pd.read_csv(r'D:\Study\数学建模培训\Day1\新建文件夹\RS_原始.csv', index_col=0)
rs_std = pd.read_csv(r'D:\Study\数学建模培训\Day1\新建文件夹\RS_标准.csv', index_col=0)
pq_raw = pd.read_csv(r'D:\Study\数学建模培训\Day1\新建文件夹\PQ_原始.csv', index_col=0)
pq_std = pd.read_csv(r'D:\Study\数学建模培训\Day1\新建文件夹\PQ_标准.csv', index_col=0)

# 定义误差值
tolerance = 0.01


# 对应值对比函数
def compare_values(raw_value, std_value):
    return abs(raw_value - std_value) <= (std_value * tolerance)


# 比较RS表格
for i in range(len(rs_raw.index)):
    for j in range(len(rs_raw.columns)):
        if compare_values(rs_raw.iloc[i, j], rs_std.iloc[i, j]):
            rs_raw.iloc[i, j] = 0
            print(f"应该连接{rs_raw.index[i]}和{rs_raw.columns[j]}")

# 比较PQ表格
for i in range(len(pq_raw.index)):
    for j in range(len(pq_raw.columns)):
        if compare_values(pq_raw.iloc[i, j], pq_std.iloc[i, j]):
            pq_raw.iloc[i, j] = 0
            print(f"应该连接{pq_raw.index[i]}和{pq_raw.columns[j]}")

# # 输出处理后的表格
# rs_raw.to_csv('RS_处理后.csv')
# pq_raw.to_csv('PQ_处理后.csv')
rs_diff = abs(rs_raw - rs_std) * 320
pq_diff = abs(pq_raw - pq_std) * 320
for i in range(len(rs_raw.index)):
    for j in range(len(rs_raw.columns)):
        if rs_raw.iloc[i, j] == 0:
            print(f"{rs_raw.index[i]}和{rs_raw.columns[j]}差值为{rs_diff.iloc[i, j]}")

for i in range(len(pq_raw.index)):
    for j in range(len(pq_raw.columns)):
        if pq_raw.iloc[i, j] == 0:
            print(f"{pq_raw.index[i]}和{pq_raw.columns[j]}差值为{pq_diff.iloc[i, j]}")
