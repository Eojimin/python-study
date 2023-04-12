N = int(input())
number = []

for i in range(N):
    new_num = int(input())
    number.append(new_num)

for n in range(N):
    min_num = min(number)
    print(min_num)
    number.remove(min_num)