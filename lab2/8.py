col1 = int(input())
row1 = int(input())
col2 = int(input())
row2 = int(input())
if col2>col1+1 or col2<col1-1 or row2>row1+1 or row2<row1-1:
    print("NO")
else:
    print("YES")