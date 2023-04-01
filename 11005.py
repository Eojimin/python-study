N, B = map(int, input().split())

num = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = []
count = 0
while True:
    new_num = N % B
    result.append(num[new_num])
    N = int(N / B)
    if N == 0:
        break

result.reverse()
print("".join(result))
