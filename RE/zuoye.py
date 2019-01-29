#作业: 1. 熟记正则表达式元字符
#     2. 使用regex对象复习re模块调用的函数
#     3. 找一个文档, 使用正则表达式匹配:
#     [1] 所有以大写字母开头的单词
#     [2] 所有的数字, 包含整数, 小数, 负数, 分数, 百分数 

import re

pattern = '\b[A-Z]+\w*'
fr= open("day01.txt")
f = fr.read()
regex = re.findall(pattern, f)
print(regex)

#pattern = r'\d+\.\d+|-\d+|\d+/\d+|\d+\%|\d+'
#pattern = r'\d+/\d+'
pattern = r'-?\d*\.?/?\d+%?'
regex = re.findall(pattern, f)
print(regex)

fr.close()