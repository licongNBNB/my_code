import pandas as pd

# %%


path1_1 = 'a'
path1_2 = '之前的代码'
path1_2 = path1_2.zfill(2)
path1 = path1_1 + path1_2
path2_1 = 'p'
path2_2 = '8'
path2 = path2_1 + path2_2
path3_1 = 's'
path3_2 = '之前的代码'
path3_2 = path3_2.zfill(2)
path3 = path3_1 + path3_2
path = "C:/Users/聪/Desktop/demo2/origin_data原始数据" + '/' + path1 + '/' + path2 + '/' + path3 + '.txt'
data1 = pd.read_csv(path, header=None)
# %%
data1 = pd.read_csv(r'C:\Users\聪\Desktop\demo2\八个人在所有活动中的数据集合\1\第八个人.csv', header=None)
path1 = '之前的代码'
# %%
for i in range(0, 18):
    path1 = int(path1)
    path1 = path1 + 1
    path1 = str(path1)
    path = 'C:/Users/聪/Desktop/demo2/八个人在所有活动中的数据集合/' + path1 + '/' + '8.csv'
    data2 = pd.read_csv(path, header=None)
    data1 = pd.concat([data1, data2], axis=1)
# %%
path3_2 = int(path3_2)
path3_2 = path3_2 + 1
path3_2 = str(path3_2)
path3_2 = path3_2.zfill(2)
path3 = path3_1 + path3_2
path = "C:/Users/聪/Desktop/demo2/origin_data原始数据" + '/' + path1 + '/' + path2 + '/' + path3 + '.txt'
data2 = pd.read_csv(path, header=None)
data1 = data1.append(data2)

# %%
person = '之前的代码'
for j in range(0, 8):
    path3_1 = 's'
    path3_2 = '之前的代码'
    path3_2 = path3_2.zfill(2)
    path3 = path3_1 + path3_2
    data1 = pd.read_csv(
        "C:/Users/聪/Desktop/demo2/origin_data原始数据" + '/' + path1 + '/' + path2 + '/' + path3 + '.txt',
        header=None)
    for i in range(0, 59):
        path3_2 = int(path3_2)
        path3_2 = path3_2 + 1
        path3_2 = str(path3_2)
        path3_2 = path3_2.zfill(2)
        path3 = path3_1 + path3_2

        data2 = pd.read_csv(
            "C:/Users/聪/Desktop/demo2/origin_data原始数据" + '/' + path1 + '/' + path2 + '/' + path3 + '.txt',
            header=None)
        data1 = data1.append(data2)
    to_path = 'C:/Users/聪/Desktop/demo2/八个人在所有活动中的数据集合/之前的代码' + '/' + '第七个人.csv'
    data1.to_csv(to_path)
    person = int(person)
    person = person + 1
    person = str(person)
    path2_2 = int(path2_2)
    path2_2 = path2_2 + 1
    path2_2 = str(path2_2)
    path2 = path2_1 + path2_2

# %%
basedata = pd.read_csv(
    'C:/Users/聪/Desktop/demo2/八个人在所有活动中的数据集合/19/之前的代码.csv',
    header=0
)
path = ''
for i in range(0, 8):
    data = pd.read_csv(
        'C:/Users/聪/Desktop/demo2/八个人在所有活动中的数据集合/19/' + path + '.csv',
        header=0
    )
    basedata = basedata.append(data)
    path = int(path)
    path = path + 1
    path = str(path)
basedata.to_csv(r'C:\Users\聪\Desktop\demo2\八个人在所有活动中的数据集合\19\活动19总和.csv')
# %%
basedata = pd.read_csv(
    'C:/Users/聪/Desktop/demo2/八个人在所有活动中的数据集合/每个活动的总数据/活动' + '之前的代码' + '总和.csv',
    header=0,
    encoding="gbk"
)
path = '2'
for i in range(0, 18):
    data = pd.read_csv(
        'C:/Users/聪/Desktop/demo2/八个人在所有活动中的数据集合/每个活动的总数据/活动' + path + '总和.csv',
        encoding="gbk",
        header=0
    )
    basedata = basedata.append(data)
    path = int(path)
    path = path + 1
    path = str(path)
basedata.to_excel(r'C:\Users\聪\Desktop\demo2\八个人在所有活动中的数据集合\总和.csv', encoding="utf_8_sig")
print('成功')

condition = basedata['活动名'].str.contains('活动一')
describe = basedata[condition].describe()
describe.drop(labels='count', inplace=True)
basedata.isnull().sum()

basedata.to_excel(r'C:\Users\聪\Desktop\demo2\八个人在所有活动中的数据集合\总和.xlsx')

basedata2 = basedata.iloc[:, 0:46].round(decimals=2)
basedata=pd.read_csv(r'C:\Users\聪\Desktop\demo2\八个人在所有活动中的数据集合\basedata2.csv',header=0)
del basedata['Unnamed: 0']