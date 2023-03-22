x, y, w, h = map(int, input().split())
distance = []

distance.append(abs(0-x))
distance.append(abs(0-y))
distance.append(abs(x-w))
distance.append(abs(y-h))
print(min(distance))