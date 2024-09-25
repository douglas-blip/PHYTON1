def Ex1():
    ct = 0
    for numero in range(0,11,1):
        ct = ct + 1
        print(numero)
    else:
        print('Encerrou o programa')
    print('Numeros contados:',ct)

def Ex2():
    print('Numeros naturais na horizontal:')
    for i in range(0,11,1):
        if i == 10:
         print(i, end=".")
        else:
         print (i, end=",")
    print("\nEncerrou o programa")

Ex2()

def Ex3():
    print('Numeros naturais pares:')
    for par in range(0,13,2):
     print(par)
    print('\nEncerrou o programa')

Ex3()

def Ex4():
    print('Numero naturais impares:')
    for impar in range(1,14,2):
        print(impar)
    print("\nEncerrou o programa")

Ex4()

def Ex5():
    print("Numeros naturais na ordem decrescente")
    for i in range(7,0,-1):
        print(i)
    print('\nEncerrou o programa')

Ex5()

def Ex6():
    valor_inicial = int(input("Digite o valor:"))
    valor_final = int(input('Digite o valor:'))
    for i in range(valor_inicial,valor_final+1,1):
     print(i)

Ex6()