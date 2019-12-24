# coding=utf-8
"""day2.py
学习python列表
"""
# list的方法
fruits = ['apple','orange','banana','pear','kiwi','apple']
#--append 向列表后添加一个项目
fruits.append('pen')
#--extend 

#--insert 在指定index后插入一个项目
fruits.insert(2,'apple pen')
#--sort 对list进行排序
fruits.sort()
print(fruits)
#--pop 从列表最后弹出一个元素，同时返回相应的元素
print(fruits.pop())
#--count 返回与目标内容相等元素个数
print(fruits.count('apple'))
#--index 返回目标元素的索引
print(fruits.index('apple'))

# list as stash
stash = [2,3,4,5]
stash.append(6)
stash.append(7)
print(stash)
stash.pop()
print(stash)

# list as a queue
from collections import deque
queue = deque(['Eric','John','Michale'])
queue.append('Terry')
queue.append('Gramham')
queue.popleft()
print(queue)
queue.popleft()
print(queue)

# list inference
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

squares1 = list(map(lambda x: x**2,range(10)))
suqares2 = [x**2 for x in range(10)]
print(squares1)
print(suqares2)

matrix = [(x,y) for x in [1,2,3] for y in [2,3,4] if x!=y]
print(matrix)
