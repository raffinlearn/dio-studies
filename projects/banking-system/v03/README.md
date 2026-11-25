# Sistema Bancário — V03

## Sobre o projeto

Terceira versão do sistema bancário desenvolvido em Python como parte dos desafios de projeto da plataforma Digital Innovation One (DIO).

Esta versão apresenta a evolução da aplicação para o paradigma de programação orientada a objetos (POO), utilizando classes, objetos, herança, encapsulamento, abstração, polimorfismo e composição.

A implementação busca representar as entidades de um sistema bancário, distribuindo as responsabilidades entre clientes, contas, transações e histórico de movimentações.

Também propõe a evolução da persistência de dados iniciada na versão anterior, utilizando uma estrutura de diretórios e arquivos JSON individuais para clientes e contas.

## Objetivos

- Aplicar os princípios da programação orientada a objetos.
- Modelar entidades e relacionamentos.
- Distribuir responsabilidades entre classes.
- Utilizar herança e polimorfismo.
- Aplicar encapsulamento de atributos.
- Implementar classes abstratas.
- Trabalhar com composição de objetos.
- Organizar as regras de negócio.
- Integrar as operações bancárias ao histórico de transações.
- Aprimorar a persistência de dados.
- Desenvolver uma aplicação modular e organizada.

## Modelagem do sistema

A aplicação é dividida em oito classes principais.

### Cliente

Representa a entidade base dos clientes do sistema bancário.

Responsabilidades:

- Armazenar os dados do cliente.
- Gerenciar as contas associadas.
- Adicionar novas contas.
- Intermediar a execução de transações em contas associadas ao cliente.

### PessoaFisica

Especialização da classe `Cliente`.

Atributos cadastrais:

- Nome.
- Ano de nascimento.
- CPF.
- Telefone.
- Endereço.

Responsabilidades:

- Representar um cliente pessoa física.
- Organizar seus dados cadastrais.
- Gerar uma representação dos dados em formato de dicionário.

### Conta

Representa a entidade base das contas bancárias.

Responsabilidades:

- Armazenar a agência.
- Armazenar o número da conta.
- Controlar o saldo.
- Realizar depósitos.
- Realizar saques.
- Possuir um histórico de transações.
- Disponibilizar a consulta de extrato.

A consulta de extrato ainda necessita de integração com os dados do titular.

### ContaCorrente

Especialização da classe `Conta`.

Responsabilidades:

- Controlar o limite por saque.
- Controlar a quantidade de saques realizados.
- Aplicar regras específicas de retirada.
- Reutilizar as operações bancárias da classe base.

### Historico

Responsável por representar o histórico de movimentações bancárias.

Responsabilidades previstas:

- Armazenar transações realizadas.
- Recuperar movimentações persistidas em JSON.
- Organizar os registros de transações.
- Disponibilizar uma representação textual do extrato.

A integração entre o histórico em memória e o armazenamento em arquivos ainda está em desenvolvimento.

### Transacao

Classe abstrata responsável por representar a estrutura base das transações bancárias.

Atributos:

- Identificador.
- Valor.
- Data e hora.

Responsabilidades:

- Validar o valor da transação.
- Definir a estrutura básica do registro.
- Estabelecer um contrato abstrato para a geração dos registros das transações.

### Saque

Especialização da classe `Transacao`.

Responsabilidades:

- Representar uma operação de retirada.
- Executar o saque através da conta bancária.
- Gerar o registro da operação.
- Encaminhar transações bem-sucedidas ao histórico.

A integração com o método de inclusão no histórico ainda necessita de correção.

### Deposito

Especialização da classe `Transacao`.

Responsabilidades:

- Representar uma operação de depósito.
- Executar o depósito através da conta bancária.
- Gerar o registro da operação.
- Encaminhar transações bem-sucedidas ao histórico.

A integração com o método de inclusão no histórico ainda necessita de correção.

## Relacionamentos entre classes

| Classe               | Relacionamento | Classe relacionada |
| -------------------- | -------------- | ------------------ |
| `PessoaFisica`       | Herança        | `Cliente`          |
| `ContaCorrente`      | Herança        | `Conta`            |
| `Saque`              | Herança        | `Transacao`        |
| `Deposito`           | Herança        | `Transacao`        |
| `Cliente`            | Associação     | `Conta`            |
| `Conta`              | Composição     | `Historico`        |
| `Historico`          | Associação     | `Transacao`        |
| `Saque` e `Deposito` | Dependência    | `Conta`            |

Os relacionamentos representam a modelagem atual do domínio. Parte da integração entre os objetos e a camada de persistência ainda está em desenvolvimento.

## Funcionalidades e situação atual

| Funcionalidade                       | Situação                                        |
| ------------------------------------ | ----------------------------------------------- |
| Modelagem de clientes                | Implementada                                    |
| Modelagem de contas bancárias        | Implementada                                    |
| Cadastro de clientes                 | Parcialmente implementado                       |
| Criação de contas correntes          | Parcialmente implementada                       |
| Identificação por CPF                | Parcialmente implementada                       |
| Regras de depósito                   | Implementadas na classe Conta                   |
| Regras de saque                      | Implementadas nas classes Conta e ContaCorrente |
| Modelagem de transações              | Implementada                                    |
| Registro de histórico                | Em integração                                   |
| Consulta de extrato                  | Em desenvolvimento                              |
| Persistência de dados cadastrais     | Em integração                                   |
| Persistência de saldo                | Pendente                                        |
| Persistência de transações           | Pendente                                        |
| Recuperação de objetos armazenados   | Pendente                                        |
| Menu completo de operações bancárias | Pendente                                        |
| Testes automatizados                 | Pendente                                        |

## Regras de negócio

| Regra                    | Definição                             |
| ------------------------ | ------------------------------------- |
| Agência bancária         | 0001                                  |
| Saldo inicial            | R$ 0,00                               |
| Valor de transação       | Maior que zero                        |
| Limite padrão por saque  | R$ 500,00                             |
| Limite padrão de saques  | 3 por instância da conta corrente     |
| Saldo insuficiente       | Saque não permitido                   |
| Associação de contas     | Cliente pode possuir múltiplas contas |
| Registro de transações   | Operações realizadas com sucesso      |
| Identificação do cliente | CPF                                   |

## Conceitos aplicados

### Programação orientada a objetos

- Classes e objetos.
- Construtores (`__init__`).
- Atributos de instância.
- Métodos de instância.
- Encapsulamento por convenção.
- Propriedades com `@property`.
- Herança.
- Polimorfismo.
- Sobrescrita de métodos.
- Utilização de `super()`.
- Abstração.
- Classes abstratas com `ABC`.
- Métodos abstratos com `@abstractmethod`.
- Composição.
- Associação entre objetos.
- Métodos especiais como `__str__`.

### Conceitos complementares

- Modularização.
- Separação de responsabilidades.
- Manipulação de arquivos.
- Manipulação de diretórios.
- Serialização JSON.
- Manipulação de datas e horários.
- Listas e dicionários.
- Validação de regras de negócio.
- Tratamento de valores inválidos com `ValueError`.

## Tecnologias utilizadas

- Python 3
- JSON
- Git
- GitHub
- Visual Studio Code

### Bibliotecas da biblioteca padrão

| Biblioteca | Finalidade                                   |
| ---------- | -------------------------------------------- |
| `abc`      | Implementação de classes e métodos abstratos |
| `datetime` | Registro da data e hora das transações       |
| `json`     | Persistência e recuperação de dados          |
| `pathlib`  | Gerenciamento de caminhos e diretórios       |

O projeto não necessita de bibliotecas externas.

## Estrutura atual do projeto

```
v03/
├── clientes.py
├── contas.py
├── sistema.py
├── teste.py
├── transaçao.py
└── README.md
```

### Responsabilidades dos módulos

| Arquivo        | Responsabilidade                                              |
| -------------- | ------------------------------------------------------------- |
| `clientes.py`  | Modelagem dos clientes e pessoas físicas                      |
| `contas.py`    | Modelagem das contas e regras das operações bancárias         |
| `transaçao.py` | Modelagem das transações e do histórico                       |
| `sistema.py`   | Gerenciamento de arquivos, diretórios e persistência de dados |
| `teste.py`     | Implementação experimental do fluxo do caixa eletrônico       |

O arquivo `teste.py` representa um protótipo de integração da aplicação e não uma suíte de testes automatizados.

## Estrutura de armazenamento

A persistência de dados foi planejada para utilizar uma estrutura individualizada por cliente e conta bancária.

```
dados/
└── clientes/
    └── nome_cliente/
        ├── dados_cadastrais.json
        ├── conta_1/
        │   └── historico.json
        └── conta_2/
            └── historico.json
```

### Dados cadastrais

Armazenamento previsto:

- Nome.
- Ano de nascimento.
- CPF.
- Telefone.
- Endereço.
- Contas bancárias associadas.
- Dados e saldo das contas.

### Histórico bancário

Armazenamento previsto:

- Identificador da transação.
- Tipo da transação.
- Valor.
- Data e hora.

A estrutura apresentada representa o objetivo da implementação. A geração, recuperação e atualização consistente desses arquivos ainda precisam ser finalizadas.

Os dados locais não são versionados pelo Git.

## Como executar

Acesse o diretório desta versão:

```bash
cd projects/banking-system/v03
```

O ponto de entrada experimental está localizado no arquivo `teste.py`:

```bash
python teste.py
```

**Atenção:** esta versão ainda está em desenvolvimento. O fluxo completo não está operacional e poderá apresentar erros relacionados à inicialização dos diretórios, persistência de arquivos e integração entre objetos.

## Fluxo previsto da aplicação

1. Inicialização do caixa eletrônico.
2. Identificação do cliente através do CPF.
3. Recuperação ou criação do cadastro.
4. Recuperação das contas associadas ao cliente.
5. Criação ou seleção de uma conta corrente.
6. Acesso ao menu de operações bancárias.
7. Execução de depósitos e saques.
8. Registro das transações realizadas.
9. Atualização do saldo e do histórico.
10. Consulta do extrato bancário.
11. Persistência das alterações realizadas.

## Evolução em relação às versões anteriores

| Característica                  | V01 | V02     | V03                |
| ------------------------------- | --- | ------- | ------------------ |
| Programação procedural          | Sim | Sim     | Parcial            |
| Modularização                   | Não | Sim     | Sim                |
| Cadastro de clientes            | Não | Sim     | Em integração      |
| Gerenciamento de contas         | Não | Sim     | Em integração      |
| Persistência JSON               | Não | Parcial | Em desenvolvimento |
| Programação orientada a objetos | Não | Não     | Sim                |
| Herança                         | Não | Não     | Sim                |
| Encapsulamento                  | Não | Não     | Sim                |
| Classes abstratas               | Não | Não     | Sim                |
| Polimorfismo                    | Não | Não     | Sim                |
| Composição de objetos           | Não | Não     | Sim                |
| Modelagem de transações         | Não | Não     | Sim                |

## Roadmap de finalização

- [x] Modelar as classes principais.
- [x] Implementar as regras básicas de saque e depósito.
- [x] Implementar herança e classes abstratas.
- [x] Criar funções iniciais de manipulação de arquivos JSON.
- [x] Implementar um menu experimental de clientes.
- [ ] Padronizar nomes de arquivos, atributos e métodos.
- [ ] Corrigir a criação dos diretórios e arquivos JSON.
- [ ] Integrar clientes e contas através de objetos.
- [ ] Implementar a recuperação dos objetos persistidos.
- [ ] Corrigir a integração entre transações e histórico.
- [ ] Implementar a persistência do saldo bancário.
- [ ] Implementar a persistência do histórico de transações.
- [ ] Finalizar o menu de operações bancárias.
- [ ] Implementar o tratamento de entradas inválidas.
- [ ] Validar as regras de negócio.
- [ ] Implementar testes automatizados.
- [ ] Atualizar a documentação final.

## Limitações atuais

- Inconsistências nos nomes dos arquivos JSON.
- Inconsistências na nomenclatura dos métodos de histórico.
- Ausência de referência direta ao titular na classe Conta.
- Ausência de integração completa entre os objetos e a persistência.
- Ausência de serialização adequada dos registros contendo data e hora.
- Fluxo de criação de contas ainda incompleto.
- Possibilidade de colisão entre diretórios de clientes com nomes iguais.
- Identificação por CPF sem autenticação.
- Ausência de testes automatizados.

Essas limitações serão tratadas durante a finalização do projeto.

## Referências

- [Digital Innovation One (DIO)](https://www.dio.me/)
- [Repositório oficial da Trilha Python — DIO](https://github.com/digitalinnovationone/trilha-python-dio)
- [Documentação oficial do Python](https://docs.python.org/pt-br/3/)

## Status

**Em desenvolvimento — modelagem orientada a objetos implementada e integração das funcionalidades pendente.**
