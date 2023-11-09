import re
with open('row.txt') as file:
    text = file.read()
res = re.sub(r'[ ,.]', ':', text)
print (res)