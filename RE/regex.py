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
