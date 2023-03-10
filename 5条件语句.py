import random

age = 34
# if age > 40:
#     print('中年版')
# elif age < 30:
#     print('少年版')
# else:
#     print('青年版')
# print('结束')

res = 18 <= age <= 40
# res1 = age >= 40 and age <= 50  # 同时满足
res = age <= 3 or age >= 80  # 满足1个

l = [1, 2, 3, 4, 5]
res = 1 in l  # 元素是否在里面
res1 = 6 not in l  # 元素是否不在里面

# print('请输入你的年龄：')
# age = input()
# age = int(age)

# print(random.randint(1, 4))  # 生成1-4之间的一个随机整数  包括1和4
#
# print('我现在内心想了一个1-20的数字')
# number = random.randint(1, 20)
# for t in range(1, 6):  # 5次机会
#     print('猜猜我想的是什么')
#     n = int(input())
#     if n < number:
#         print('猜小了')
#     elif n > number:
#         print('猜大了')
#     else:
#         print('猜对了')
#         break
# print('游戏结束')


# l = ['sdf', 'siki', 'cvcve']
# for s in l:
#     if s == 'siki':
#         print(s.upper())
#     else:
#         print(s)
