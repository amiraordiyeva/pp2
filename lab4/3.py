A=(set(input().split()))
B=(set(input().split()))
print(*sorted(set(A&B),key=int))

