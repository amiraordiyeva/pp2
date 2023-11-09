import re
with open('row.txt') as file:
    text = file.read()
res = re.findall('ab{2,3}',text)
print (res)