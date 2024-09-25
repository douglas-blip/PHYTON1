maior = -999999999
menor = 999999999
print ("Digite 0 para saida:")
ct = 0
while True:
 valor = int(input("Digite o valor:"))
 if valor == 0:
     break
ct = ct + 1
 if  valor < menor:
     menor = valor
if   valor > maior:
     maior = valor

media = soma / ct
print ("A quantidade e:",ct)
print("A media e:",media)
print("O maior valor e:",maior)
print("O menor valor e:",menor)