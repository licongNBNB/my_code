import os
import pandas as pd

# %%
data17 = pd.DataFrame()
for root_dir, sub_dir, files in os.walk(r"C:\Users\聪\Desktop\demo17\describe"):
    for file in files:
        file_name = os.path.join(root_dir, file)
        df = pd.read_csv(file_name, header=17)
        data17 = data17.append(df)

# %%
describe17 = data17.describe()
describe17.drop(labels='count', inplace=True)

# %%
text17 = describe17.iloc[0]
text17 = text17.append(describe17.iloc[1])
text17 = text17.append(describe17.iloc[2])
text17 = text17.append(describe17.iloc[3])
text17 = text17.append(describe17.iloc[4])
text17 = text17.append(describe17.iloc[5])
text17 = text17.append(describe17.iloc[6])
# %%
tet = pd.concat([tet, text19], axis=1)

data = pd.read_csv(r'C:\Users\聪\Desktop\demo2\八个人在所有活动中的数据集合\总和.csv', header=0)
del data['Unnamed: 0']
data = data.replace('活动一', 1)

