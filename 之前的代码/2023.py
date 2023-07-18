import pandas as pd
data1 = pd.read_excel(r'C:\Users\聪\Desktop\23美赛\Problem_C_Data_Wordle.xlsx')
not_five_chars = data1[data1['Word'].str.len() != 5]


import pandas as pd

df = pd.read_excel(r'C:\Users\聪\Desktop\23美赛\1.xlsx')
df['repeated_letters'] = 0
for index, row in df.iterrows():
    s = row['Word']
    repeated_letters = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            repeated_letters += 1
    df.at[index, 'repeated_letters'] = repeated_letters

not_five_chars = df[df['Word'].str.len() != 5]

import pandas as pd

# 创建一个Dataframe
df = pd.read_excel(r'C:\Users\聪\Desktop\23美赛\剔除后 加入特征值.xlsx')
# 定义一个函数来计算单词的音节数
def count_syllables(word):
    # 计算单词中元音的数量
    num_vowels = len([letter for letter in word if letter in 'aeiou'])
    # 从单词的总长度中减去元音的数量
    return len(word) - num_vowels
# 将函数应用于Dataframe，并将结果添加到一个新的列中
df['num'] = df['Word'].apply(count_syllables)





