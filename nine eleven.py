ct_masc = 0
ct_fem = 0
menor = 3
maior = 0
print("Digite 0 para sair")
while True:
    altura = float(input("Altura:"))
    if  altura == 0:
     break
    genero = str(input("[m] para masculino\n[f] para feminino:\nOpçao:"))
    if altura > maior:
       maior = altura
    if altura < menor:
       menor = altura
    if genero == "m":
       ct_masc += 1
    else:
        ct_fem += 1
print("Maior altura:",maior)
print("Menor altura",menor)
print("Quantidade de homens:",ct_masc)
print("Quantidade de mulheres:",ct_fem)
