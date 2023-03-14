score_list = []
count_list = []
total = 0
count = 0
while True:
    try:
        a, b, c = input().split()
        if c != "P":
            count += float(b)
            score_list.append(c)
            count_list.append(float(b))

    except:
        break
for i in range(len(count_list)):
    if score_list[i] == "A+":
        total += count_list[i] * 4.5
    elif score_list[i] == "A0":
        total += count_list[i] * 4.0
    elif score_list[i] == "B+":
        total += count_list[i] * 3.5
    elif score_list[i] == "B0":
        total += count_list[i] * 3.0
    elif score_list[i] == "C+":
        total += count_list[i] * 2.5
    elif score_list[i] == "C0":
        total += count_list[i] * 2.0
    elif score_list[i] == "D+":
        total += count_list[i] * 1.5
    elif score_list[i] == "D0":
        total += count_list[i] * 1.0
    elif score_list[i] == "F":
        total += 0
print(round(total/count, 6))
