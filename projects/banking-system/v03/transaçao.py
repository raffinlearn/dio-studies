from datetime import datetime
from sistema import ler_json, caminho_conta
from abc import ABC, abstractmethod


class Historico:

    def __init__(self):
        self._transações = []
        self.extrato_completo = []

    def adicionar_transação(self, transação):
        self._transações.append(transação)

    def abrir_extrato(self, nome, conta):
        caminho = caminho_conta(nome, conta)
        arquivo = ler_json(caminho, "historico.json")

        self.extrato_completo = arquivo

        return self.extrato_completo

    def __str__(self):
        extrato = ""

        for transacao in self.extrato_completo:
            extrato += f"{transacao}\n"

        return extrato


class Transacao(ABC):

    def __init__(self, valor=0):
        self._id = 0
        self.data_hora = datetime.now()

        if valor > 0:
            self._valor = valor
        else:
            raise ValueError("O valor da transação deve ser maior que zero.")

    @abstractmethod
    def registro(self):
        return {
            "id": self._id,
            "data/hora": self.data_hora,
            "tipo": "",
            "valor": self._valor,
        }


class Saque(Transacao):

    def __init__(self, valor):
        super().__init__(valor)

    @property
    def valor(self):
        return self._valor

    def registro(self):
        registro = super().registro()
        registro.update({
            "tipo": "Saque"
        })
        return registro

    def executar(self, conta):
        executar_transacao = conta.sacar(self.valor)

        if executar_transacao:
            conta._historico.adicionar_transacao(self)


class Deposito(Transacao):

    def __init__(self, valor):
        super().__init__(valor)

    @property
    def valor(self):
        return self._valor

    def registro(self):
        registro = super().registro()
        registro.update({
            "tipo": "Deposito"
        })
        return registro

    def executar(self, conta):
        executar_transacao = conta.depositar(self.valor)

        if executar_transacao:
            conta._historico.adicionar_transacao(self)