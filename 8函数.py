# def 定义一个函数
# def hello(name):  # 形参
#     print('Hello ' + name)
# hello('wq')  # 实参

# 默认值 必须放在后面
# def add(a, b=2, c=3):
#     return a + b  # 返回值
# res = add(1, 1)
# res1 = add(a=1, b=2)  # 关键字参数
# print(res)
# print(add(2))
# print(add(1, c=1))  # 使用关键字参数 就不用指定b的值了，会使用默认值
# None 类型NoneType 什么都没有

# 位置参数  关键字参数
# print('hello', end='')
# sep关键字参数 表示用什么分隔符连接
# print('hello', 'world', 'wq', sep='|', end='')

# 变量的作用域
# def test():
#     name = 'wq'
#     print(name)
# test函数外无法使用name
# name = 'globalName'
# def test():
#     # name = 'localName'
#     # print(name)  # localName
#     global name  # 表示使用全局变量name
#     name = 'wq'
#     print(name)
# test()
# print(name)  # globalName  wq

# 动态参数 可变个数参数 n表示一个参数 会把参数组建成一个元组给n  *n参数个数不定，0-多个
# def test(*n):
#     # def test(a,*n): 第一个参数给a，后续参数放进元组给n
#     for i in n:
#         print(i)

# 导入一个模块 可以起别名
# import moduleTest as mt
# mt.test1()
# # 导入一个模块中的某一个函数 可以用,隔开导入多个函数 并可以通过as起别名，防止重名
# from moduleTest import test2, test1 as t
# test2()  # 不用带模块名.了
# t()
# 导入模块中的所有方法 除了import moduleTest之外 不推荐
from test import *


# 函数的递归
# def sumF(n):
#     if n == 1:
#         return 1
#     he = sumF(n - 1) + n
#     return he
# print(sumF(5))

# 练习
# def make_shirt(size=200, mark='i love python'):
#     print('T恤的尺码是', size, '字样是', mark)
# make_shirt(185, 'wq')
# make_shirt(size=185, mark='wq')
# make_shirt(size=190)

# def make_album(name, album_name, count=0):
#     d = {'name': name, 'album_name': album_name}
#     if count > 0:
#         d['count'] = count
#     return d
# print(make_album('wq', '人生', 6))
# print(make_album('mc', '舞曲'))
