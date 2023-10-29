def down(n):
    for i in reversed(range(n)):
        yield i
d=down(7)
for i in range (7):
    print(next(d))