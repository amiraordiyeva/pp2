import re
with open('row.txt') as file:
    text = file.read()
res = re.findall(r'\b[A-Z][a-z]+\b',text)
print (res)