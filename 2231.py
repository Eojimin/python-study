N = input()
if int(N) > 20:
    count = len(N) * 9
elif int(N) >= 10:
    count = (len(N)-1) * 9
else:
    count = 0

num_list = []
new_N = int(N) - count

def fun(new_N):
    num = str(new_N)
    result = int(num)
    for i in num:
        result += int(i)

    if result == int(N):
        num_list.append(int(num))
        return
    else:
        if int(num) < int(N):
            fun(int(new_N)+1)
        else:
            num_list.append(0)
            return

if int(N) < 10:
    if int(N) % 2 == 0:
        print(int(N)//2)
    else:
        print(0)
else:
    fun(new_N)
    print(num_list[0])


