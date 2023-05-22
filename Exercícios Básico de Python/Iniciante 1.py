#1. Faça um Programa que mostre a mensagem "Olá, mundo!" na tela.
print("Olá, mundo!")
#2  Crie um programa que peça ao usuário para digitar um número e exiba o dobro desse número  
x = int(input("Digite um número: "))
print("O número digitado foi: ", x*2)
#3 Escreva um programa que peça ao usuário para digitar seu nome e exiba uma saudação personalizada
x = input("Digite seu nome: ") 
print("Olá, ", x)
#4 Faça um programa peça ao usuário para digitar dois números e exiba a soma deles. 
x = int(input("Digite um número: "))
y = int(input("Digite outro número: "))
print("A soma dos números é: ", x+y)
#5 Crie um programa que converta graus Celsius para Fahrenheit. O usuário deve digitar a temperatura em Celsius.
x = int(input("Digite a temperatura em Celsius: "))
print("A temperatura em Fahrenheit é: ", (x*1.8)+32)
#6 Escreva um programa que peça ao usuário para digitar um número e verifique se esse número é par ou ímpar.
x = int(input("Digite um número: "))
if x%2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")
#7 Faça um programa que calcule a área de um círculo. O usuário deve digitar o raio do círculo.
x = int(input("Digite o raio do círculo: "))
print("A área do círculo é: ", 3.14*(x**2))
#8 Crie um programa que peça ao usuário para digitar uma palavra e verifique se essa palavra é um palíndromo (ou seja, se pode ser lida da mesma forma da esquerda para a direita e vice-versa).
x = input("Digite uma palavra: ")   
if x == x[::-1]:
    print("A palavra é um palíndromo")
else:
    print("A palavra não é um palíndromo")  
#9 Faça um programa que exiba os números de 1 a 10 usando um loop (laço) de repetição.
for i in range(1,11):  
    print(i)
#10 Escreva um programa que peça ao usuário para digitar um número e exiba a tabuada desse número (multiplicação de 1 a 10).
x = int(input("Digite um número: "))
for i in range(1,11):
    print(x,"x",i,"=",x*i)

