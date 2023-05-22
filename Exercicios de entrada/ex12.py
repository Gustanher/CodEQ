
T = int(input("Digite T: "))
respostas = list(map(int, input().split()))
acertos = 0

for i in range(len(respostas)):
    if(respostas[i] == T):
        acertos = acertos + 1
print("acertos", acertos)