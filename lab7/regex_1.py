import re
with open('row.txt') as file:
    text = file.read()
res = re.findall('a.*b',text)
print (res)