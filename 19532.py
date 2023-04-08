a, b, c, d, e, f = map(int, input().split())


for y in range(-999, 1000):
    for x in range(-999, 1000):
        result_1 = a * x + b * y
        result_2 = d * x + e * y
        if result_1 == c and result_2 == f:
            print(x, y)
            break
    if result_1 == c and result_2 == f:
        break