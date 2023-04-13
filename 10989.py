N = list(map(int, input()))

N.sort(reverse=True)

N_str = list(map(str, N))
print(''.join(N_str))