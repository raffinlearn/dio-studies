from pathlib import Path
from sistema import ler_json, criar_conta, criar_cadastro


def iniciar_caixa_eletronico():
    print("=" * 30)
    print("Iniciar Caixa Eletrônico".center(30))
    print("=" * 30)

    cpf = input("\nLogin [CPF]: ").replace(".", "").replace("-", "")

    if len(cpf) != 11 or not cpf.isnumeric():
        print("CPF inválido")
        return

    caminho = Path("dados/clientes")

    for pasta_cliente in caminho.iterdir():
        if pasta_cliente.is_dir():
            cliente = ler_json(pasta_cliente, "dados_cadastrais.json")

            if cpf == cliente["dados"]["cpf"]:
                return cliente

    return None

def menu_cliente(cliente):
    print("=" * 30)
    print(f"Bem vindo {cliente["dados"]["nome"]}".center(30))
    print("=" * 30)

    while True:
        print("""
[1] Criar conta corrente
[2] Acessar conta corrente
[0] Sair
""")
        menu = int(input("Digite uma opção: "))

        if menu not in (1, 2, 0):
            print("Opção inválida.")
            continue

        if menu == 1:
            conta_corrente = criar_conta(cliente)
            return conta_corrente

        elif menu == 2:
            numero_conta = int(input("Digite o número da conta corrente: "))
            print("Busca da conta ainda será implementada.")
            for conta in cliente["contas"]:
                if numero_conta == conta["numero"]:
                    return conta

        elif menu == 0:
            break



def caixa_eletronico():
    cliente = iniciar_caixa_eletronico()
    if cliente is None:
        cliente = criar_cadastro()

    menu_cliente(cliente)

caixa_eletronico()