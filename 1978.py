a = int(input())
b = list(map(int, input().split()))
decimal = []
for i in b:
    count = 0
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            count += 1
    if count == 0:
        decimal.append(i)
print(len(decimal))