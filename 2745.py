N, B = input().split()
result = 0
count = 0
num = list("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
for n in N[::-1]:
    number_n = num.index(n)
    result += number_n * (int(B) ** count)
    count += 1

print(result)
