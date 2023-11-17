import math
def calculate(line):
     upper=0
     lower=0

     for i in range(0, len(line)):
         if line[i].isupper():
             upper+=1
         if line[i].islower():
             lower+=1
     return upper,lower


str='AbcRda'
res=calculate(str)
print(res)