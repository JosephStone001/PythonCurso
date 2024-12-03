ContaBancaria001 = 200
ContaBancaria002 = 500
QuantidadeDeCredito = 100
Imposto001 = 300

print (ContaBancaria001 > ContaBancaria002)
print("===============")

if ContaBancaria001 > ContaBancaria002:
    print ("Conta Bancaria 001 é maior")
else:
    print("Conta Bancaria 002 é maior")

if Imposto001 > ContaBancaria001:
    print("Você está despejado Devedor 001!!")
if ContaBancaria001+QuantidadeDeCredito>Imposto001 or ContaBancaria001+QuantidadeDeCredito == Imposto001 and Imposto001>ContaBancaria001:
    print("Não Aceito Crédito Devedor 001!!!")

else:
    print("Pague o Aluguel Devedor001!!")

if Imposto001 > ContaBancaria002:
    print("Você está despejado Devedor 002!!")
if ContaBancaria002+QuantidadeDeCredito<Imposto001 or ContaBancaria002+QuantidadeDeCredito >= Imposto001 and Imposto001>ContaBancaria002:
    print("Não Aceito Crédito Devedor 002!!!")

else:
    print("Pague o Aluguel Devedor002!!")

