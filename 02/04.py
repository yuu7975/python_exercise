# coding: utf-8
# おみくじを作る
# 比較演算子 == > < >= <= !=
# 大吉  中吉  小吉  凶  大凶

import random

number = random.randint(1,10)

# print(number)

if number == 1:
    print("大吉")
elif number == 2:
    print("中吉")
elif number <= 4:
    print("小吉")
elif number <= 7:
    print("凶")
else:
    print("大凶")