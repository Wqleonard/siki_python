# key-value 键值对 key可以是字符串数字和(布尔) value可以是任意类型
# stu1 = {'name': 'wq',
#         'age': 17,
#         'gender': 'man'}
# print(stu1['name']) 获取属性
# stu1['rank'] = 3 添加属性

# del(stu1['age']) 删除属性两种方式
# del stu1['age']

# 允许列表换行
# l = ['si', 'zs',
#      'mc', 'sk', 'si',
#      'zs', 'mc', 'sk']
# 连续字符串 \ \\\ 单个或三个\
# str = 'asfdfasjklfk\
# jakslkfalskf'

# 嵌套使用
# students = [{'name': 'wq',
#              'age': 17,
#              'gender': 'man', 'hobby': ['ball', 'game', 'read']},
#             {'name': 'sk',
#              'age': 27,
#              'gender': 'woman'}]
# print(students[1]['gender'])
# print(students[0]['hobby'][0])

# 列表和字典相等的条件
# l1 = ['a', 'b']
# l2 = ['a', 'b']
# print(l1 == l2)  True 长度内容顺序一致则相等

# stu1 = {'name': 'wq',
#         'age': 17,
#         'gender': 'man'}
# stu2 = {
#     'age': 17,
#     'name': 'wq',
#     'gender': 'man'}
# print(stu1 == stu2) True key和value一致即相等，无序

# 遍历
stu1 = {'name': 'wq',
        'age': 17,
        'gender': 'man'}
# 不是列表类型，可以for循环遍历
# stu1.keys()
# stu1.values()
# # 转化为列表
# keys = list(stu1.keys())
# for i in stu1.items():
#     print(i)  # i是key value的元组
#     print(i[0], i[1])  # key和value
# for k, v in stu1.items():
#     print(k, v)  # 键值对
# 检测键是否存在
res = 'gender' in stu1.keys()
print(res)  # True
res = 17 in stu1.values()
res = 'man' in stu1
print(res)  # False 默认查找键
stu1.setdefault('name', 'micheal')  # 当name不存在时默认值生效 防止key不存在时报错
