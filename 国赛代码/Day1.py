# %%假设完全介质，并无空气洞的情况下，算出两两点之间的时间。
import math
import pandas as pd


def distance_between_points(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# 原始数据
P_points = [(0, 0), (40, 0), (80, 0), (120, 0), (160, 0), (200, 0), (240, 0)]
O_points = [(0, 240), (40, 240), (80, 240), (120, 240), (160, 240), (200, 240), (240, 240)]

R_points = [(0, 0), (0, 40), (0, 80), (0, 120), (0, 160), (0, 200), (0, 240)]
S_points = [(240, 0), (240, 40), (240, 80), (240, 120), (240, 160), (240, 200), (240, 240)]


# 计算距离并创建表格
def create_distance_table(points1, points2):
    distance_table = []
    for point1 in points1:
        row = []
        for point2 in points2:
            distance = distance_between_points(point1[0], point1[1], point2[0], point2[1])
            row.append(distance)
        distance_table.append(row)
    return distance_table


# 计算 P 点和 O 点之间的距离
distance_PO_table = create_distance_table(P_points, O_points)

# 计算 R 点和 S 点之间的距离
distance_RS_table = create_distance_table(R_points, S_points)

# 将列表转换为DataFrame
df_PO = pd.DataFrame(distance_PO_table, index=[f'P{i + 1}' for i in range(len(P_points))],
                     columns=[f'O{i + 1}' for i in range(len(O_points))])
df_RS = pd.DataFrame(distance_RS_table, index=[f'R{i + 1}' for i in range(len(R_points))],
                     columns=[f'S{i + 1}' for i in range(len(S_points))])

# 将两个表格中的每个数都除以 2880
df_PO /= 2880
df_RS /= 2880

# 打印 DataFrame
print("Distance between P points and O points (divided by 2880):")
print(df_PO)

print("\nDistance between R points and S points (divided by 2880):")
print(df_RS)

# 题目中给出的数据
data1 = {
    'tij': ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7'],
    'Q1': [0.0611, 0.0989, 0.3052, 0.3221, 0.3490, 0.3807, 0.4311],
    'Q2': [0.0895, 0.0592, 0.4131, 0.4453, 0.4529, 0.3177, 0.3397],
    'Q3': [0.1996, 0.4413, 0.0598, 0.4040, 0.2263, 0.2364, 0.3566],
    'Q4': [0.2032, 0.4318, 0.4153, 0.0738, 0.1917, 0.3064, 0.1954],
    'Q5': [0.4181, 0.4770, 0.4156, 0.1789, 0.0839, 0.2217, 0.0760],
    'Q6': [0.4923, 0.5242, 0.3563, 0.0740, 0.1768, 0.0939, 0.0688],
    'Q7': [0.5646, 0.3805, 0.1919, 0.2122, 0.1810, 0.1031, 0.1042]
}

data2 = {
    'tij': ['R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7'],
    'S1': [0.0645, 0.0753, 0.3456, 0.3655, 0.3165, 0.2749, 0.4434],
    'S2': [0.0602, 0.0700, 0.3205, 0.3289, 0.2409, 0.3891, 0.4919],
    'S3': [0.0813, 0.2852, 0.0974, 0.4247, 0.3214, 0.5895, 0.3904],
    'S4': [0.3516, 0.4341, 0.4093, 0.1007, 0.3256, 0.3016, 0.0786],
    'S5': [0.3867, 0.3491, 0.4240, 0.3249, 0.0904, 0.2058, 0.0709],
    'S6': [0.4314, 0.4800, 0.4540, 0.2134, 0.1874, 0.0841, 0.0914],
    'S7': [0.5721, 0.4980, 0.3112, 0.1017, 0.2130, 0.0706, 0.0583]
}

data1 = pd.DataFrame(data1)
data2 = pd.DataFrame(data2)
data1 = data1.set_index("tij")
data2 = data2.set_index("tij")
