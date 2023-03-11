# i = 1
# while i < 11:
#     print(i)
#     i += 1

# 1-100的和
# i = 1
# he = 0
# while i < 101:
#     he += i
#     i += 1
# print(he)

# he = 0
# i = -1
# flag = True
# while flag:
#     i = int(input('请输入一个数字'))
#     he += i
#     if i == 0:
#         flag = False
# print(he)

# he = 0
# i = -1
# while True:
#     i = int(input('请输入一个数字'))
#     he += i
#     if he > 100:
#         break  # 利用break跳出循环
# print(he)

# 搬运列表
# l = [1, 2, 3, 4, 5, 6]
# newL = []
# while l:  # 当l不为空时执行
#     newL.append(l.pop())

# 把指定元素从列表中全部删除
# while 1 in newL:
#     newL.remove(1)

# 填充字典
# d = {}
# while True:
#     key = input('请输入键值对的键：')
#     value = input('请输入键值对的值：')
#     d[key] = value
#     res = input('您是否需要继续填写')
#     if res == 'no':
#         break
# print(d)

# print 换行
# for i in range(1, 11):
#     # 默认print(i,'\n') 换行，可以修改第二个参数为''使print不换行
#     print(i, end='')

# 打印4行12列*
# for row in range(1, 5):
#     for star in range(0, 12):
#         print('*', end='')
#     print()

# 乘法口诀
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(i, 'x', j, '=', i * j, end=' ')
#     print()

# 输入的数是否是素数
# n = int(input('请输入一个大于1的整数'))
# isSu = True
# for i in range(2, n):
#     if n % i == 0:
#         isSu = False
#         break
# if isSu:
#     print(n, '是素数')
# else:
#     print(n, '不是素数')

# 三位数分别取出
# n = int(input('请输入一个三位数'))
# ge = n % 10
# shi = n // 10 % 10
# bai = n // 100

# 8的阶乘
# res = 1
# for i in range(1, 9):
#     res *= i
# print(res)
