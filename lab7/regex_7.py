import re
with open('row.txt') as file:
    text = file.read()
textt = text.split('_')
big = [word.capitalize() for word in textt]
res=''.join(big)
print (res)