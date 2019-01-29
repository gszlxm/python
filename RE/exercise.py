import re, sys



def get_address(port):
    #提取一段内容
    with open('1.txt') as f:
        fr = f.read()
    pattern = r"\b%s\b.*?\n{2}"%port
    regex1 = re.findall(pattern,fr,flags=re.S)
    if not regex1:
       return 'NOT Found'
    s1 = ' '.join(regex1)
    print(s1)
    pattern1 = r'(\baddress is (\w+\.){2}\w+(\.\d+/\d+)?)'
    regex2 = re.findall(pattern1, s1)
    if not regex2:
        return "Unknown"
    address = []
    for i in regex2:
        address.append(i[0])
    return address
#def get_address(port):
#    f = open("1.txt")
#
#    while True:
#        data = ''
#        for line in f:
#            if line != '\n':
#                data += line
#            else:
#                break 
#        #已经到文件的结尾
#               
#        if not data:
#            return  'Not Found'
#
#        #匹配首字母单词
#        try:
#            PORT = re.match(r'\S+', data).group()
#        except Exception as e:
#            print(e)
#            continue
#        if PORT == port:
#            #pattern = r'address is ([0-9a-f]){4}\.[0-9a-f]{4}[0-9a-f]{4}' 
#            pattern = r"address is ((\d{1,3}\.){3}d{1,3}/\d+|Unknow)"
#            address = re.search(pattern,data)group()
#            retunrn address
#
if __name__ == "__main__":
    port = sys.argv[1]
    addr = get_address(port)
    print(addr)

        