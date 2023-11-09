import re
with open('row.txt') as file:
    text = file.read()
res = re.findall(r'\b[a-z]+_[a-z]+\b',text)
print (res)