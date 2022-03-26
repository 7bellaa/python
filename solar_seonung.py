N, M = map(int, input().split())
grid = [[10]*N for _ in range(M)]

TMP = [N, M]
tmp = min(TMP)
if tmp % 2 == 0:
    tmp //= 2
else:
    tmp = tmp//2 + 1

add = 0

for i in range(tmp):

    for j in range(M-i*2):
        grid[M-j-1-i][i] = j+1 + add

    for j in range(N-1-i*2):
        grid[i][j+1+i] = M+j+1 + add -(2*i)

    for j in range(M-1-i*2):
        if grid[j+1+i][N-i-1] != 10:
            continue
        grid[j+1+i][N-i-1] = M+N+j + add - (4*i)

    for j in range(N-2-i*2):
        if grid[M-1-i][N-j-2-i] != 10:
            continue
        grid[M-1-i][N-j-2-i] = (M*2)+N+j-1 + add - (6*i)

    add += (N+M-2)*2 - 8*i
    # print(add)


# for i in range(M):
#     for j in range(N):
#         print(grid[i][j], end = " ")
#     print('')


    
