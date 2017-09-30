# coding: utf-8
# whileによるループ処理
import random

hp = 30
while hp > 0:
    hit = random.randint(1, 10)
    print("スライムに" + str(hit) + "のダメージを与えた")
    hp -= hit
print("スライムをたおした")

'''
i = 1
while i <= 10:
    print(i)
    i += 1
print("last" + str(i))
'''
