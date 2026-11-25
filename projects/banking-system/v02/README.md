# Sistema Bancário — V02

## Sobre o projeto

Segunda versão do sistema bancário desenvolvido em Python como parte dos desafios de projeto da plataforma Digital Innovation One (DIO).

Esta versão apresenta uma evolução da implementação inicial, utilizando funções, modularização e separação de responsabilidades para organizar as funcionalidades do sistema bancário.

Além das operações básicas de depósito, saque e extrato, foram introduzidos o cadastro de usuários, o gerenciamento de contas correntes e a persistência de dados utilizando arquivos JSON.

## Objetivos

- Aplicar funções na organização do código.
- Desenvolver soluções modulares e reutilizáveis.
- Separar as responsabilidades da aplicação.
- Implementar o cadastro e a identificação de usuários.
- Gerenciar múltiplas contas bancárias.
- Trabalhar com listas e dicionários.
- Implementar a persistência de dados em arquivos JSON.
- Aplicar validações e tratamento de exceções.

## Funcionalidades

### Cadastro de usuários

- Cadastro de nome completo.
- Cadastro de CPF.
- Cadastro de data de nascimento.
- Cadastro de endereço.
- Validação do formato do CPF.
- Verificação de CPF já cadastrado.
- Validação da data de nascimento.
- Persistência dos dados cadastrais em JSON.

### Identificação do usuário

- Identificação através do CPF.
- Normalização do CPF informado.
- Busca de usuários cadastrados.
- Possibilidade de realizar um novo cadastro quando o usuário não for encontrado.

### Gerenciamento de contas correntes

- Criação de contas correntes.
- Geração sequencial do número da conta.
- Associação da conta ao CPF do usuário.
- Identificação da agência bancária.
- Busca de contas existentes.
- Verificação da titularidade da conta.
- Possibilidade de possuir múltiplas contas.

### Depósito

- Realização de depósitos.
- Validação de valores positivos.
- Atualização do saldo.
- Registro da movimentação no extrato da sessão.

### Saque

- Realização de saques.
- Validação do saldo disponível.
- Controle do limite por saque.
- Controle da quantidade de saques.
- Registro da movimentação no extrato da sessão.

### Extrato bancário

- Exibição das movimentações realizadas durante a sessão.
- Numeração das movimentações.
- Exibição do saldo disponível.
- Identificação da ausência de movimentações.

### Persistência de dados

- Armazenamento dos usuários em arquivos JSON.
- Armazenamento das contas bancárias em arquivos JSON.
- Recuperação dos dados armazenados.
- Atualização do saldo ao encerrar o menu de operações bancárias.

## Regras de negócio

| Regra                    | Definição                                                      |
| ------------------------ | -------------------------------------------------------------- |
| Agência bancária         | 0001                                                           |
| Saldo inicial            | R$ 0,00                                                        |
| Identificação do usuário | CPF                                                            |
| CPF                      | Deve conter 11 caracteres numéricos e não pode estar duplicado |
| Número da conta          | Gerado sequencialmente                                         |
| Titularidade             | Conta associada ao CPF do usuário                              |
| Valor de depósito        | Maior que zero                                                 |
| Valor de saque           | Maior que zero                                                 |
| Limite por saque         | R$ 500,00                                                      |
| Limite de saques         | 3 por sessão bancária                                          |
| Saldo insuficiente       | Operação não permitida                                         |
| Data de nascimento       | Não pode ser uma data futura                                   |

## Conceitos aplicados

- Definição e utilização de funções.
- Modularização.
- Importação de módulos.
- Separação de responsabilidades.
- Argumentos posicionais.
- Argumentos nomeados.
- Parâmetros exclusivamente posicionais (`/`).
- Parâmetros exclusivamente nomeados (`*`).
- Retorno de múltiplos valores.
- Listas e dicionários.
- Expressões geradoras.
- Funções `any()` e `enumerate()`.
- Manipulação de strings.
- Tratamento de exceções com `try/except`.
- Manipulação de arquivos.
- Gerenciadores de contexto (`with`).
- Serialização e desserialização JSON.
- Manipulação de datas.
- Manipulação de caminhos com `pathlib`.

## Tecnologias utilizadas

- Python 3
- JSON
- Git
- GitHub
- Visual Studio Code

### Bibliotecas da biblioteca padrão

| Biblioteca | Finalidade                           |
| ---------- | ------------------------------------ |
| `json`     | Leitura e gravação de arquivos JSON  |
| `datetime` | Manipulação e validação de datas     |
| `pathlib`  | Manipulação de caminhos e diretórios |

O projeto não necessita de bibliotecas externas.

## Estrutura do projeto

```
v02/
├── main.py
├── contas.py
├── cx_eletronico.py
├── usuario.py
└── README.md
```

### Responsabilidades dos módulos

| Arquivo            | Responsabilidade                                                               |
| ------------------ | ------------------------------------------------------------------------------ |
| `main.py`          | Inicialização e integração dos módulos                                         |
| `contas.py`        | Criação, busca e seleção de contas correntes                                   |
| `cx_eletronico.py` | Identificação do usuário, operações bancárias, extrato e persistência do saldo |
| `usuario.py`       | Cadastro, validação, busca e persistência dos usuários                         |

## Armazenamento de dados

A aplicação utiliza dois arquivos JSON:

```
dados/
├── usuario.json
└── contas.json
```

O arquivo `usuario.json` armazena os dados cadastrais dos usuários.

O arquivo `contas.json` armazena os dados das contas bancárias, incluindo agência, número da conta, CPF do titular e saldo.

O diretório de dados locais não é versionado pelo Git, evitando a exposição de informações pessoais.

## Como executar

Acesse o diretório da versão:

```bash
cd projects/banking-system/v02
```

Antes da execução, é necessário ajustar o caminho do diretório de dados definido no arquivo `main.py`, pois a implementação original utiliza um caminho específico do ambiente anterior de desenvolvimento.

Também é necessário criar os arquivos `usuario.json` e `contas.json` no diretório de dados, inicializando cada um com uma lista JSON vazia:

```json
[]
```

Após configurar o caminho e os arquivos, execute:

```bash
python main.py
```

## Fluxo da aplicação

1. Inicialização do caixa eletrônico.
2. Carregamento dos usuários e contas armazenados.
3. Identificação do usuário através do CPF.
4. Cadastro de um novo usuário, quando necessário.
5. Criação ou seleção de uma conta corrente.
6. Acesso ao menu de operações bancárias.
7. Realização de depósitos, saques ou consulta de extrato.
8. Atualização dos dados ao encerrar a sessão bancária.

## Limitações da versão

- Dependência da criação prévia dos arquivos JSON.
- Caminho de armazenamento dependente do ambiente original de desenvolvimento.
- Ausência de programação orientada a objetos.
- Ausência de persistência do histórico de transações.
- Limite de saques reiniciado a cada sessão bancária.
- Persistência do saldo realizada somente ao encerrar o menu bancário.
- Tratamento parcial de entradas inválidas.
- Ausência de tratamento completo para erros de leitura e gravação de arquivos.
- Identificação por CPF sem mecanismos de autenticação.
- Ausência de validação dos dígitos verificadores do CPF.
- Ausência de testes automatizados.

## Evolução em relação à V01

| Característica          | V01                 | V02                     |
| ----------------------- | ------------------- | ----------------------- |
| Paradigma               | Procedural          | Procedural modularizado |
| Organização             | Arquivo único       | Múltiplos módulos       |
| Funções                 | Não                 | Sim                     |
| Cadastro de usuários    | Não                 | Sim                     |
| Gerenciamento de contas | Não                 | Sim                     |
| Persistência JSON       | Não                 | Parcial                 |
| Estruturas de dados     | Variáveis e strings | Listas e dicionários    |
| Tratamento de exceções  | Não                 | Parcial                 |

Esta versão representa a transição entre uma implementação procedural concentrada em um único arquivo e uma aplicação modularizada com responsabilidades distribuídas.

A próxima versão introduz a programação orientada a objetos, aprimorando a representação das entidades e a organização das regras de negócio.

## Referências

- [Digital Innovation One (DIO)](https://www.dio.me/)
- [Repositório oficial da Trilha Python — DIO](https://github.com/digitalinnovationone/trilha-python-dio)
- [Documentação oficial do Python](https://docs.python.org/pt-br/3/)

## Status

**Implementação histórica preservada — requer configuração do armazenamento local para execução.**
