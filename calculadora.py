

menu='''
MENU
====
1-  Somar.
2-  Subtrair.
3-  Multiplicar.
4-  Dividir.

Escolha: 
'''

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        soma_x = 0
        soma_y = 0
        subtrair_x = 0
        subtrair_y = 0
        multiplicar_x = 0
        multiplicar_y = 0
        dividir_x = 0
        dividir_y = 0
        god = soma_x + soma_y + subtrair_x + subtrair_y + multiplicar_x + multiplicar_y + dividir_x + dividir_y
        god = str(input(msg))
        if god.isnumeric():
            valor = int(god)
            ok = True
            
        else:
            print("ERRO. POR FAVOR DIGITE UM NÚMERO!")
        if ok:
            break
    return valor

 
    
########################################
#1 - SOMAR 
def somar():
    soma_x= leiaInt("Digite um número:")
    soma_y= leiaInt("Digite outro número:")

    print("A soma dos numeros", soma_x, "e", soma_y, "é igual a:", soma_x+soma_y)

########################################
#2 - SUBTRAIR
def subtrair():
    subtrair_x= leiaInt("Digite um número:")
    subtrair_y= leiaInt("Digite outro número:")

    print("A subtração dos numeros", subtrair_x, "e", subtrair_y, "é igual a:", subtrair_x-subtrair_y)
    

########################################
#3 - MULTIPLICAR
def multiplicar():
    multiplicar_x= leiaInt("Digite um número:")
    multiplicar_y= leiaInt("Digite outro número:")

    print("A multiplicação dos numeros", multiplicar_x, "e", multiplicar_y, "é igual a:", multiplicar_x*multiplicar_y)
    

########################################
#4 - DIVIDIR
def dividir():
    try:
        dividir_x = leiaInt("Digite um número:")
        if dividir_x == 0:
            print("Não é possível dividir zero! Por favor digite outro número.")
            return dividir()
        dividir_y = leiaInt("Digite outro número:")
        print("O numero", dividir_x , "dividido por", dividir_y , "é igual a:", dividir_x/dividir_y)
        
    except ZeroDivisionError:
        print("Não é possível dividir um número por zero.")
        return dividir()
        
        

###PROGRAMA PRINCIPAL#######
############################


while True:
    escolha = input(menu)
    if escolha == '1':
        somar()
    if escolha == '2':
        subtrair()
    if escolha == '3':
        multiplicar()
    if escolha == '4':
        dividir()


somar()
subtrair()
multiplicar()
dividir()
