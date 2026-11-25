from datetime import datetime
from abc import ABC, abstractmethod


class Historico:

    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(transacao.registro())

    def __str__(self):
        if not self.transacoes:
            return "Nenhuma movimentação realizada."

        extrato = []

        for transacao in self.transacoes:
            extrato.append(
                f"{transacao['data_hora']} | "
                f"{transacao['tipo']} | "
                f"R$ {transacao['valor']:.2f}"
            )

        return "\n".join(extrato)


class Transacao(ABC):

    def __init__(self, valor):
        self._valor = valor
        self._data_hora = datetime.now()

    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

    def registro(self):
        return {
            "tipo": self.__class__.__name__,
            "valor": self.valor,
            "data_hora": self._data_hora.isoformat(sep=" ", timespec="seconds"),
        }


class Saque(Transacao):

    def __init__(self, valor):
        super().__init__(valor)

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso = conta.sacar(self.valor)

        if sucesso:
            conta.historico.adicionar_transacao(self)

        return sucesso


class Deposito(Transacao):

    def __init__(self, valor):
        super().__init__(valor)

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso = conta.depositar(self.valor)

        if sucesso:
            conta.historico.adicionar_transacao(self)

        return sucesso
