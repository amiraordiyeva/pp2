import re
with open('row.txt') as file:
    text = file.read()
res = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
print (res)