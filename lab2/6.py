num1 = int(input())
num2 = int(input())
num3 = int(input())
if num1==num2 or num1==num3 or num2==num3:
    if num1==num2 and num2==num3:
        print("3")
    else:
        print("2")
if num1!=num2 and num1!=num3 and num2!=num3:
    print("0")