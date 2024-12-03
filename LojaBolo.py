Bolo = ["Farinha", "Ovo", "Leite", "Açúcar", "Baunilha"]
print (Bolo[2])
Bolo.append("Canela")
print (Bolo)
Bolo.remove("Açúcar")
print (Bolo)

NovoIgrediente = input ("Adicione seu igrediente do seu Bolo personalizado:")
Bolo.append(NovoIgrediente)
print ("Seu Bolo será preparado com:" + str (Bolo))
print ("Epero que goste do Nosso Produto, Volte Sempre ^^")