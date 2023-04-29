
numGrenais = 0
greWins = 0
interWins = 0
empate = 0

while True:
    golsInter = int(input("Digite o número de gols do Inter: "))
    golsGre = int(input("Digite o número de gols do Gremio: "))
    opt = int(input("Novo grenal (1-sim 2-nao)"))

    numGrenais = numGrenais + 1
    if golsInter > golsGre:
        interWins = interWins + 1
    elif golsInter < golsGre:
        greWins = greWins + 1
    else:
        empate = empate + 1 

    if not opt == 1:
        break

if(greWins > interWins):
    vencedor = "Grêmio"
elif(greWins < interWins):
    vencedor = "Inter"
else:
    vencedor = "Não houve vencedor"
print(f"{interWins + greWins + empate} grenais")
print("Inter: ", interWins)
print("Gremio: ", greWins)
print("Empates: ", empate)

print("O time que venceu o maior número de grenais foi: ", vencedor)