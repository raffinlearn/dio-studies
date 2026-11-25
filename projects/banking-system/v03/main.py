from datetime import date
from math import isfinite

from clientes import PessoaFisica
from contas import ContaCorrente
from transacoes import Saque, Deposito
from sistema import carregar_dados, salvar_dados, buscar_cliente, proximo_numero_conta


def solicitar_cpf():
    while True:
        cpf = input("CPF: ").strip()
        cpf = cpf.replace(".", "").replace("-", "")

        if len(cpf) == 11 and cpf.isascii() and cpf.isdigit():
            return cpf

        print("CPF inválido.")


def criar_cliente(clientes):
    print("\n=== CADASTRO DE CLIENTE ===")

    cpf = solicitar_cpf()

    if buscar_cliente(clientes, cpf):
        print("CPF já cadastrado.")
        return

    nome = input("Nome completo: ").strip()

    while True:
        try:
            nascimento = input("Data de nascimento (AAAA-MM-DD): ")

            data_nascimento = date.fromisoformat(nascimento)

            if data_nascimento > date.today():
                print("Data de nascimento inválida.")
                continue

            break

        except ValueError:
            print("Informe uma data válida.")

    telefone = input("Telefone: ").strip()
    endereco = input("Endereço: ").strip()

    if not nome or not endereco:
        print("Nome e endereço são obrigatórios.")
        return

    cliente = PessoaFisica(
        nome=nome,
        data_nascimento=data_nascimento,
        cpf=cpf,
        telefone=telefone,
        endereco=endereco,
    )

    clientes.append(cliente)
    salvar_dados(clientes)

    print("Cliente cadastrado com sucesso!")


def criar_conta(cliente, clientes):
    numero = proximo_numero_conta(clientes)

    conta = ContaCorrente.nova_conta(cliente, numero)
    cliente.adicionar_conta(conta)

    salvar_dados(clientes)

    print("\nConta criada com sucesso!")
    print(conta)


def listar_contas(cliente):
    if not cliente.contas:
        print("Nenhuma conta cadastrada.")
        return

    for conta in cliente.contas:
        print("-" * 35)
        print(conta)


def selecionar_conta(cliente):
    if not cliente.contas:
        print("Cliente não possui contas.")
        return None

    listar_contas(cliente)

    try:
        numero = int(input("\nNúmero da conta: "))

    except ValueError:
        print("Número de conta inválido.")
        return None

    for conta in cliente.contas:
        if conta.numero == numero:
            return conta

    print("Conta não encontrada.")
    return None


def solicitar_valor():
    try:
        entrada = input("Valor: R$ ").replace(",", ".")
        valor = float(entrada)

        if not isfinite(valor) or valor <= 0:
            print("O valor deve ser positivo e finito.")
            return None

        return valor

    except ValueError:
        print("Valor inválido.")
        return None


def realizar_operacao(cliente, conta, clientes, tipo):
    valor = solicitar_valor()

    if valor is None:
        return

    transacao = tipo(valor)

    sucesso = cliente.realizar_transacao(conta, transacao)

    if sucesso:
        salvar_dados(clientes)


def exibir_extrato(conta):
    print("\n=== EXTRATO BANCÁRIO ===")
    print(conta.mostrar_extrato())
    print("-" * 35)
    print(f"Saldo atual: R$ {conta.saldo:.2f}")


def menu_conta(cliente, conta, clientes):
    while True:
        print(f"""
===================================
           CAIXA ELETRÔNICO
===================================
Titular: {cliente.nome}
Conta: {conta.numero}
Saldo: R$ {conta.saldo:.2f}

[1] Depositar
[2] Sacar
[3] Extrato
[0] Voltar
""")

        opcao = input("Opção: ").strip()

        match opcao:
            case "1":
                realizar_operacao(cliente, conta, clientes, Deposito)

            case "2":
                realizar_operacao(cliente, conta, clientes, Saque)

            case "3":
                exibir_extrato(conta)

            case "0":
                break

            case _:
                print("Opção inválida.")


def menu_cliente(cliente, clientes):
    while True:
        print(f"""
===================================
          MENU DO CLIENTE
===================================
Bem-vindo, {cliente.nome}!

[1] Criar conta corrente
[2] Listar contas
[3] Acessar conta corrente
[0] Voltar
""")

        opcao = input("Opção: ").strip()

        match opcao:
            case "1":
                criar_conta(cliente, clientes)

            case "2":
                listar_contas(cliente)

            case "3":
                conta = selecionar_conta(cliente)

                if conta is not None:
                    menu_conta(cliente, conta, clientes)

            case "0":
                break

            case _:
                print("Opção inválida.")


def main():
    clientes = carregar_dados()

    while True:
        print("""
===================================
          SISTEMA BANCÁRIO
===================================

[1] Cadastrar cliente
[2] Acessar sistema
[0] Encerrar
""")

        opcao = input("Opção: ").strip()

        match opcao:
            case "1":
                criar_cliente(clientes)

            case "2":
                cpf = solicitar_cpf()
                cliente = buscar_cliente(clientes, cpf)

                if cliente is not None:
                    menu_cliente(cliente, clientes)
                else:
                    print("Cliente não encontrado.")

            case "0":
                print("Sistema encerrado.")
                break

            case _:
                print("Opção inválida.")


if __name__ == "__main__":
    main()
