while True:
    lenght = list(map(int, input().split()))
    if lenght == [0, 0, 0]:
        break
    lenght.sort()

    if (lenght[0] + lenght[1]) <= lenght[2]:
        print("Invalid")

    elif lenght[0] == lenght[1] and lenght[0] == lenght[2]:
        print("Equilateral")

    elif lenght[0] == lenght[1] or lenght[1] == lenght[2] or lenght[0] == lenght[2]:
        print("Isosceles")

    else:
        print("Scalene")

