# coding=utf-8
"""day2.py
learning python list
"""
fruits = ['apple','orange','banana','pear','kiwi','apple']
#--append
fruits.append('pen')
#--extend
#--insert
fruits.insert(2,'apple pen')
#--sort
fruits.sort()
print(fruits)
#--pop
print(fruits.pop())
#--count
print(fruits.count('apple'))
#--index
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
