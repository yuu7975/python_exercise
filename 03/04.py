# coding: utf-8
# 年齢入力のプルダウン作成

print("<select name=\'age\'>")
for age in range(100):
    print("<option>" + str(age + 1) + "才</option>")
print("</select>")

'''
print("<select name=\'age\'>")
print("<option>1才</option>")
print("<option>2才</option>")
print("</select>")
'''
