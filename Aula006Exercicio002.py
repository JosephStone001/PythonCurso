n1=int(input("Insira o primeiro Inteiro desejado: "))
n2=int(input("Insira o segundo Inteiro desejado: "))

def Multiplicacao(n1:int, n2:int):
   Resultado = n1*n2
   if Resultado >= 500:
    print("O resultado da sua operação é Maior do que 500")
   else :
    print("O resultado da sua operação é Menor do que 500")

Multiplicacao(n1,n2)