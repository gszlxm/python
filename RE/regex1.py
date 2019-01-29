import re

pattern = r'(ab)cd(?P<dog>ef)'

regex = re.compile(pattern)

#获取match对象
obj = regex.search('abcdefghjik',pos=0,endpos=8)

#obj属性变量
print(obj.pos) #目标字符串的开始位置
print(obj.endpos) #目标字符串的结束位置 (向后错一 即左开右闭)
#python 右闭即字符串向后取一, 方便编写解释执行器

print(obj.re)  #正则表达式
print(obj.string) #目标字符串

print(obj.lastgroup) #最后一组的名称, 若是最后一组没有名称则打印的是None
print(obj.lastindex) #最后一组是第几组

print('===================================')

#obj方法
print(obj.span())  #匹配内容的起止位置
print(obj.start()) #匹配内容的开始位置
print(obj.end())  #匹配内容的结束位置

print(obj.group())  #整体匹配内容
print(obj.group(1)) #第一组内容
print(obj.group(2)) #第二组内容
print(obj.group('dog')) #dog组内容

#子组有意义的前提是整体匹配到内容
print(obj.groupdict()) #获取捕获组字典, 若没有则是空字典
print(obj.groups()) #获取所有子组对应内容
