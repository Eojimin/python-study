while True:
    a = int(input())
    if a < 0:
        break
    factor = []
    perfect = "1 "
    for i in range(1, a):
        if a % i == 0:
            factor.append(i)
    if sum(factor) == a:
        for i in factor[1:]:
            perfect += f"+ {i} "
        print(f"{a} = {perfect}")
    else:
        print(f"{a} is NOT perfect.")
