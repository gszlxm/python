import re

#re.I 忽略大小写
#s = "Hello World"
#pattern = r'hello'
#regex = re.compile(pattern, flags=re.I)

# re.A 只能匹配ascii
#s = "Hello 你好"
#pattern = r'\w+'
#regex = re.compile(pattern, flags=re.A)

#re.S 使.匹配\n
#s = """Hello World
#nihao China  
#"""
#pattern = r'.+'
#regex = re.compile(pattern, flags=re.S)

# M 匹配每行开头结尾

#"""
#pattern = r'world$'
#regex = re.compile(pattern, flags=re.M|re.I)
##

#s = """Hello World
#nihao China  
#"""
##X给正则加注释
s = 'abcdefghijk'
pattern = r'''(ab) # 第一行分组
\w+   #任意字符串
(?P<dog>ef)  #dog组
'''
regex = re.compile(pattern, flags=re.X)

l = regex.findall(s)
print(l)



