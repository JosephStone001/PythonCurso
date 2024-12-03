#TRUQUES !!

# TRUQUES COM PYTHON 
Numero = 0
Numero = 20

# avançar uma casa a frente com Int
Numero-=1 
Numero = Numero+1 

#Avanço utilizando outra variavel
AVancar = 3
Numero = Numero+AVancar
VariavelNova = Numero+AVancar

#Recorte de Stirng 
String_ = "AlunoEAluna"
String_[4:]
String_[:4]
String_[1:6]

#Conversão de string para lista
ListaDeNomes = "Luana;Raphael;Natalia;Lucas"
ListaDeNomes = ListaDeNomes.split(";")
print(ListaDeNomes[1])

variavel_teste = ["primeiro","Segundo","Terceiro"]
for i in variavel_teste :
    print(i)
print("Acabou!")

# Crie um laço que execute 10 vezes e sempre que
# executar miltiple a variavl de "taxa" por 1.2

taxa = 0.2
for T in range (0,10):
    print ("Executou" + str (T))
    taxa = taxa*1.2
print(taxa)

# Crie um Laço que faça um laço de repetição em
# uma lista de INT chamada valores e some
# cada um dos valores por 4

Valores = [2,5,6,7,8]


for z in Valores:
    print (z+4)

for ComData in range(0,len(Valores)-1):
    print(ComData+4)

    
Quantidade = 0
while Quantidade < len(Valores)-1:
    print(Valores[Quantidade]+4)
    Quantidade+=1

Escala = 2
ValorEscala = []

for ExtraEscala in range (0,9):
    ValorEscala.append(Escala)
    Escala = Escala + 2
    print (ValorEscala)


PontosDeVida = 50
DanoPorTurnos = []

print ("Você foi emboscado, tente sobreviver")

while (PontosDeVida > 1):
    DanoPorTurnos.append(PontosDeVida)
    print ("Você Levou um tiro de Flecha, perdeu 10 pontos de vida!")
    print (DanoPorTurnos)
    PontosDeVida = PontosDeVida - 10


print ("Você Morreu, Fim de Jogo")



















