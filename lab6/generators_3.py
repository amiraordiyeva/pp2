def thfr(n):
    thfr=[]
    for i in range(n):
        if i%3==0 and i%4==0:
            thfr.append(i)
    yield thfr
thr=thfr(int(input()))
print(*next(thr))