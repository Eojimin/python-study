list_x = []
list_y = []
for i in range(3):
    x, y = map(int, input().split())
    list_x.append(x)
    list_y.append(y)

before_x = list_x[0]
before_y = list_y[0]

if before_x in list_x[1:]:
    for i in range(2):
        list_x.remove(before_x)

if before_y in list_y[1:]:
    for i in range(2):
        list_y.remove(before_y)

new_x = list_x[0]
new_y = list_y[0]
print(new_x, new_y)