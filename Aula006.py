# def Soma():
#     a = 2
#     b = 3
#     print(a+b)

# def Repetir(Repeticao):
#     VezesFoiRepetida = 0
#     for x in range(Repeticao):
#         VezesFoiRepetida+=1
#     print(f" Foi executado {VezesFoiRepetida} Vezes")

# UsuarioGrapete = int (input("Quantas vezes quer executar? "))

# Repetir(UsuarioGrapete)

# #OU
# Repetir(int(input ("Quantas vezes deseja executar? ")))

# # for in range(10):
# #   Soma()

# # Ouuu
# UsuarioGrapete =input("Quantas vezes vai executar? ")
# UsuarioGrapete = int(UsuarioGrapete)
# Repetir(UsuarioGrapete)

def Repetir(Repeticao:int, nome:str, MostrarMensagem=True):
    VezesFoiRepetida = 0
    for x in range(Repeticao):
        VezesFoiRepetida+=1
    if MostrarMensagem == True:
        print(f"{nome} Foi executado {VezesFoiRepetida} Vezes, Ou será que não?")

UsuarioGrapete =input("Quantas vezes vai executar? ")
UsuarioGrapete = int(UsuarioGrapete)
Repetir(UsuarioGrapete, "José", True)
