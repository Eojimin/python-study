apartment = []
floor_0 = list(range(1, 15))
apartment.append(floor_0)
for i in range(14):
    new_floor = []
    for j in range(14):
        new_floor.append(sum(apartment[i][:j+1]))
    apartment.append(new_floor)

a = int(input())
for i in range(a):
    k = int(input())
    n = int(input())
    print(apartment[k][n-1])
