
linhas = 2
colunas = 9
DDD = [[0 for j in range(colunas)] for i in range(linhas)] #peguei isso aqui da internet kk
entrada = int(input("Insira o DDD: "));
DDD[0][0] = 61;
DDD[1][0] = "Brasília";
DDD[0][1] = 71;
DDD[1][1] = "Salvador";
DDD[0][2] = 11;
DDD[1][2] = "São Paulo";
DDD[0][3] = 21;
DDD[1][3] = "Rio de Janeiro";
DDD[0][4] = 32;
DDD[1][4] = "Juiz de Fora";
DDD[0][5] = 19;
DDD[1][5] = "Campinas";
DDD[0][6] = 27;
DDD[1][6] = "Vitória";
DDD[0][7] = 31;
DDD[1][7] = "Belo Horizonte";
DDD[0][8] = 55;
DDD[1][8] = "Santa Maria"; 
i = 0
while( i < colunas):
    if(entrada == DDD[0][i]):
        print(DDD[1][i])
        break
    elif(i+1 == colunas):
        print("DDD não cadastrado")
    i = i+1


