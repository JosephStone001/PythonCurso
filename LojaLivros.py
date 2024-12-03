print("LOJA DE LIVROS DO SENAC")
print("==========================")

Valor_Carteira = input("Quanto você tem? $: ")
GeneroFavorito = input("Qual o seu Gênero Favorito? ")
CarrinhoCheio = False

print("===============================")

if int(Valor_Carteira) >= 30 and GeneroFavorito == "infantil":
    print("Comprou Livro Infantil")
    if int(Valor_Carteira) >= 32: 
        print("Livro Esporte")
    if int(Valor_Carteira) >= 40:
        print("Marca Texto")
    CarrinhoCheio = True

if int(Valor_Carteira) >= 45 and GeneroFavorito == "mitologia":
    print("Comprou Livro de Mitologia")
    if int(Valor_Carteira) >= 50: 
        print("Livro de Mitologia Grega")
    if int(Valor_Carteira) >= 55:
        print("Livro de Mitologia Nórdica")
    CarrinhoCheio = True

if int(Valor_Carteira) >= 60 and GeneroFavorito == "detetive":
    print("Comprou Livro Detetive")
    if int(Valor_Carteira) >= 62: 
        print("Livro Erótico")
    CarrinhoCheio = True

if int(Valor_Carteira) >= 80 and GeneroFavorito == "fantasia":
    print("Comprou Livro Fantasia")
    CarrinhoCheio = True

if CarrinhoCheio == False:
    print("Estoque indispovel para TODOS os Gêneros")