num1 = int(input())
num2 = int(input())
num3 = int(input())
if num1 < num2 and num1 < num3:
    min= num1
if num2 < num1 and num2 < num3:
    min= num2
if num3 < num1 and num3 < num2:
    min= num3
print(min)