import json
from pathlib import Path
from clientes import PessoaFisica

def ler_json(caminho, nome_arquivo):
    arquivo_json = caminho / nome_arquivo
    with open(arquivo_json, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
    return dados

def salvar_json(caminho, nome_arquivo, dados):
    arquivo_json = caminho / nome_arquivo
    with open(arquivo_json, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

def caminho_cliente(nome):
    caminho = Path(f"dados/clientes/{nome}")
    return caminho

def caminho_conta(nome, conta):
    caminho = Path(f"dados/clientes/{nome}/conta_{conta}")
    return caminho

def criar_pasta(nome, numero_conta=0):
    caminho = caminho_cliente(nome)
    if not caminho.exists():
        caminho.mkdir(parents=True, exist_ok=True)

    elif numero_conta != 0:
        caminho = caminho_conta(nome, numero_conta)

        if not caminho.exists():
            caminho.mkdir(parents=True, exist_ok=True)


def criar_cadastro():
    nome = input("Nome: ")
    ano_nascimento = input("Ano de Nascimento: ")
    cpf = input("CPF: ")
    telefone = input("Telefone DDD+Numero: ")
    endereço = input("Endereço Rua/n: ")

    pessoa = PessoaFisica(nome, ano_nascimento, cpf, telefone, endereço)

    cadastro = {
        "dados": pessoa.dados,
        "contas": []   
    }

    nome = nome.replace(' ','_').lower()
    criar_pasta(nome)
    caminho = caminho_cliente(nome)
    salvar_json(caminho, "dados_cadastrais", cadastro )
    return cadastro

def criar_conta(cliente):
    from contas import ContaCorrente
    contas = cliente["contas"]
    if contas:
        numero_conta = contas[-1]["numero"] + 1
    else:
        numero_conta = 1

    conta = ContaCorrente(numero_conta)
    nome = cliente["dados"]["nome"]
    nome = nome.replace(" ", "_").lower()

    criar_pasta(nome, numero_conta)
    criar_historico(nome, numero_conta)

    caminho = caminho_cliente(nome)
    cadastro = ler_json(caminho, "dados_cadastrais.json")

    dados_conta = {
        "agencia": conta.agencia,
        "numero": conta.numero,
        "tipo": "corrente",
        "saldo": conta.saldo
    }

    cadastro["contas"].append(dados_conta)
    salvar_json(caminho, "dados_cadastrais.json", cadastro)
  

def criar_historico(nome, conta):
    caminho = caminho_conta(nome, conta)
    historico = []
    salvar_json(caminho, "historico", historico)