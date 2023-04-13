number = []

for i in range(5):
    num = int(input())
    number.append(num)

number.sort()
print(sum(number)//5)
print(number[2])