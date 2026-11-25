class Cliente:

    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        if conta not in self.contas:
            return False

        return transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):

    def __init__(self, nome, data_nascimento, cpf, telefone, endereco):
        super().__init__(endereco)

        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.telefone = telefone

    def registro(self):
        return {
            "nome": self.nome,
            "data_nascimento": self.data_nascimento.isoformat(),
            "cpf": self.cpf,
            "telefone": self.telefone,
            "endereco": self.endereco,
        }
