import math

import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import LSTM, Dense

# 假设你已经将完整数据加载到名为"data"的Pandas DataFrame中
# 如果还没有加载数据，请将数据加载到名为"data"的DataFrame中

data = pd.read_csv(r'C:\Users\聪\Desktop\新建文件夹\新数据集\合并日期.csv')  # 用于从CSV文件加载数据的示例

# 选择目标和特征
target_col = 'PM2.5'
feature_cols = ['CO']

# 提取目标列和特征列
X = data[feature_cols].values
y = data[target_col].values.reshape(-1, 1)

# 进行数据归一化
scaler = MinMaxScaler()
X_normalized = scaler.fit_transform(X)

# 定义时间步
time_steps = 30

# 构建时间序列样本
X_time_series = []
y_time_series = []
for i in range(time_steps, len(X_normalized)):
    X_time_series.append(X_normalized[i - time_steps:i])
    y_time_series.append(y[i, 0])
X_time_series, y_time_series = np.array(X_time_series), np.array(y_time_series)

# 拆分数据集为训练集和测试集（按时间顺序拆分）
X_train, X_test, y_train, y_test = train_test_split(X_time_series, y_time_series, test_size=0.2, shuffle=False)

# 构建LSTM模型
model = Sequential()
model.add(LSTM(units=50, input_shape=(X_train.shape[1], X_train.shape[2])))  # 修正输入维度
model.add(Dense(units=1))
# 在这里你可以选择其他参数，如optimizer，loss等，具体的选择需要根据实际情况和实验结果来确定
model.compile(optimizer='adam', loss='mean_squared_error')

# 训练模型
# 在这里你可以选择epoch和batch_size等参数，具体的选择需要根据实际情况和实验结果来确定
model.fit(X_train, y_train, epochs=1000, batch_size=1)

# 准备测试数据
X_test_reshaped = X_test.reshape(X_test.shape[0], X_test.shape[1], X_test.shape[2])

# 进行预测
predicted_pm25 = model.predict(X_test_reshaped)

# 进行逆归一化还原预测结果
predicted_pm25_original = scaler.inverse_transform(predicted_pm25)

# 进行逆归一化还原真实标签
y_test_original = scaler.inverse_transform(y_test)

# 计算预测结果和真实标签的误差
rmse = math.sqrt(mean_squared_error(predicted_pm25_original, y_test_original))
print(f'Mean Squared Error (MSE): {rmse}')
