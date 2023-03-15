a = int(input())
room = []
for i in range(a):
    H, W, N = map(int, input().split())
    floor = N % H
    number = int(N / H) + 1
    if floor == 0:
        floor = H
        number -= 1
    room.append(floor*100+number)
for i in room:
    print(i)
