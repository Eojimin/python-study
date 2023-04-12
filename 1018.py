N, M = map(int, input().split())
board = []
for n in range(N):
    line = list(input())
    board.append(line)

x = 0
y = 0
result = []
while y+8 <= N:
    count_B = 0
    count_W = 0
    for i in range(8):
        for j in range(8):
            if i % 2 == 0 and j % 2 == 0:
                if board[y + i][x + j] != 'B':
                    count_B += 1
                else:
                    count_W += 1
            elif i % 2 == 1 and j % 2 == 0:
                if board[y + i][x + j] == 'B':
                    count_B += 1
                else:
                    count_W += 1
            elif i % 2 == 0 and j % 2 == 1:
                if board[y + i][x + j] == 'B':
                    count_B += 1
                else:
                    count_W += 1
            elif i % 2 == 1 and j % 2 == 1:
                if board[y + i][x + j] != 'B':
                    count_B += 1
                else:
                    count_W += 1
    result += [count_W, count_B]
    x += 1
    if x+8 > M:
        x = 0
        y += 1

print(min(result))