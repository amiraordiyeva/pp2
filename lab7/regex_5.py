import re
with open('row.txt') as file:
    text = file.read()
res = re.search('a.*?b$',text)
print (res)