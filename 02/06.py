# coding: utf-8
# 西暦年から平成年を求める
import datetime

s = datetime.date.today().year

print("西暦" + str(s) + "年は", end="")\

# 西暦年から平成年を計算する
# 平成1年とは、西暦1989年　差1988

h = s - 1988
print("平成" + str(h) + "年です")
