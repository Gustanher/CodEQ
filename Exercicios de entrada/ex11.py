
p = int(input("Digite P: ")) 
n = int(input("Digite N: "))
alturas = list(map(int, input().split()))
cano_anterior = alturas[0] 
for i in range(1, n):
    cano = alturas[i]
    if abs(cano - cano_anterior) > p: 
        print("GAME OVER")
        break 
    cano_anterior = cano    
else:
    print("YOU WIN") 