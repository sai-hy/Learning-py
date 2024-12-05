import re,os
os.system('cls')

# res=re.match('.\s[a-z]','  a11a1bca')
# res=re.match('.','a11a1bca')
# res=re.match(r'<(\w*)>\w*</\1>','<html>innerhtml</html>') #\数字 表示引用前面第几个括号的内容
# res=re.match(r'<(?P<l1>\w*)><(?P<l2>\w*)>.*</(?P=l2)></(?P=l1)>','<html><body>innerhtml</body></html>')
res=re.search('.\d','a11a1bca')

print('res',res.group())

lis=re.findall('3.','abc123adfbdf321234')
print(lis)

print(re.sub('你','我','你真真是个小可爱呀,你你',2)) #第4个参数是替换的次数，不写默认替换所有

print(re.split('','你真真是个小可爱呀,你你',4))
print(re.split('[2468]','12345678901234567890',4))

print(re.match(r'\\\\\\','\\\\\\123').group())