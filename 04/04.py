# coding: utf-8
# ループでリストを操作する

team = ["勇者", "戦士", "魔法使い", "盗賊"]

# print(team)
# print(team[0])

print("<select name='job'>")
for job in team:
    print("<option>" + job + "</option>")
print("</select>")


'''
team = ["勇者", "戦士", "魔法使い"]
print(team)
'''
