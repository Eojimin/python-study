N = int(input())
dot = 2
count = 1
result = dot
for i in range(N):
    result += count
    count *= 2

print(result**2)