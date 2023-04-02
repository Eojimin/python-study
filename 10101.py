angle = []
for i in range(3):
    N = int(input())
    angle.append(N)

if sum(angle) != 180:
    print("Error")

elif angle[0] == 60 and angle[1] == 60:
    print("Equilateral")

elif angle[0] == angle[1] or angle[1] == angle[2] or angle[0] == angle[2]:
    print("Isosceles")

else:
    print("Scalene")