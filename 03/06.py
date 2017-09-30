# coding: utf-8
# 標準入力とループ処理

count = int(input())

# print("データ個数" + str(count))

for i in range(count):
    line = input().rstrip()
    print(line + "は")

'''
count = int(input())

print("データ個数" + str(count))

for i in range(count):
    line = input().rstrip()
    print("hello " + line)
'''

'''
line = input()
print("hello " + line)

line = input()
print("hello " + line)
'''
