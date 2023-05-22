
N = int(input())
v = list(map(int, input().split()))
arq = 0;
imp = 0;
for i in range(0, N):
    if (v[i] == 0):
        arq += 1
    elif (v[i] == 1):
        imp += 1
    else:
        print("Erro")
        break

if (arq > imp):
    print("acusacao arquivada")
elif (imp > arq):
    print("impeachment")
else:
    print("empate")