def p(s):
     t=''.join(reversed(s))
     if t==s:
         return True
     else:
         return False
ans=p('abba')
print(ans)
