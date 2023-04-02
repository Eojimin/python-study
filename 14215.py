lenght = list(map(int, input().split()))
lenght.sort()

if (lenght[0] + lenght[1]) <= lenght[2]:
    lenght[2] = lenght[0] + lenght[1] - 1

print(sum(lenght))

