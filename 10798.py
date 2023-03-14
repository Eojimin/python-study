total = []
result = ""
for i in range(5):
    a = list(input())
    b = len(a)
    for j in range(15 - b):
        a.append("")
    total.append(a)

for i in range(15):
    for j in range(5):
        result += total[j][i]

print(result)