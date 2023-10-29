def squares(n):
    squares=[]
    for i in range(1, n+1):
        squares.append(i*i)
    yield squares
sq=squares(5)
print(*next(sq))