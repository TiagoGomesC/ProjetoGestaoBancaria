print("------------------------------------------------")
print("Bem Vindo ao BankPython! o Seu sistema bancário!🐍")
print("------------------------------------------------")
print("\n")

print("------------------------------------------------")
nome = input("Para iniciar digite o seu nome: ")
print("------------------------------------------------")
idade = float(input("Informe sua idade: "))
print("------------------------------------------------")

historico = []

if idade < 16:
    print("Infelizmente a idade mínima é de 16 anos.")
else:
    print(f"Seja bem-vindo, {nome}!")
    saldo = float(input("Informe um valor para o seu saldo/depósito inicial: "))

    if saldo <= 0:
        print("O valor do depósito deve ser maior que zero!")
    else:
        # Configuração do Cheque Especial
        tem_cheque_especial = input("Deseja ativar o Cheque Especial de R$ 500,00? (S/N): ").upper()
        if tem_cheque_especial == "S":
            limite_cheque = 500.00
            print("----------")
            print("Cheque especial de R$ 500,00 ativado!")
            print("----------")
        else:
            print("----------")
            limite_cheque = 0.00
            print("Cheque especial não ativado.")
            print("----------")

        print(f"Seu depósito de R$ {saldo:.2f} foi recebido!")

        while True:
            print("\n")
            print("Selecione a operação desejada:")
            print("1- Para Sacar Dinheiro")
            print("2- Para Depositar Dinheiro")
            print("3- Para visualizar suas últimas três operações")
            print("4- Para Sair")

            escolha = int(input("Digite a opção: ")) 

            if escolha == 1:
                valorSaque = float(input("Quanto você deseja sacar: "))
                taxa = 2.50
                custoTotal = valorSaque + taxa

                # Nova Regra: Saldo Disponível Total = Saldo Atual + Limite do Cheque
                saldo_disponivel_total = saldo + limite_cheque

                if custoTotal > saldo_disponivel_total:
                    print(f"Saldo e limite insuficientes!")
                    print(f"Saldo atual: R$ {saldo:.2f} | Limite Cheque Especial: R$ {limite_cheque:.2f}")
                    print(f"Total disponível para uso: R$ {saldo_disponivel_total:.2f}")
                    print(f"Custo necessário para este saque: R$ {custoTotal:.2f} (Saque + Taxa)")
                else:
                    saldo -= custoTotal # Deduz o valor do saldo (pode ficar negativo)
                    print(f"Seu saque de R$ {valorSaque:.2f} foi realizado com sucesso!")
                    print(f"Taxa de R$ {taxa:.2f} aplicada.")
                    
                    # Avisa o cliente se ele entrou no cheque especial
                    if saldo < 0:
                        print(f"Atenção: Você entrou no Cheque Especial!")
                        print(f"Saldo atual: R$ {saldo:.2f} (Utilizando R$ {abs(saldo):.2f} do limite)")
                    else:
                        print(f"Saldo atual: R$ {saldo:.2f}")
                    
                    historico.append(f"Saque: R$ {valorSaque:.2f} (Taxa: R$ {taxa:.2f})")

            elif escolha == 2:
                valorDeposito = float(input("Quanto você deseja depositar? "))
                if valorDeposito > 0:
                    saldo += valorDeposito # O depósito abate a dívida do cheque especial automaticamente
                    print(f"Seu depósito de R$ {valorDeposito:.2f} foi realizado!")
                    print(f"Saldo atual: R$ {saldo:.2f}")
                    historico.append(f"Depósito de R$ {valorDeposito:.2f}")
                else:
                    print("Valor de depósito inválido.")

            elif escolha == 3:
                print("\n--- Extrato Bancário (Últimas 3 operações) ---")
                ultimasOperacoes = historico[-3:]

                if len(ultimasOperacoes) == 0:
                    print("Nenhuma operação foi realizada!")
                else:
                    for operacao in ultimasOperacoes:
                        print(f"- {operacao}")
                
                print(f"Saldo Conta: R$ {saldo:.2f}")
                print(f"Limite Cheque Especial: R$ {limite_cheque:.2f}")
                print(f"Total Disponível para Saque: R$ {(saldo + limite_cheque):.2f}")

            elif escolha == 4:
                print("Obrigado por usar o BankPython, volte sempre!")
                break
            else:
                print("Opção Inválida! Tente novamente.")