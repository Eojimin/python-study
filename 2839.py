N = int(input())

result = []
count = 0

five_coin = N // 5
three_coin = 0
while True:
    test = N - (5 * five_coin)
    if test % 3 == 0:
        three_coin = test // 3
        break
    else:
        five_coin -= 1

    if five_coin < 0:
        break

if five_coin <= 0 and three_coin == 0:
    print(-1)
else:
    print(five_coin + three_coin)