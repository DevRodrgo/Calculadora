print("##########CALCULADORA############")

operacao = input("digite a operação desejada(soma, sub, mult, divisao): ")
num1 = input("Digite seu primeiro numero:") 
num2 = input ("Digite seu segundo numero:")

if operacao == "soma":
	resultado =  int(num1) + int(num2)
if operacao == "sub":
	resultado = int(num1) - int(num2)
if  operacao == "mult":
	resultado = int(num1) * int(num2)
if operacao == "divisao":
	resultado = int(num1) / int(num2)
else:
	Resultado = "NAO FOI POSSIVEL CALCULAR"

print("O resultado da operacao é: " + str(resultado))
