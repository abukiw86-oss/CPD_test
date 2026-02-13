n,h = map(int, input().split())
a = list(map(int, input().split()))

sum = 0
for i in a:
    if i <= h:
        sum+=1
    else:
        sum+=2

print(sum)