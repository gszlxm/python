import re

#pattern = r"\d+"
#s = '2018年中国经济增长6.6%, 与2017年基本持平, 2019面临很多困难'

#it = re.finditer(pattern, s)

#match对象属性
#print(dir(next(it)))
#'end', 'endpos', 'expand', 'group', 'groupdict', 
#'groups', 'lastgroup', 'lastindex', 'pos',
#'re', 'regs', 'span', 'start', 'string'


#for x in it:
#    print(x.group())

#try:
#    obj = re.fullmatch(r'\w+', 'hello1988')
#    print(obj.group())
#except AttributeError as e:
#    print(e)    
#
obj = re.match(r'[A-Z]\w+', "Hello world")
print(obj.group())
#
#s = '2018年中国经济增长6.6%, 与2017年基本持平, 2019面临很多困难'
#obj = re.search(r'\d+', s)
#print(obj.group())

#regex = re.compile(r'[A-Z]\w+')
#s = "Hello world"
#l = regex.match(s,0, 10)
#print(l.group())