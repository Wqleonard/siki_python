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

he = 0
i = -1
while True:
    i = int(input('请输入一个数字'))
    he += i
    if he > 100:
        break  # 利用break跳出循环
print(he)
