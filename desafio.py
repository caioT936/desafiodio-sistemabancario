menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

==> """


saldo = 0

limite = 500

extrato = """========= EXTRATO =========
"""

numero_saques = 0

limite_saques = 3



while True:
        

    opcao = input(menu)

    if opcao == "d":
        print("Depósito \n")
        print(f"Esse é o saldo atual : R$ {saldo:.2f} \n")
        dep = float(input("Digite valor para depositar: ")) 
        if dep < 0:
            print("Error: Não existe depósito negativo")
            continue
        saldo += dep
        print(f'Agora seu saldo é: R$ {saldo:.2f}')
        extrato += f'Depósito --> R$ {dep:.2f}\n'


    elif opcao == "s":
        print("Saque \n")
        if numero_saques >= 3:
            print("Esgotou-se seu número de saques diário")
            continue
       
        saque = float(input("Digite valor para sacar (limite de R$500.00): "))
        if saque > saldo:
               print("\nError: Saque maior que o Saldo")
               continue
        elif saque > 500:
            print("\nError: Saque maior que R$ 500")
            continue
        elif saque < 0:
            print("Error: Não existe saque negativo!!!")
            continue
        numero_saques += 1
        saldo -= saque
        extrato += f"Saque --> R$ {saque:.2f}\n"



    elif opcao == "e":
        print()
        print(extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("============================")

    elif opcao == 'q':
        print("Saindo...")
        break
    
    else:
        print('Por favor, digite apenas os comandos mostrados abaixo!!!')
