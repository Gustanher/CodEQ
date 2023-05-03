C = int(input())
R = 0
cont = 0
for i in range(C):
    N, M = map(int, input().split())
    R = N ** M
    while R != 0:
        R = R // 10
        cont += 1
    print(cont)
    cont = 0
