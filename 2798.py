N, M = map(int, input().split())
card = list(map(int, input().split()))
result_list = []

for i in range(N-2):
    for j in range(1, N-1):
        if i >= j:
            continue
        for k in range(2, N):
            if j >= k:
                continue

            result = card[i] + card[j] + card[k]
            if result == M:
                result_list.append(result)
                break
            elif result < M:
                result_list.append(result)
        if result == M:
            break
    if result == M:
        break

print(max(result_list))
