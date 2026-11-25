import json
from pathlib import Path
from datetime import date

from clientes import PessoaFisica
from contas import ContaCorrente

DIRETORIO = Path(__file__).resolve().parent / "dados"
ARQUIVO = DIRETORIO / "banco.json"


def salvar_dados(clientes):
    DIRETORIO.mkdir(parents=True, exist_ok=True)

    dados = []

    for cliente in clientes:
        registro = cliente.registro()
        registro["contas"] = []

        for conta in cliente.contas:
            registro["contas"].append(
                {
                    "numero": conta.numero,
                    "agencia": conta.agencia,
                    "saldo": conta.saldo,
                    "historico": conta.historico.transacoes,
                }
            )

        dados.append(registro)

    with ARQUIVO.open("w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)


def carregar_dados():
    if not ARQUIVO.exists():
        return []

    with ARQUIVO.open("r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    clientes = []

    for registro in dados:
        cliente = PessoaFisica(
            nome=registro["nome"],
            data_nascimento=date.fromisoformat(registro["data_nascimento"]),
            cpf=registro["cpf"],
            telefone=registro["telefone"],
            endereco=registro["endereco"],
        )

        for dados_conta in registro["contas"]:
            conta = ContaCorrente.nova_conta(cliente, dados_conta["numero"])

            conta._saldo = dados_conta["saldo"]

            conta.historico.transacoes.extend(dados_conta["historico"])

            cliente.adicionar_conta(conta)

        clientes.append(cliente)

    return clientes


def buscar_cliente(clientes, cpf):
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente

    return None


def proximo_numero_conta(clientes):
    numeros = [conta.numero for cliente in clientes for conta in cliente.contas]

    return max(numeros, default=0) + 1
