"""
задайте список. Напишите программу, которая определит, присутствует ли в заданном списке некое число
"""

lst = ['red', 'green', 'blue2']
num = 2
answer = False
for i in lst:
    if i.count(str(num)):

    # if str(num) in i:
        answer = True
        break
    # print(i)
    # for j in i:
    #     # print(j)
    #     if j == str(num):
    #         answer = True
    #         break
print(answer)

