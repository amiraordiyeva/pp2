def sq(a,b):
    for i in range(a,b):
        yield i*i
gen = sq(3,12)
for i in range(12-3):
    print(next(gen))