# %%
import jieba
import wordcloud
from matplotlib import pyplot as plt

# 读取文本内容
with open('data.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# 分词
words = jieba.cut(text)

# 统计词频
word_dict = {}
for word in words:
    if len(word) > 1:
        word_dict[word] = word_dict.get(word, 0) + 1

# 生成词云图
wc = wordcloud.WordCloud(
    font_path='msyh.ttc',
    background_color='white',
    max_words=100,
    max_font_size=100,
    width=800,
    height=600,
    collocations=False
)
wc.generate_from_frequencies(word_dict)

# 显示词云图
plt.imshow(wc)
plt.axis('off')
plt.show()

# 保存词云图
wc.to_file('wordcloud.png')
