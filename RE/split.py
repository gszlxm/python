import re

pattern = r'(\w+):(\d+)'
#s = '告别2018, 展望2019'
s = "张:1994,李:1995"
# 直接使用re调用
#l = re.findall(pattern, s)
#print(l)

regex = re.compile(pattern)

l = regex.findall(s, pos = 0, endpos = 10)
print(l)

l = re.split(r'\s+', "hello   nihao   world")
print(l)

s = "hello   nihao   world"

regex = re.compile(r'\s+')

l = regex.split(s, 1)
print(l)