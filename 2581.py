a = int(input())
b = int(input())
sosu = []
number = list(range(a, b+1))
for i in number:
    count = 0
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            count += 1
    if count == 0:
        sosu.append(i)

if len(sosu) == 0:
    print(-1)
else:
    print(sum(sosu))
    print(min(sosu))
