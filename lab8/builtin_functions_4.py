import math
import time
def square_root(n,s):
     time.sleep(s/1000) 
     return math.sqrt(n)
num=float(input())
square=int(input())
ans=square_root(num,square)
print(f"Square root of {num} after {square} milliseconds is {ans}")