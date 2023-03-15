import math
A, B, V = map(int, input().split())
day = (V - A) / (A - B)
total = math.ceil(day) + 1
print(total)