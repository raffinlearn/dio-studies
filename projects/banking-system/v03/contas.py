from datetime import date

from transacoes import Historico


class Conta:

    def __init__(self, numero, cliente):
        self._saldo = 0.0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido.")

        elif valor > self.saldo:
            print("Saldo insuficiente.")

        else:
            self._saldo -= valor
            print("Saque realizado com sucesso!")
            return True

        return False

    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido.")
            return False

        self._saldo += valor
        print("Depósito realizado com sucesso!")
        return True

    def mostrar_extrato(self):
        return str(self.historico)


class ContaCorrente(Conta):

    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)

        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        hoje = date.today().isoformat()

        numero_saques = sum(
            1
            for transacao in self.historico.transacoes
            if transacao["tipo"] == "Saque" and transacao["data_hora"].startswith(hoje)
        )

        if numero_saques >= self._limite_saques:
            print("Limite diário de saques atingido.")
            return False

        if valor > self._limite:
            print("Valor de saque excedeu o limite.")
            return False

        return super().sacar(valor)

    def __str__(self):
        return (
            f"Agência: {self.agencia}\n"
            f"Conta: {self.numero}\n"
            f"Titular: {self.cliente.nome}\n"
            f"Saldo: R$ {self.saldo:.2f}"
        )
