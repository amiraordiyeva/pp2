col1 = int(input())
row1 = int(input())
col2 = int(input())
row2 = int(input())
if col1%2!=0:
    if row1%2!=0:
        field1 = 0
    else:
        field1 = 1
if col1%2==0:
    if row1%2!=0:
        field1 = 1
    else:
        field1 = 0
if col2%2!=0:
    if row2%2!=0:
        field2 = 0
    else:
        field2 = 1
if col2%2==0:
    if row2%2!=0:
        field2 = 1
    else:
        field2 = 0
if field1 == field2:
    print("YES")
else:
    print("NO")