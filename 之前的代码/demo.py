# %% 8
import math
from random import random

import numpy

s = 0
item = 1
flag = 1
n = 0
while abs(item) > 1e-6:
    s = s + item
    flag = -flag
    n = n + 1
    item = flag / (2 * n + 1)
print(s * 4)


# %% 10
def fibonacci1(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        print(a)


fibonacci1(9)
# %% 之前的代码
for i in range(1, 4):
    print("")
    for j in range(1, 7):
        print("* ", end="")
# %% 2
for i in range(1, 4):
    print(" ")
    for j in range(1, 7):
        print("* ", end="")

# %% 3
a = eval(input("sad"))
d = a // 100
b = a / 10
c = a % 10
print()
# %% 4

# %% 5
for x in range(0, 101):  # 设公鸡为x，
    for y in range(0, 101):  # 设母鸡为y
        for z in range(0, 101):  # 设母鸡为y
            if 5 * x + 3 * y + z / 3 == 100 and x + y + z == 100:
                print(x, y, z)

# %%
scores = {}

# 循环输入5门科目的成绩
for i in range(5):
    subject, score = input().split()
    scores[subject] = int(score)

# 查找最高和最低成绩的科目和分数
max_score = max(scores.values())
min_score = min(scores.values())
max_subjects = [subject for subject, score in scores.items() if score == max_score]
min_subjects = [subject for subject, score in scores.items() if score == min_score]

# 输出结果
print(max_score, end=' ')
print(' '.join(max_subjects))
print(min_score, end=' ')
print(' '.join(min_subjects))
