import re
with open('row.txt') as file:
    text = file.read()
res = re.findall(r'([a-z0-9])([A-Z])', text)
big='_'.join(map(str.lower,res))
print (big)

