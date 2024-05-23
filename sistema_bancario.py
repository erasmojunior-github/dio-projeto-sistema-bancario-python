menu_inicial = """

Usuário, por favor, selecione uma das opções abaixo:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
LIMITE_POR_SAQUE = 500
NUMERO_MAX_SAQUES = 3
num_saques = 1
movimentação = 0

ligar_sistema = True

while ligar_sistema:
    opção = input(menu_inicial)
    
    if opção == "d":
        
        deposito = float(input("Informe o valor do depósito:\n"))
        saldo += deposito
        movimentação = movimentação + 1
        
    elif opção == "s":
        
        if num_saques <= NUMERO_MAX_SAQUES:
            
            saque = float(input("\nInforme o valor do saque:\n"))
            
            if saque > 0:
                
                if saldo > saque:
                    
                    if saque < LIMITE_POR_SAQUE:
                        saldo -=saque
                        num_saques = num_saques + 1
                        movimentação = movimentação + 1
                        
                    else:
                        print("\nOperação falhou! O valor do saque excede o limite.")
                
                else:
                     print("\nOperação falhou! Você não tem saldo suficiente.")
                
            else:
                print("\nOperação falhou! O valor informado é inválido.")
            
        else:
            print("\nOperação falhou! Número máximo de saques excedido.")
            
    elif opção == "e":
        
        extrato = "EXTRATO"
        print("\n")
        print(extrato.center(20,"="))
        
        if movimentação == 0:
            print("\nNão foram realizadas movimentações.\n")
        else:
            print(f"\nSaldo: {saldo:.2f}\n")
            
        print("="*20)
        
    elif opção == "q":
        ligar_sistema = False
        
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        
print("\nOperações encerradas! Volte sempre.")