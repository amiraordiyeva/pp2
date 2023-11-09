import re
with open('row.txt') as file:
    text = file.read()
res = re.findall('[A-Z][^A-Z]*', text)
print (res)