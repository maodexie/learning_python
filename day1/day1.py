# -*- coding: utf-8 -*-
"""python练习第一天.

目标：复习string
"""
s = 'hi'
print(s[0])
print(s + ' there')

# 使用raw string，让反斜杠不生效
#print('c:\xie\python')
print(r'c:\xie\python')

# 使用"""，让字符串中的换行符生效
print("""
Usage:thingy [OPTIONS]
    -h
    -H hostname
""")
# 使用+号进行连接，使用*号进行重复
print(s*3+' there')
# 两个或者多个字符串常量相邻会自动连接在一起
print('Py''thon')
print('Put several strings withn parantheses'
    ' to have them joined together')

# 字符串也可以被切割，通过数组索引进行访问，indices可以是负数
word = 'Python'
print(word[-1])
print(word[-3])
print(word[2:5])
print(len(word))

# 字符串常量实际是一个str对象，可以通过str的构造函数来创建
text = str('i am str')
print(text)
# str的一些方法
# find(sub[,start])，返回找到的第一个substring
print(text.find('am'))
#--format,对字符进行格式化操作
#--split(sep=None,maxsplit=1),返回分割的字符列表
print(text.split(' '))
#--splitlines([keepends]),返回字符串中的按行分割的列表
text1 = """ab c\n\nde fg
hijk\rlmn\r\nopqrst
uvwxyz"""
print(text1.splitlines())