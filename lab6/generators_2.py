def even(n):
    even=[]
    for i in range(0, n+1):
        if i%2==0:
            even.append(i)
    yield even
ev=even(int(input()))
print(*next(ev))