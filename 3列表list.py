names = ['wq', 'ml', 'xm', 'lc', 'yx']  # 中括号表示列表
scores = [100, 23, 34, 12, 45]
# print(names[1])  # ml

# print(scores[-1])  # 访问倒数第一个元素  45

# 列表截取
l1 = names[0:3]  # 截取0-3的元素，包括下标0，不包括下标3 返回一个新的数组  ['wq', 'ml', 'xm']
l2 = names[:3]  # 开始索引不写从第一个开始截取  结束索引不写截取到最后一个  都不写等于复制列表

# 列表的增删改
names[2] = 'dm'  # 改
names.append('zs')  # 尾部增加
names.insert(0, 'ls')  # 0下标位置插入ls ['ls','wq',...]
del (names[2])  # 删除names的下标2的元素
del names[2]  # 也可以不用括号
del names[-1]  # 删除倒数第一个元素
names.remove('lc')  # 根据元素名删除 不存在则报错 若存在多个，删除第一个
s = names.pop()  # 删除最后一个 s为删除的元素 可以指定下标，弹出指定的元素 names.pop(1)

# 列表的排序 中文无法排序 数字在前，字母顺序，大写在前 永久排序会改变列表
names.sort()
names.sort(reverse=True)  # 倒序排序

# 临时排序，不改变原列表 返回临时排序的列表
newList = sorted(names)

# 列表翻转，倒序
names.reverse()

# 列表长度
length = len(names)

# 多维列表
names = [['ab', 'abc', 'ml'], ['ls,lsi'], ['xm', 'xh'], 1, 'abc']
# print(names[0][1])

# 返回元素的下标
# print(names.index(['ls,lsi']))  1

# 将列表元素追加到已有列表的结尾 逐个添加
names.extend(['haha', 'xixi', 'hehe'])

# 列表遍历
# names = ['lh', 'rain', 'jack', 'xx', 'pq', 'black']
# for name in names:
#     print(name + '你很棒')
# print('全体成员表现都很好')

# 转化成列表
# print(list(range(3, 10, 2)))  # 生成[3,10)之间的数字并转成列表 [3, 4, 5, 6, 7, 8, 9] [3, 5, 7, 9]  第三个参数表示步长

# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] 1-10的平方
l = []
for t in range(1, 11):
    l.append(t ** 2)
# 简写形式 后面遍历取值 前面对值做处理放入列表
newL = [t ** 2 for t in range(1, 11)]
# 最大最小求和
# print(min(l))
# print(max(l))
# print(sum(l))

# 通过索引来遍历列表 长度5 range可以取到4，正好最后一个元素的下标
# names = ['a', 'b', 'c', 'd', 'e']
# for t in range(0, len(names)):
#     print(names[t])

# 列表的复制
names = ['lh', 'zs', 'ls', 'ww', 'mk']
newNames = names[:] * 2  # newNames修改不改变原数组names *2表示复制多份
# newName = names  # newNames修改会改变原数组names 复制多份 newName=names*2
# newNames=names.copy()

# 合并列表
l1 = ['ll', 'mm', 'nn']
l2 = ['bb', 'cc', 'dd']
# l1.extend(l2)  # 第一种 会改变l1 把l2合并到l1尾部
l3 = l1 + l2  # 第二种，不改变原列表
